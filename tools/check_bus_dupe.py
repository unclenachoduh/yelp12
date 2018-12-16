# Used to check that there are no duplicates of businesses in the sorted data
cal = open("Dataset/calgary").read().split("\n")
chm = open("Dataset/champaign").read().split("\n")
cha = open("Dataset/charlotte").read().split("\n")
cle = open("Dataset/cleveland").read().split("\n")
lsv = open("Dataset/lasvegas").read().split("\n")
mad = open("Dataset/madison").read().split("\n")
mon = open("Dataset/montreal").read().split("\n")
phx = open("Dataset/phoenix").read().split("\n")
pit = open("Dataset/pittsburgh").read().split("\n")
tor = open("Dataset/toronto").read().split("\n")

reg = [["cal", cal], ["chm", chm], ["cha", cha], ["cle", cle], ["lsv", lsv], ["mad", mad], ["mon", mon], ["phx", phx], ["pit", pit], ["tor", tor]]

master = {}

for r in reg:
	print(r[0])
	for x in r[1]:
		if x not in master:
			master[x] = 1
		else:
			print("Bad boi", x)