# Nextflow
`nextflow run main.nf`

# CWL
`cwltool rnatoy.cwl rnatoy.yml`

# Snakemake 
`snakemake`

# Implementation
## Step 1
This step builds the index for the genome file. 

### Nextflow
```
process buildIndex {
    tag "$genome_file.baseName"
    
    input:
    file genome from genome_file
     
    output:
    file 'genome.index*' into genome_index
       
    """
    bowtie2-build --threads ${task.cpus} ${genome} genome.index
    """
}
```

### CWL
```
cwlVersion: v1.0
class: CommandLineTool

inputs:
  indexfile:
    type: File
    inputBinding:
      position: 1
  doing:
    type: string
    inputBinding:
      position: 2
outputs: 
  indexout:
    type: File[]
    outputBinding:
      glob: "*"
baseCommand: bowtie2-build
```

### Snakemake
```
rule buildIndex:
	message: 'indexing'
	input:
		genome
	output:
		"genome.index.1.bt2"

	shell:
		'bowtie2-build {genome} genome.index'
```