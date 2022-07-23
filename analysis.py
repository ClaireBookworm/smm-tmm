import json
# from xml.etree.ElementTree import tostring
import pandas
import csv
import os

# f = open("jsons/1658438224287_S1_TMM_backup.json")


def clean_word(word):
	word = word.strip()
	word = word.replace(" ", "")
	word = word.replace("\t", "")
	word = word.replace("\n", "")
	word = word.replace(",", "")
	word = word.replace('\"', "")
	return word

def generatecsv(file, type):
	print (file)
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
		try:
			word = clean_word(line)
			if line[0] == "}" or line[0] == "{":
				continue
			if line.isnumeric():
				data["imageTypeQuiz"].append(line)
				continue
			if len(word.split(":")) == 1:
				continue
			# types.append(word.split(":")[0])
			init = word.split(":")[0]
			response = word.split(":")[1]
			data[init].append(response)
		except:
			continue
	# def convert_to_string(list):
	# 	# print (list)
	# 	# word = ""
	# 	# for elem in list:
	# 		# print (elem)
	# 	word = ','.join(list)
	# 	print(word)
	# 	return word

	# fieldnames = []
	# for key in data.keys():
	# 	fieldnames.append(key)

	mturk = data["d_mTurkID"]
	print (mturk)

	with open('results/' + mturk[0] + '_' + type + '.csv', 'w') as f:
		writer = csv.writer(f)
		# writer = csv.DictWriter(f, fieldnames=fieldnames)
		# writing dictionary keys as headings of csv
		# writer.writerow(data.keys())
		# writer.writerow(data.keys())
		# writing list of dictionary
		# for value in data.values():
		# 	writer.writerow(keys + "," + convert_to_string(values))
		writer.writerows(data.values())
		# for key in data.keys():
		# 	row = ""
		# 	# print (key,value)
		# 	row += key + ","
		# 	for value in data.values():
		# 		print (type(row))
		# 		temp = ','.join(str(v) for v in value)
		# 		row += temp
		# 	writer.writerow(row)	# write the row to the csv file
directory = 'jsons'

# iterate over files in
# that directory
for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	# checking if it is a file
	if os.path.isfile(f):
		type = f.split('_')[1]
		print (f)
		generatecsv(f, type)