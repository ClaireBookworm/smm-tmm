import json
# from xml.etree.ElementTree import tostring
import pandas
import csv
import os
from functools import reduce	

# f = open("jsons/1658438224287_S1_TMM_backup.json")

euc = open("eucdist.txt")

def clean_word(word):
	word = word.strip()
	word = word.replace(" ", "")
	word = word.replace("\t", "")
	word = word.replace("\n", "")
	word = word.replace(",", "")
	word = word.replace('\"', "")
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

def checkaccuracy (dict):
	# check for image type quiz
	testingCorrect = 0
	for key in dict.keys():
		if key == "imageTypeQuiz":
			# print(','.join(dict[key]).replace("[","").replace("]","").split(',')[0])
			print(','.join(dict[key]))
			correct = ','.join(dict[key]).replace("[","").replace("]","").split(',')[0]
			# incorrect = dict[key][1]
			# noResponse = 50 - correct - incorrect
			if int(correct) < 40:
				return False # not greater than 80%
		if key == "1=correct":
			for value in dict[key]:
				testingCorrect += int(value) # value = 1 if correct, 0 if incorrect
			if testingCorrect < 60:
				return False
	# print ("Accuracy: " + str(testingCorrect / 60 * 100) + "%")
	print ("Passed!")
	return True

def generatecsv(file, type):
	# print (file)
	f = open(file)
	
	data = {
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
		"imageTypeQuiz": [],
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
		"duration_ms": [],
		"d_mTurkID": []
	}

	for line in f:
		quiz = ""
		try:
			word = clean_word(line)
			if line[0] == "}" or line[0] == "{":
				continue
			if int(line).isnumeric():
				quiz += line + ","
				continue
			if len(word.split(":")) == 1:
				continue
			# types.append(word.split(":")[0])
			init = word.split(":")[0]
			response = word.split(":")[1]
			data[init].append(response)
		except:
			continue
	print (quiz)
	data["imageTypeQuiz"].append(quiz)
	checkaccuracy(data)
	# for key in data.keys():
	# 	if key = ""

	# fieldnames = []
	# for key in data.keys():
	# 	fieldnames.append(key)

	mturk = data["d_mTurkID"]
	# print (mturk)
	# analysis(data)
	# with open('results/' + mturk[0] + '_' + type + '.csv', 'w') as f:
	# 	writer = csv.writer(f)
	# 	writer.writerows(data.values())

directory = 'jsons'

# iterate over files in
# that directory
for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	# checking if it is a file
	if os.path.isfile(f):
		type = f.split('_')[1]
		# print (f)
		generatecsv(f, type)
		