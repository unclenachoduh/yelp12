import sys, os, json, operator

from random import shuffle

import nltk


# Stop words from Yoast SEO https://github.com/Yoast/YoastSEO.js/blob/develop/src/config/stopwords.js
stopwords_source = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]
nltk_stopwords = {}

for word in stopwords_source:
	tokens = nltk.word_tokenize(word)
	for token in tokens:
		nltk_stopwords[token] = 1

# json_file = "yelp_dataset/yelp_academic_dataset_review.json"
json_file = "output/VUtazCTIc0aoOrQprP_s-Q.json"

files = []

if len(sys.argv) == 3:
	if sys.argv[1] == "-b":
		files = open(sys.argv[2]).read().split("\n")
elif len(sys.argv) == 2:
	files.append(sys.argv[1])
else:
	print("Bad arguments. ")
	raise ValueError("Bad arguments. Should be '[file]' or '-b [file]'")

def getgrams(text):
	tokens = nltk.word_tokenize(text)

	one = []
	two = []
	three = []

	count = 1
	prev1 = ""
	prev2 = ""
	for token in tokens:
		passing = 0

		onecheck = False
		if token.islower() or token.isupper():
			if token not in nltk_stopwords:
				onecheck = True

		twocheck = False
		if prev1.islower() or prev1.isupper():
			if prev1 not in nltk_stopwords:
				twocheck = True

		threecheck = False
		if prev2.islower() or prev2.isupper():
			if prev2 not in nltk_stopwords:
				threecheck = True


		if onecheck == True:
			one.append(token)
		if count - 1 > 0 and onecheck == True and twocheck == True:
			two.append(prev1 + "_" + token)
		if count - 2 > 0 and onecheck == True and twocheck == True and threecheck == True:
			three.append(prev2 + "_" + prev1 + "_" + token)
		count += 1

		prev2 = prev1
		prev1 = token

	return[one, two, three]


# Returns a score for the summary
# The score represents the coverage of grams that make up the reviews
def redscore(summary, source):

	onelen = len(source[0])
	twolen = len(source[1])
	threelen = len(source[2])

	already = {}

	count = 0
	
	yes = [0,0,0]
	for grams in summary:
		for gram in grams:
			if gram in source[count]:
				if gram not in already:
					yes[count] += 1
					already[gram] = 1

		count += 1

	score = yes[0]/onelen + yes[1]/twolen + yes[2]/threelen

	return score


# Generates a summary using sentences at random from the set from the star rating
# Returns a list with ngrams inteh same fashion as the the extractive summary
def rand_sum(plain_lines, rev_len):
	rand_tokes = [
		[[],[],[]],
		[[],[],[]],
		[[],[],[]],
		[[],[],[]],
		[[],[],[]]]

	text = ""
	rand_count = 0
	for index in plain_lines:
		rand_len = 0
		text += str(rand_count + 1) + " STAR SUMMARY\n\n"
		shuffle(index)
		i = 0
		while rand_len < rev_len[rand_count] - 10:
			tokens = nltk.word_tokenize(index[i])
			if rand_len + len(tokens) < rev_len[rand_count] + 20:
				rand_len += len(tokens)

				text += index[i] + "\n\n"
				count = 0

				r_count = 0
				results = getgrams(index[i])
				for gram_num in results:
					for gram in gram_num:
						rand_tokes[rand_count][r_count].append(gram)
					r_count += 1

			i += 1

			if i == len(index):
				break

		rand_count +=1
	
		# print(text)
	return [rand_tokes, text]

wout = open("rando_analysis_out.txt", "w+")

average = 0
extractive = 0

avg_avg = []
ext_avg = []

