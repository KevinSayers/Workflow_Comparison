# Containers

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

## Singularity and Docker interoperability


# CWL 
CWL supports Docker with work being done to add in Singularity support.

# Snakemake 
## Singularity and Docker interoperability
http://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html#running-jobs-in-containers