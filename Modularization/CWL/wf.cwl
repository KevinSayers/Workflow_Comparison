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
