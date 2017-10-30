# Containers

# Nextflow
Nextflow supports both Docker and Singularity containers. 

## Specifying a container
Nextflow allows you to specify either on container to be used for the entire workflow or an individual container for each process block. Containers can be specified in a number of ways:
* The `nextflow.config` file using `docker.container = CONTAINER`
* In `nextflow.config` for a specific process `process.$PROCESSNAME.container = CONTAINER`
* Within a given process block such as
```
process demo{
  container 'CONTAINER'
}



# CWL 
CWL supports Docker with work being done to add in Singularity support.

# Snakemake 