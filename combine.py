# combine
import os

ids = []

def directory(path):
	directory = path
	# iterate over files in
	# that directory
	for filename in os.listdir(directory):
		f = os.path.join(directory, filename)
		# checking if it is a file
		if os.path.isfile(f):
			mturk = f.split('_')[0]
			exptype =  f.split('_')[1].split('.')[0]
			for i in ids:
				if i == mturk:
					with open(mturk + "_" + exptype "_.json", 'w') as f:
						file1 = open()
						f.write()
			
			readfile(f, exptype)

directory('officialdata')