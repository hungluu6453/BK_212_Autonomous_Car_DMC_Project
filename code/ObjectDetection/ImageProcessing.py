import os

# Index initialization
count_stop = 1
count_30 = 1
count_60 = 1

# old path
path_image = "D:/Download/Traffic Sign/Dataset4/TrafficSignLocalizationandDetection/train/images/"
label_path = "D:/Download/Traffic Sign/Dataset4/TrafficSignLocalizationandDetection/train/labels/"

# new path
path_stop = "D:/Download/Data/Stop/"
path_30 = "D:/Download/Data/Speed30/"
path_60 = "D:/Download/Data/Speed60/"


# class code
code_stop = 31
code_30 = 26
code_60 = 28


# move and rename function

def move_rename(class_code, cur_name):
	global count_stop
	global count_30
	global count_60
	if class_code == code_stop:
		os.rename(path_image+cur_name+".jpg", path_stop + "stop_" + str(count_stop) + ".jpg")
		os.rename(label_path+cur_name+".txt", path_stop + "stop_" + str(count_stop) + ".txt")
		count_stop = count_stop + 1
	elif class_code == code_30:
		os.rename(path_image+cur_name+".jpg", path_30 + "speed30_" + str(count_30) + ".jpg")
		os.rename(label_path+cur_name+".txt", path_30 + "speed30_" + str(count_30) + ".txt")
		count_30 = count_30 + 1
	elif class_code == code_60:
		os.rename(path_image+cur_name+".jpg", path_60 + "speed60_" +str(count_60) + ".jpg")
		os.rename(label_path+cur_name+".txt", path_60 + "speed60_" +str(count_60) + ".txt")
		count_60 = count_60 + 1

def get_code(file_path):
	with open(file_path, 'r') as f:
		code_list = []
		while True:
			line = f.readline()
			if not line:
				break
			else:
				code = line.split(" ")[0]
				code_list += [int(code)]

		if code_30 in code_list:
			code = code_30
		elif code_60 in code_list:
			code = code_60
		elif code_stop in code_list:
			code = code_stop
		else:
			code = -1

		return code

def rename_code(code_read, code_write, file):
	with open(file, 'r') as f:
		lines = f.readlines()
	with open(file, 'w') as f:
		for line in lines:
			if line[:2] == str(code_read):
				f.write(str(code_write) + line[2::])
# open txt file
def seperate_file():
	for file in os.listdir():
		code = get_code(file)
		if code != -1:
			move_rename(code, file[:len(file)-4])

if __name__ == "__main__":
	#seperate file
	os.chdir(label_path)
	seperate_file()
	# rename stop sign
	os.chdir(path_stop)
	for file in os.listdir():
		if file.endswith(".txt"):
			rename_code(code_stop,0,file)
	# rename 30 sign
	os.chdir(path_30)
	for file in os.listdir():
		if file.endswith(".txt"):
			rename_code(code_30,1,file)
	# rename 60 sign
	os.chdir(path_60)
	for file in os.listdir():
		if file.endswith(".txt"):
			rename_code(code_60,2,file)
			