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

# CWL


# Nextflow
Nextflow currently lacks support for modularization. There is support for running a subworkflow by just executing `nextflow run subwf.nf` as part of a normal script block. 