for file in files:
	if file != "":

		bus_id = ""

		gen_text = open(file).read().split("\n")

		ind = -1

		ext_rev = []

		rev_len = [0,0,0,0,0]

		id_check = False
		sum_check = False
		for line in gen_text:
			if line != "":

				if "YELP12 OUTPUT FOR BUSINESS:" in line:
					parts = line.split(": ")
					bus_id = parts[1]
					id_check = True
				elif line == "EXTRACTIVE SUMMARY":
					sum_check = True
				elif "STARS: " in line and sum_check == True:
					ind +=1
					ext_rev.append([[],[],[]])
				elif line == "TOPIC WORDS":
					ind == -1
					sum_check = False
				elif ind > -1 and sum_check == True:
					count = 0
					tokes = nltk.word_tokenize(line)
					rev_len[ind] += len(tokes)

					results = getgrams(line)
					for gram_num in results:
						for gram in gram_num:
							ext_rev[ind][count].append(gram)
						count += 1

		print(rev_len)

		if id_check == False:
			raise ValueError("No Business ID found")
		else:

			print(bus_id)
			wout.write(bus_id)

			json_data = open(json_file)
			line = json_data.readline()

			bus_exists = False

			onestar = [{},{},{}]
			twostar = [{},{},{}]
			threestar = [{},{},{}]
			fourstar = [{},{},{}]
			fivestar = [{},{},{}]

			master = [onestar, twostar, threestar, fourstar, fivestar]

			plain_lines = [[],[],[],[],[]]

			while line:
				review_struct = json.loads(line)
				bid = review_struct["business_id"]

				if bid == bus_id:

					bus_exists = True

					rev_text = review_struct["text"].lower()
					star = review_struct["stars"]

					if star == 1:
						results = getgrams(rev_text)
						count = 0
						for gram_num in results:
							for gram in gram_num:
								if gram not in onestar[count]:
									onestar[count][gram] = 1
								else:
									onestar[count][gram] += 1
							count += 1

						these_lines = nltk.sent_tokenize(rev_text)
						for this_line in these_lines:
							plain_lines[0].append(this_line)

					elif star == 2:
						results = getgrams(rev_text)
						count = 0
						for gram_num in results:
							for gram in gram_num:
								if gram not in twostar[count]:
									twostar[count][gram] = 1
								else:
									twostar[count][gram] += 1
							count += 1

						these_lines = nltk.sent_tokenize(rev_text)
						for this_line in these_lines:
							plain_lines[1].append(this_line)
					elif star == 3:
						results = getgrams(rev_text)
						count = 0
						for gram_num in results:
							for gram in gram_num:
								if gram not in threestar[count]:
									threestar[count][gram] = 1
								else:
									threestar[count][gram] += 1
							count += 1

						these_lines = nltk.sent_tokenize(rev_text)
						for this_line in these_lines:
							plain_lines[2].append(this_line)
					elif star == 4:
						results = getgrams(rev_text)
						count = 0
						for gram_num in results:
							for gram in gram_num:
								if gram not in fourstar[count]:
									fourstar[count][gram] = 1
								else:
									fourstar[count][gram] += 1
							count += 1

						these_lines = nltk.sent_tokenize(rev_text)
						for this_line in these_lines:
							plain_lines[3].append(this_line)
					elif star == 5:
						results = getgrams(rev_text)
						count = 0
						for gram_num in results:
							for gram in gram_num:
								if gram not in fivestar[count]:
									fivestar[count][gram] = 1
								else:
									fivestar[count][gram] += 1
							count += 1

						these_lines = nltk.sent_tokenize(rev_text)
						for this_line in these_lines:
							plain_lines[4].append(this_line)
					else:
						print("Star Problem")
						print(line)

				line = json_data.readline()

			my_scores = [0,0,0,0,0]
			master_count = 0
			for needscore in ext_rev:
				my_scores[master_count] = redscore(needscore, master[master_count])
				master_count += 1

			random_first = [
				rand_sum(plain_lines, rev_len), 
				rand_sum(plain_lines, rev_len), 
				rand_sum(plain_lines, rev_len), 
				rand_sum(plain_lines, rev_len), 
				rand_sum(plain_lines, rev_len), 
				rand_sum(plain_lines, rev_len), 
				rand_sum(plain_lines, rev_len), 
				rand_sum(plain_lines, rev_len), 
				rand_sum(plain_lines, rev_len), 
				rand_sum(plain_lines, rev_len)]

			random_batch = [
				random_first[0][0],
				random_first[1][0],
				random_first[2][0],
				random_first[3][0],
				random_first[4][0],
				random_first[5][0],
				random_first[6][0],
				random_first[7][0],
				random_first[8][0],
				random_first[9][0]]

			rand_batch_scores = [0,0,0,0,0]

			rand_batch_count = 0
			for batch in random_batch:
				star_count = 0
				for needscore in batch:
					rand_batch_scores[star_count] += redscore(needscore, master[star_count])
					star_count += 1

			print_count = 0
			for score in rand_batch_scores:

				extractive_score = my_scores[print_count]
				random_score = score/10

				ext_avg.append(extractive_score)
				avg_avg.append(random_score)

				if extractive_score > random_score:
					extractive += 1
				else:
					average += 1
				
				print("EXT_SUM:" + str(extractive_score))
				print("RANDOM: " + str(random_score))
				print_count += 1
				print()

				wout.write("\n\nSTARS: " + str(print_count))
				wout.write("\nEXT SUM: " + str(extractive_score))
				wout.write("\nRANDOM:  " + str(random_score))

			print("AVGERAGE:")
			print("EXT SUM: " + str(sum(my_scores)/len(my_scores)))
			print("RANDOM:  " + str((sum(rand_batch_scores)/len(rand_batch_scores)/10) ))

			wout.write("\n\nAVGERAGE:")
			wout.write("\nEXT SUM: " + str(sum(my_scores)/len(my_scores)))
			wout.write("\nRANDOM:  " + str((sum(rand_batch_scores)/len(rand_batch_scores)/10) ))
			wout.write("\n\n")


wout.write("\n\n----\nEXTRACTIVE WINS:" + str(extractive) + " / " + str(extractive + average) )
wout.write("\n\nAVERAGES:")
wout.write("\nEXTRACTIVE: " + str(sum(ext_avg)/len(ext_avg)))
wout.write("\nRANDOM:     " + str( (sum(avg_avg)/ (len(avg_avg)) ) ) )


random_text = random_first[0][1] + \
	random_first[1][1] + \
	random_first[2][1] + \
	random_first[3][1] + \
	random_first[4][1] + \
	random_first[5][1] + \
	random_first[6][1] + \
	random_first[7][1] + \
	random_first[8][1] + \
	random_first[9][1]
output_file = open("random_sums.txt", "w+")
output_file.write(random_text)