import json, sys
import numpy as np

json_data = open("small_rev.json").readlines()

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


wout = open("fakeout/rev_fake", "w+")

for j in json_data:
	review = json.loads(j)

	rid = review["review_id"]
	bid = review["business_id"]
	uid = review["user_id"]
	stars = review["stars"]
	text = review["text"]
	print(rid)
	print(bid)
	print(uid)
	print(stars)
	print(text)

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
		print("Error on stars")

	total_rev += 1

print("\nTotal rev / Sum Total revs")

print(total_rev, total_one+total_two+total_three+total_four+total_five)


print("\nTotal bus / len bus arr")

print(total_bus, len(bus_ids))

print("")

max_stars = [0, 0, 0, 0, 0]
min_stars = [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize]

rev_by_bus = []


print("stars by bus")
for bus in bus_ids:
	print(bus)
	star_num = 0
	this_bus_star = 0
	for star in bus_data[bus]:
		print(star_num+1, star)

		this_bus_star += star

		if star > max_stars[star_num]:
			max_stars[star_num] = star
		if star < min_stars[star_num]:
			min_stars[star_num] = star
		star_num += 1

	rev_by_bus.append(this_bus_star)


print("\nReview per bus")
max_rev_bus = 0
min_rev_bus = sys.maxsize
for rev_count in rev_by_bus:
	print(rev_count)
	if rev_count > max_rev_bus:
		max_rev_bus = rev_count
	if rev_count < min_rev_bus:
		min_rev_bus = rev_count

print("Avg rev per bus")
print(total_rev/total_bus)

print("Max rev per bus")
print(max_rev_bus)

print("Min rev per bus")
print(min_rev_bus)

print("\nTotal reviews per Star:")
print(1, total_one)
print(2, total_two)
print(3, total_three)
print(4, total_four)
print(5, total_five)

print("\nMax reviews per star:")
for i in max_stars:
	print(i)

print("\nMin reviews per star:")
for i in min_stars:
	print(i)


print("\nAvg reviews per star:")
print(1, total_one/total_bus)
print(2, total_two/total_bus)
print(3, total_three/total_bus)
print(4, total_four/total_bus)
print(5, total_five/total_bus)