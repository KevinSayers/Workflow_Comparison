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
