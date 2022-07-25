# page renamer
import os


def findmturk(file):
	with open(file) as f:
		data = f.readlines()
	# cont = data.reverse()
	print (data)


def clean_word(word):
	word = word.strip()
	word = word.replace(" ", "")
	word = word.replace("\t", "")
	word = word.replace("\n", "")
	word = word.replace(",", "")
	word = word.replace('\"', "")
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

directory = 'jsons'

# iterate over files in
# that directory
for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	# checking if it is a file
	if os.path.isfile(f):
		# findmturk(f)
		image_accuracy(f)