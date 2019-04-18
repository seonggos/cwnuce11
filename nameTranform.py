import os, re

def transform_fileName(path, grade=1, img_num=1):
	file_list = os.listdir(path)

	for file_name in file_list:
		if re.match(r".학년$", file_name):
			grade = int(file_name.split("학년")[0])
			img_num = 1

		file_name = os.path.join(path, file_name)

		if os.path.isdir(file_name):
			img_num = transform_fileName(file_name, grade, img_num)

		fileExtension = file_name.split("/")

		if re.match(r"^img", fileExtension[-1]):
			os.rename(file_name, "test/" + str(grade) + "_" + str(img_num))
			img_num = img_num + 1

	return img_num

def main():
	if not os.path.exists("./test"):
		os.mkdir("./test")

	else:
		print("Directory already exists")
		exit(0)

	transform_fileName("./")
	print("Transform completed")

main()
