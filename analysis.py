import math
import csv
import os
from functools import reduce

# f = open("jsons/1658438224287_S1_TMM_backup.json")

# euc = open("eucdist.txt")

def clean_word(word):
	word = word.strip()
	word = word.replace(" ", "")
	word = word.replace("\t", "")
	word = word.replace("\n", "")
	word = word.replace(",", "")
	word = word.replace('\"', "")
	word = word.replace('{', "")
	word = word.replace('[', "")
	word = word.replace('}', "")
	word = word.replace(']', "")
	return word

# def analysis(dict):
# 	# euc.write(dict["d_mTurkID"][0] + "\n")
# 	dists = []
# 	for dist in dict["Euclidian_distance"]:
# 		if dist == -1:
# 			continue
# 		dists += [int(dist)]
# 	return reduce(lambda a, b: a + b, dists) / len(dists)
# 		# euc.write(dist + "\n")

def checkaccuracy (data):
	exptype = data["blockName"][0]

	try:
		mturk = data["d_mTurkID"][0]
	except:
		print("none: " + f)
		mturk = "NA"
	quizCorrect = int(data["imageTypeCorrect"][0])
	# if int(data["imageTypeCorrect"][0]) < 35:
	# # percentage = int(data["imageTypeCorrect"][0]) * 2
	# 	# print(mturk + " type: " + exptype + " correct: " + data["imageTypeCorrect"][0] + "%")
	# 	return Falses
	correct = 0
	for num in data["1=correct"]:
		correct += int(num)
	# print (correct)
	if correct < 60 or quizCorrect < 35:
		print(mturk + " type: " + exptype + " correct: " + str(correct) + "%" + " quiz correct: " + str(quizCorrect*2) + "%")
		return False
	return True

def readfile(file, exptype):
	# print (file)
	f = open(file)
	
	data = {
		"d_mTurkID": [],
		"round": [],
		"blockName": [],
		"Setsize": [],
		"cueLength": [],
		"test_ind": [],
		"test_timeStamp": [],
		"view_ind": [],
		"view_timeStamp": [],
		"1=OldItem": [],
		"Response": [],
		"1=correct": [],
		"viewLoc_index": [],
		"viewLoc_x": [],
		"viewLoc_y": [],
		"viewLoc_row": [],
		"viewLoc_col": [],
		"clickLoc_x": [],
		"clickLoc_y": [],
		"clickLoc_row": [],
		"clickLoc_column": [],
		"Euclidian_distance": [],
		"imageTypeCorrect": [],
		"imageTypeWrong": [],
		"TimeBarLoc_1st": [],
		"TimeBarLoc_resp": [],
		"TimeError_RespMinus1stAppear": [],
		"RT": [],
		"LapseTimeSinceExpStart": [],
		"imageID": [],
		"CanvasHeight": [],
		"CanvasWidth": [],
		"curID": [],
		"curTime": [],
		"userAgent": [],
		"windowWidth": [],
		"windowHeight": [],
		"screenWidth": [],
		"screenHeight": [],
		"duration_ms": []
	}

	for line in f:
		try:
			word = clean_word(line)
			if len(word.split(":")) == 1:
				continue
			# types.append(word.split(":")[0])
			init = word.split(":")[0]
			response = word.split(":")[1]
			data[init].append(response)
		except:
			continue
	
	for num in range(0, 49):
		data["d_mTurkID"].append(data["d_mTurkID"][0])
	checkaccuracy(data)
	# if checkaccuracy(data):
		# spatial_analysis(data)
		# generatecsv(data)
	return data



def generatecsv(data):
	if data["blockName"][0] == "Test":
		data["blockName"][0] = "Temporal"
	with open("csv2/" + data["blockName"][0] + '.csv', 'a') as f:
		writer = csv.writer(f)
		row = []
		for num in range(0,50):
			for value in data.values():
			# print (value[num]) 
				try:
					row.append(value[num])
				except:
					continue
			writer.writerow(row)
			row = []


def directory(path):
	# directory = 'od-files'
	directory = path

	# iterate over files in
	# that directory
	for filename in os.listdir(directory):
		f = os.path.join(directory, filename)
		# checking if it is a file
		if os.path.isfile(f):
			exptype = f.split('_')[1].split('.')[0]
			# print (f)
			readfile(f, exptype)

def spatial_analysis(data):
	sums = 0
	count = 0
	floats = []
	for dist in data['Euclidian_distance']:
		if float(dist) == float(-1):
			continue
		floats.append(float(dist))
		sums += float(dist)
		count += 1
	mean = float(sums/count)
	variance = 0
	for val in floats: 
		variance += abs(float(val) - mean) * abs(float(val) - mean)
	variance = variance / len(dist)
	stdev = math.sqrt(variance)
	print(stdev)

	rois = [0,0,0] # three ROIs, one stdev, 2 stdev, three stdev
	for val in floats:
		if val <= stdev:
			rois[0] += 1
			continue
		elif val <= stdev * 2:
			rois[1] += 1
			continue
		elif val > stdev * 2:
			rois[2] += 1

	# if count == 0:
	# 	print (data["d_mTurkID"][0] + "--" + data["blockName"][0] + "-> sum: " + str(float(sums)) + " count: " + str(count))
	# else:	
	# 	print (data["d_mTurkID"][0] + "--" + data["blockName"][0] + ": " + str(float(sums/count)))
	with open("analysis/spatial.csv", 'a') as f:
		writer = csv.writer(f)
		# writer.writerow(["mturk id", "experiment", "Temperature 2"])
		row = [data["d_mTurkID"][0], data["blockName"][0],float(sums),count,mean,stdev, rois[0], rois[1], rois[2]]
		writer.writerow(row)

directory('od-files')
