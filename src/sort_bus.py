# Used to sort business IDs by region
import sys, json

calgary = [50.5, 51.5, -114.5, -113.7]
champaign = [39.5, 40.5, -88.6, -87.1]
charlotte = [34.5, 36, -81.5, -80]
cleveland = [41, 42, -82.5, -80]
lasvegas = [35.5, 36.5, -115.5, -114.5]
madison = [42.8, 43.3, -90, -89]
montreal = [44.8, 46.5, -74.5, 73]
pittsburgh = [40, 41, -80.5, 79.5]
phoenix = [33, 34, -114.5, -111]
toronto = [43, 44.5, -80, -78.5]

regions = [calgary, champaign, charlotte, cleveland, lasvegas, madison, montreal, pittsburgh, phoenix, toronto]

json_data = open("yelp_dataset/yelp_academic_dataset_business.json").readlines()

reg_bus_count = [0,0,0,0,0,0,0,0,0,0]

bus_reg = [[],[],[],[],[],[],[],[],[],[]]

business_count = 0
for j in json_data:
	business = json.loads(j)

	if business["latitude"] != None and business["longitude"] != None:

		lat = float(business["latitude"])
		lon = float(business["longitude"])

		region_count = 0
		this_count = 0
		assign_to = -1
		for region in regions:
			if lat > region[0] and lat < region[1]:
				if lon > region[2] and lon < region[3]:
					assign_to = region_count
					reg_bus_count[region_count] += 1
					this_count += 1
			region_count += 1

		if this_count > 1:
			print("Business found in two regions: ", business["business_id"])
		else: 
			bus_reg[assign_to].append(business["business_id"])

	business_count += 1

print(reg_bus_count)
print(business_count)


names = ["calgary", "champaign", "charlotte", "cleveland", "lasvegas", "madison", "montreal", "pittsburgh", "phoenix", "toronto"]

write_count = 0
for name in names:
	wout = open("Dataset/" + name, "w+")
	wout.write('\n'.join(bus_reg[write_count]))
	write_count += 1