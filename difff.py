from sys import argv

script, source, target = argv

source = open(source)
target = open(target)

def compare():
	diff = ""
	i = 0
	j = 0

	for copy in target:
		lineExists = False
		source.seek(0)

		for original in source:
			if original.strip() == copy.strip():
				lineExists = True
				break

		if lineExists == False:
			#print "original: ", original
			diff += copy
			i+=1

	print diff
	#print "number of lines: ", i

compare()
