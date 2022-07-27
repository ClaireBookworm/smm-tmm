# processsing . py 
import os 
import csv

# helper functions 
def clean_word(word):
	word = word.strip()
	word = word.replace(" ", "")
	word = word.replace("\t", "")
	word = word.replace("\n", "")
	word = word.replace(",", "")
	word = word.replace('\"', "")
	return word

def file_scanner(dir):
	directory = dir

	# iterate over files in
	# that directory
	for filename in os.listdir(directory):
		f = os.path.join(directory, filename)
		# checking if it is a file
		if os.path.isfile(f):
			exptype = f.split('_')[1]
			# do things 

def generate_csv(dict, type):

	with open('results/' + dict["d_mTurkID"][0] + '_' + type + '.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerows(dict.values())


def generate_dict(file, type):
		# print (file)
	f = open(file)
	
	data = {
		"round": [],
		"type": [],
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
		"imageTypeCorrect":[],
		"imageTypeWrong":[],
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

	# for key in data.keys():
	# 	if key = ""

	# fieldnames = []
	# for key in data.keys():
	# 	fieldnames.append(key)

	mturk = data["d_mTurkID"]
	# print (mturk)
	# analysis(data)

