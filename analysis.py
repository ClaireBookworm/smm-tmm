from binascii import a2b_hex
import json
# from xml.etree.ElementTree import tostring
import pandas
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
	try:
		mturk = data["d_mTurkID"][0]
	except:
		print("none: " + f)
		mturk = "NA"
	if int(data["imageTypeCorrect"][0]) < 35:
	# percentage = int(data["imageTypeCorrect"][0]) * 2
		# print(mturk + " type: " + exptype + " correct: " + data["imageTypeCorrect"][0] + "%")
		return False
	correct = 0
	for num in data["1=correct"]:
		correct += int(num)
	# print (correct)
	if correct < 60:
		# print(mturk + " type: " + exptype + " correct: " + str(correct) + "%")
		return

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
	checkaccuracy(data)

	for num in range(0, 49):
		data["d_mTurkID"].append(data["d_mTurkID"][0])
	generatecsv(data)
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
				# for key in value:
					# print (key)
				# writer.writerow(value[num])
			
			writer.writerow(row)
			row = []
		# print (a)
		# writer.writerow(a)

directory = 'od-files'

# iterate over files in
# that directory
for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	# checking if it is a file
	if os.path.isfile(f):
		exptype = f.split('_')[1].split('.')[0]
		# print (f)
		readfile(f, exptype)
		