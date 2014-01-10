from sys import argv

script, source, target = argv

source = open(source)
target = open(target)

def compare():
	diff = ""
	result = ""
	i = 0
	j = 0

	for copy in target:
		lineExists 	= False
		source.seek(0)

		for original in source:
			if original.strip() == copy.strip():
				lineExists = True
				break

		if lineExists == False:
			#print "original: ", original
			result += copy
			i+=1

	print result
	#print "number of lines: ", i

compare()