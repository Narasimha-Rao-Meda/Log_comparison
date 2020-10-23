import re

file1_path = input("Enter Your file1 path:\n")
file2_path = input("Enter Youe file2 path:\n")

file1_path = file1_path.replace('\\','\\\\')
file2_path = file2_path.replace('\\','\\\\')

try:
	file1_obj = open(file1_path,'r')
	file2_obj = open(file2_path,'r')
	file1_data = file1_obj.read().splitlines()
	file2_data = file2_obj.read().splitlines()
except:
	print("File path is wrong")
else:
	file1_obj.close()
	file2_obj.close()


text1_data = []
text2_data = []
original1_data = []
original2_data = []

for i in file1_data:
	txt = re.sub('^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6} +[a-zA-Z]+[_]+[0-9]{1,12} +[a-zA-Z]+[_]+[0-9]{1,12} ','',i)
	text1_data.append(txt)
	original1_data.append(i)
for i in file2_data:
	txt = re.sub('^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6} +[a-zA-Z]+[_]+[0-9]{1,12} +[a-zA-Z]+[_]+[0-9]{1,12} ','',i)
	text2_data.append(txt)
	original2_data.append(i)

compare_data = []

for line in text1_data:
	if line not in text2_data:
		compare_data.append(line)

for line in text2_data:
	if line not in text1_data:
		compare_data.append(line)


result = []

for i in compare_data:
	for val in original1_data:
		if re.search(i,val):
			if val in result:
				pass
			else:
				result.append(val)


for i in compare_data:
	for val in original2_data:
		if re.search(i,val):
			if val in result:
				pass
			else:
				result.append(val)


for i in result:
	print(i)
