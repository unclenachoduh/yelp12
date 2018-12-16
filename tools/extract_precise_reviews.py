import json, sys

json_data = open("yelp_dataset/yelp_academic_dataset_review.json")

line = json_data.readline()

bus_id = "VUtazCTIc0aoOrQprP_s-Q"

wout = open("output/" + bus_id + ".json", "w+")

i = 0
while line:
	if bus_id in line:
		wout.write(line)
	line = json_data.readline()