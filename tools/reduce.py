# Used to create a json file with only the reviews from business that have 50+ reviews per star
import json, sys

json_data = open("yelp_dataset/yelp_academic_dataset_review.json")

line = json_data.readline()

bus_data = open("output/over50").read().split('\n')

wout = open("output/long_data.json", "w+")

i = 0
while line:
	for bus in bus_data:
		if bus in line:
			wout.write(line)
	line = json_data.readline()

	if i == 10:
		print(10)
	if i == 1000:
		print(1000)
	if i == 10000:
		print(10000)
	if i == 100000:
		print(100000)
	if i == 1000000:
		print(1)
	if i == 2000000:
		print(2)
	if i == 3000000:
		print(3)
	if i == 4000000:
		print(4)
	if i == 5000000:
		print(5)
	i += 1