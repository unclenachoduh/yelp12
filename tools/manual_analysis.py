import sys, operator

file = sys.argv[1]

readfrom = open(file).read().split("\n\n")

bus_id = readfrom[0]

text = [readfrom[1], readfrom[2], readfrom[3], readfrom[4],readfrom[5]]

action = "search"

dicts = [{},{},{},{},{}]
bad_dicts = [{},{},{},{},{}]

count = 0
for group in text:
	parts = group.split("----")

	lines = parts[1].split("\n")

	line_count = 0

	sep = "BAD"

	for line in lines:

		if line == ">>":
			sep = "GOOD"
		elif line != "":
			if sep == "GOOD":
				if line not in dicts[count]:
					dicts[count][line] = 1
				else:
					dicts[count][line] += 1
			else:
				if line not in bad_dicts[count]:
					bad_dicts[count][line] = 1
				else:
					bad_dicts[count][line] += 1



		line_count += 1
	count += 1

print(bus_id)

ind = 0

outputs = ["", "", "", "", ""]

for index in dicts:
	# print(ind)

	outputs[ind] += str(ind) + " STAR\n\nGOOD\n----\n"

	sort = sorted(index.items(), key=operator.itemgetter(1), reverse=True)
	total = 0
	for item in sort:
		total += item[1]
	for item in sort:
		# print(item[0], item[1], int(1+((item[1]/total) * 100) ))
		outputs[ind] += item[0] + "\t" +  str(int(1+((item[1]/total) * 100) )) + "\n"

	outputs[ind] += "\nBAD\n----\n"
	sort = sorted(bad_dicts[ind].items(), key=operator.itemgetter(1), reverse=True)
	total = 0
	for item in sort:
		total += item[1]
	for item in sort:
		# print(item[0], item[1], int(1+((item[1]/total) * 100) ))
		outputs[ind] += item[0] + "\t" + str(int(1+((item[1]/total) * 100) )) + "\n"

	ind += 1

wout = open("manual_analysis/" + bus_id + "_topics.txt", "w+")
for o in outputs:
	# print(o)
	wout.write(o + "\n")