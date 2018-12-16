# Used to get the plain review text from a batch of business IDs
import json

businesses = open("output/businesses").read().split("\n")

# k=bus_id v=index
bus_d = {}

count = 0
for b in businesses:
	bus_d[b] = count
	count += 1

json_file = open("yelp_dataset/yelp_academic_dataset_review.json")

one = [[] for x in range(len(businesses))]
two = [[] for x in range(len(businesses))]
three = [[] for x in range(len(businesses))]
four = [[] for x in range(len(businesses))]
five = [[] for x in range(len(businesses))]

line = json_file.readline()

while line:
	review_struct = json.loads(line)

	bid = review_struct["business_id"]
	star = review_struct["stars"]
	text = review_struct["text"]

	if bid in bus_d:

		i = bus_d[bid]

		if star == 1:
			one[i].append(text)
		elif star == 2:
			two[i].append(text)
		elif star == 3:
			three[i].append(text)
		elif star == 4:
			four[i].append(text)
		elif star == 5:
			five[i].append(text)
		else:
			print("Star Problem")
			print(line)

	line = json_file.readline()

count = 0
for b in businesses:
	wout = open("output/PLAIN_TEXT_" + b, "w+")

	wout.write(b)
	wout.write("\n\nONE\n\n")
	wout.write("\n\n".join(one[count]))
	wout.write("\n\nTWO\n\n")
	wout.write("\n\n".join(two[count]))
	wout.write("\n\nTHREE\n\n")
	wout.write("\n\n".join(three[count]))
	wout.write("\n\nFOUR\n\n")
	wout.write("\n\n".join(four[count]))
	wout.write("\n\nFIVE\n\n")
	wout.write("\n\n".join(five[count]))

	count += 1