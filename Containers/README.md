# Containers
Containers provide a way to deploy tools used in a workflow. The two primary container engines utilized in bioinformatics are Docker and Singularity. They also provide a way to conduct reproducible computations as the tools can be version tagged. Containers can either be used such that one container has all the tools for a given workflow. Alternatively a unique container can be used for each step of the workflow. In my opinion this second approach is more flexible. It would enable the easy drop in of a different version or different tool with minimal modification of the workflow. 


# Nextflow
Nextflow supports both Docker and Singularity containers. 
## Enabling containers
The easiest way to enable Docker of Singularity for Nextflow is using the `nextflow.config` file. Enabling either container engine can be done simply by using `docker.enabled = true` or `singularity.enabled = true`

## Specifying a container
Nextflow allows you to specify either on container to be used for the entire workflow or an individual container for each process block. Containers can be specified in a number of ways:
* The `nextflow.config` file using `process.container = CONTAINER`
* In `nextflow.config` for a specific process `process.$PROCESSNAME.container = CONTAINER`
* Within a given process block such as
```
process demo{
  container 'CONTAINER'
}
```

## Singularity and Docker interoperability
Nextflow supports using either Docker Hub of Singularity Hub images with the Singularity engine. When Singularity pulls a Docker Hub image it is converted into a Singularity image automatically. 

Docker Hub:
```
process demo{
  container 'docker://CONTAINER'
}
```

Singularity Hub:
```
process demo{
  container 'shub://CONTAINER'
}
```

# CWL 
CWL supports Docker with work being done to add in Singularity support.

## Specifying a container
Docker containers can be specified as a hint inside of a `CommandLineTool` file. 
```
hints:
  DockerRequirement:
    dockerPull: CONTAINER
```

# Snakemake 
## Specifying a container
Snakemake allows individual Singularity containers to be used for each rule. 
```
  singularity:
    "docker://biocontainers/bowtie2"
```

## Singularity and Docker interoperability
Snakemake can use either Docker Hub or Singularity Hub images with Singularity. 
Docker Hub:
```
  singularity:
    "docker://CONTAINER"
```

Singularity Hub:
```
  singularity:
    "shub://CONTAINER"
```

# Conclusions
All three workflows provide some level of container support. Nextflow seems to offer the most flexibility at the time of writing. It enables the relatively easy use of either Singularity or Docker. With the Singularity engine it is also possible to use a mix of Docker Hub and Singularity Hub images. It provides the option of using either one container, or individual containers for each process. 

The CWL Docker support is also quite nice. Enabling the use of a different container for each `CommandLineTool` or one container for a `Workflow`. The addition of Singularity support will definitely be advantageous. 

Snakemakes support for Singularity works nicely, and the support for images from either Docker Hub or Singularity Hub is nice to have. Snakemake seemingly does not support the use
of an individual Docker container for each task which is limiting for groups using primarily docker. 

#Outstanding questions
* CWL CommandLineTool vs Workflow Docker
* Snakemake docker individual containers?
* compare the use of private repositories 
