import time
import os
from Bio import SeqIO
from Bio.SeqIO.QualityIO import FastqGeneralIterator
from multiprocessing import Pool

def slowParse(filename):
	parsed = SeqIO.parse(filename,'fastq')

	laneDict = {}

	for record in parsed:
		lane = record.description.split(':')[3]
		if lane in laneDict.keys():
			laneDict[lane].append(record)
		else:
			laneDict[lane] = []
			laneDict[lane].append(record)

	for i in laneDict.keys():
		outname = filename.replace('.fq', '_' + i + '.fq')
		SeqIO.write(laneDict[i], outname, "fastq")

def fastParse(filename):
	laneDict = {}

	for title, seq, qual in FastqGeneralIterator(open(filename)):
		lane = title.split(':')[3]
		record = "@%s\n%s\n+\n%s" % (title, seq, qual)

		if lane in laneDict.keys():
			laneDict[lane].append(record)
		else:
			laneDict[lane] = []
			laneDict[lane].append(record)

	for i in laneDict.keys():
		basename = os.path.basename(filename)
		outname = basename.replace('.fq', '_' + i + '.fq')
		resultfolder = basename.replace('.fq','')
		if not os.path.exists(resultfolder):
				os.makedirs(resultfolder)
		outfile = open(resultfolder + '/' + outname,'w')
		outfile.write("\n".join(laneDict[i]))
		outfile.close()

def main():
	start = time.time()
	pool = Pool(processes=4)
	# the dirPath must be a complete path to the folder with fastq
	dirPath = '/home/kevin/rnatoy/data/ggal/data'
	files = []
	for i in os.listdir(dirPath):
		files.append(dirPath+'/'+i)

	# for j in files:
	# 	fastParse(j)
	pool.map(fastParse, files)
	end = time.time()
	print('Time to process: ' + str(end-start))

if __name__ == "__main__":
	main()