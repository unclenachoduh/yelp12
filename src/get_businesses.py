import json, plotly

json_data = open("yelp_dataset/yelp_academic_dataset_business.json").readlines()

minlat = 0
maxlat = 0
minlon = 0
maxlon = 0

wout = open("yelp12/plot_map", "w+")

for j in json_data:
	business = json.loads(j)
	# print(business["business_id"])
	# print(business["latitude"])
	# print(business["longitude"])

	if business["latitude"] != None and business["longitude"] != None:

		lat = float(business["latitude"])
		lon = float(business["longitude"])

		# wout.write(str(lat) + "\t" + str(lon) + "\n")
		wout.write(str(lon) + "\t" + str(lat) + "\n")

		if lat < minlat:
			minlat = lat
		if lat > maxlat:
			maxlat = lat
		if lon < minlon:
			minlon = lon
		if lon > maxlon:
			maxlon = lon


print("MINLAT:", minlat)
print("MAXLAT:", maxlat)
print("MINLONG:", minlon)
print("MAXLONG:", maxlon)

# print(json_data)