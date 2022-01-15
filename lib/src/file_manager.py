def file(path_to_file):
	with open(path_to_file) as file:
		lines = file.readlines()
		linesW = [line.rstrip() for line in lines]
		return lines