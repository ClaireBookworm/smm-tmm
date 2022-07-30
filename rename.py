# page renamer
import os


def findmturk(file, et):
	data = ""
	with open(file) as f:
		try:
			data = f.readlines()
			# cont = data.reverse()
		except:
			print("error")
	# print (data)
	
	unclean = ",".join(data).split(",")[-1]
	exptype = ""
	thing = ""
	# print (unclean)
	for elem in ",".join(data).split(",")[1:2]:
		thing = (clean_word(elem).split(":")[1])
		print (thing)
	if thing == "Round2":
		exptype = "F2"
	elif thing == "Spatial":
		exptype = "S1"
	elif thing == "Temporal" or thing == "Test":
		exptype = "T1"
	elif thing == "FullInstruction" or thing == "Full Instruction":
		exptype == "F1"
	elif thing == "Identity":
		exptype == "I1"
	try: 
		os.rename(file,unclean.split('"')[3] + "_" + et + ".txt")
	except:
		print("empty")

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

def image_accuracy(file):
	response = []
	quiz = False
	for line in file: 
		if quiz:
			response.append(clean_word(line))
			continue
		if len(response) == 3:
			break
		word = clean_word(line)
		if word[0] == "}" or word[0] == "{":
			continue
		if "imageTypeQuiz" in word:
			quiz = True
	print(response)
	# if response[0] < 40:
	# 	return False
	return True

directory = 'rawnew'

# iterate over files in
# that directory
for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	# checking if it is a file
	if os.path.isfile(f):
		exptype = f.split('_')[1]
		# findmturk(f)
		findmturk(f, exptype)