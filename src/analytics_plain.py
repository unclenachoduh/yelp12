import json, sys
#import numpy as np

json_data = open("yelp_dataset/yelp_academic_dataset_review.json")
# json_data = open("fake_data/small_rev.json")

line = json_data.readline()

bus_data = open("yelp_dataset/yelp_academic_dataset_business.json").readlines()

bus = {}

for j in bus_data:
	business = json.loads(j)
	if business["business_id"] not in bus:
		bus[business["business_id"]] = 1

print("WE HERE")

bus_ids = []

bus_data = {}

total_bus = 0
total_rev = 0

total_one = 0
max_one = 0
avg_one = 0

total_two =0
max_two = 0
avg_two = 0

total_three = 0
max_three = 0
avg_three = 0

total_four = 0
max_four = 0
avg_four = 0

total_five = 0
max_five = 0
avg_five = 0


wout = open("yelp12/fakeout/rev_fake", "w+")

while line:
	
	review = json.loads(line)

	if review["business_id"] in bus:

		rid = review["review_id"]
		bid = review["business_id"]
		uid = review["user_id"]
		stars = review["stars"]
		text = review["text"]
		# print(rid)
		# print(bid)
		# print(uid)
		# print(stars)
		# print(text)

		if bid not in bus_data:
			bus_ids.append(bid)
			bus_data[bid] = [0, 0, 0, 0, 0]

			total_bus += 1

		if review["stars"] == 5:
			bus_data[bid][4] += 1
			total_five += 1
		elif review["stars"] == 4:
			bus_data[bid][3] += 1
			total_four += 1
		elif review["stars"] == 3:
			bus_data[bid][2] += 1
			total_three += 1
		elif review["stars"] == 2:
			bus_data[bid][1] += 1
			total_two += 1
		elif review["stars"] == 1:
			bus_data[bid][0] += 1
			total_one += 1
		else:
			print("Error on stars", rid, bid)

		total_rev += 1

	line = json_data.readline()


print("\nTotal rev / Sum Total revs")
print(total_rev, total_one+total_two+total_three+total_four+total_five)

print("\nTotal bus / len bus arr")
print(total_bus, len(bus_ids))
print("")

max_stars = [0, 0, 0, 0, 0]
min_stars = [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize]

rev_by_bus = []


over_50 = []
over_50_count = 0

over_100 = []
over_100_count = 0

over_150 = []
over_150_count = 0

over_200 = []
over_200_count = 0

for bus in bus_ids:


	check_over_50 = 0
	check_over_100 = 0
	check_over_150 = 0
	check_over_200 = 0

	# print(bus)
	star_num = 0
	this_bus_star = 0
	for star in bus_data[bus]:
		# print(star_num+1, star)

		if star > 49:
			check_over_50 += 1
		if star > 99:
			check_over_100 += 1
		if star > 149:
			check_over_150 += 1
		if star > 199:
			check_over_200 += 1

		this_bus_star += star

		if star > max_stars[star_num]:
			max_stars[star_num] = star
		if star < min_stars[star_num]:
			min_stars[star_num] = star
		star_num += 1



	if check_over_50 == 5:
		over_50.append(bus)
		over_50_count += 1
	if check_over_100 == 5:
		over_100.append(bus)
		over_100_count += 1
	if check_over_150 == 5:
		over_150.append(bus)
		over_150_count += 1
	if check_over_200 == 5:
		over_200.append(bus)
		over_200_count += 1

	rev_by_bus.append(this_bus_star)


print("OVER 50", over_50_count)
print("OVER 100", over_100_count)
print("OVER 150", over_150_count)
print("OVER 200", over_200_count)

out50 = open("output/over50", "w+")
out50.write('\n'.join(over_50))

out100 = open("output/over100", "w+")
out100.write('\n'.join(over_100))

out150 = open("output/over150", "w+")
out150.write('\n'.join(over_150))

out200 = open("output/over200", "w+")
out200.write('\n'.join(over_200))

print("")


# print("\nReview per bus")
max_rev_bus = 0
min_rev_bus = sys.maxsize
for rev_count in rev_by_bus:
	# print(rev_count)
	if rev_count > max_rev_bus:
		max_rev_bus = rev_count
	if rev_count < min_rev_bus:
		min_rev_bus = rev_count

print("Avg rev per bus")
print(total_rev/total_bus)

print("Max rev per bus")
print(max_rev_bus)

print("\nMax reviews per star:")
for i in max_stars:
	print(i)

print("\nAvg reviews per star:")
print(1, total_one/total_bus)
print(2, total_two/total_bus)
print(3, total_three/total_bus)
print(4, total_four/total_bus)
print(5, total_five/total_bus)

