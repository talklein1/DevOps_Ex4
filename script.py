#! python
import sys

f = open("print.txt", "r")
if f.mode == 'r':
	sys.stdout.write("print.txt Opened\n")
	num_lines = sum(1 for line in f)
	if num_lines == 0:
		sys.stdout.write("File is Empty")	
	else:
		f.seek(0)
		counter = 1
		for line in f:
			sys.stdout.write("Line " + str(counter) + ":  " + line)
			counter = counter +1
else:
	sys.stdout.write("Text File is not in reading mode\n")