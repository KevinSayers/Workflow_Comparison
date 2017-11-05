# Snakemake
Snakemake offers a couple methods of modularization. The first is an `include`, this enables commonly used rules to be maintained separately and included when needed. The second main method of modularization is the use of wrappers. Wrappers abstract away writing the shell command for some common bioinformatics tools. These can be pulled either from the [Snakemake Wrappers](https://bitbucket.org/snakemake/snakemake-wrappers) or from available files using `file://` in the wrapper string. The workflow in the Snakemake folder demonstrates both of these modularization techniques.   

```
SAMFILES = ["toy"]

rule all:
	input:
		expand("out/{sample}.bai",sample=SAMFILES)

include: "SAM_to_BAM"

rule indexbam:
	input:	
		"out/{sample}.bam"
	output:
		"out/{sample}.bai"

	wrapper:
		"0.0.8/bio/samtools_index"
```

The include then points to the `SAM_to_BAM` file. The rules in this file are then available to the rest of the workflow. 
```
rule samtobam:
	input:
		"../../data/{sample}.sam"

	output:
		"out/{sample}.bam"
	shell:
		"samtools view -Sb  {input} > {output}"
```

One thing that is really nice about Snakemake is that includes do not have to specify the inputs or outputs due to the connections of the steps being based on the DAG. 

# CWL
CWL is modular by nature. It is possible to write a single CWL workflow file with each step included, but it messy. Writing a workflow file that points to a different CWL file for each step is seemingly more common in the community. The workflow file acts as a mapping of inputs and outputs from each of the steps. 

main workflow file:
```
cwlVersion: v1.0
class: Workflow

    
inputs:
  samfile: File
  bamfile: string

outputs:
  bams:
    type: File
    outputSource: samtobam/bamout

steps:
  samtobam:
    run: samtobam.cwl
    in:
      sam: samfile
      bam: bamfile
    out: [bamout]
```

step:
```
cwlVersion: v1.0
class: CommandLineTool
baseCommand: samtools

arguments: ["view","-Sb"]
inputs:
  sam:
    type: File
    inputBinding:
      position: 1
  bam:
    type: string
    inputBinding:
      position: 2
      prefix: "-o"
outputs: 
  bamout:
    type: File
    outputBinding:
      glob: "*.bam"
```

Above you can see the main workflow has an `in` section for the step `samtobam` with mappings from inputs in the workflow file to those in the step. For example `sam` from the workflow file maps to `samfile` in the step file. 

The mappings combined with CWL very verbose nature though does lead to significantly lenghtier workflows. This is especially true when compared to Snakemake's ability to infer the inputs and outputs from the DAG. 

# Nextflow
Nextflow currently has limited modularization abilities. It is possible to place the script block into a separate bash file for reuse. This allows independent testing of the command as it can be executed on the commandline. This implementation is not quite as polished as those offered by Snakemake and CWL. 

A simple workflow demonstrates the use of a template: 

```
process samtobam{
	input:
	file samfile from file("../../data/toy.sam")
	val bamfile from file("../../data/toy.sam").baseName


	output:
	file "*.bam" into bam

	script:
	template 'samtobam.sh'
}
```

The inputs are then made available to the bash script in the template folder.
```
#!/bin/bash
samtools view -Sb  ${samfile} > ${bamfile}.bam
```
