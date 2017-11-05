process samtobam{
	input:
	file samfile from file("../../data/toy.sam")
	val bamfile from file("../../data/toy.sam").baseName


	output:
	file "*.bam" into bam

	script:
	template 'samtobam.sh'
}