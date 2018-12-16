# Reads source JSON file and returns models

# System packages
import json, sys, operator

# External Packages
import nltk

# Master holds all values that will be returned to the main system
# It is a list with 5 indeces, one for each star
# each star has 7 indeces:
# 0: LIST of TOKENS
# 1: DICTIONARY k=TOKENS, v=[token frequency, document frequency]
# 2: LIST of SENTENCES
# 3: DICTIONARY k=SENTENCE, v=tokens
# 4: LIST of REVIEWS
# 5: DICTIONARY k=REVIEWS, v=tokens
# 6: COUNT of REVIEWS (aka documents)
# 7: COUNT of SENTENCES
# 8: COUNT of TOKENS

def get_deets(raw_ind, text, useful, master2):

	# base value for TF. May be weighted by useful
	add_value = 1

	# # weighting add_value with review useful score. 
	# # Useful minscore = 0
	add_value = add_value / ((useful*.25) + 1)

	i = raw_ind - 1
	
	sentences = nltk.sent_tokenize(text)
	
	# All unique tokens found in this document (review)
	doc_tokens = []
	# Dictionary of unique tokens in this doc for quick search
	doc_dict = {}

	for sentence in sentences:
		tokens = nltk.word_tokenize(sentence)

		# a list of unique tokens in this sentence
		sent_tokens = []

		for token in tokens:
			if token.isupper() or token.islower():
				if token not in master2[i][1]:
					master2[i][0].append(token)
					master2[i][1][token] = [add_value, 0]
				else:
					borrowed_list = master2[i][1][token]
					borrowed_list[0] += add_value
					master2[i][1][token] = borrowed_list

				if token not in doc_dict:
					doc_tokens.append(token)
					doc_dict[token] = 1

				if token not in sent_tokens:
					sent_tokens.append(token)

			master2[i][8] += 1

		master2[i][2].append(sentence)
		master2[i][3][sentence] = sent_tokens

		master2[i][7] += 1

	for token in doc_tokens:
		borrowed_list = master2[i][1][token]
		borrowed_list[1] += 1
		master2[i][1][token] = borrowed_list

	# count of reviews
	master2[i][6] += 1
	# list of reviews
	master2[i][4].append(text)
	# dictionary of reviews
	master2[i][5][text] = doc_tokens

	return master2


def analytics(business_id, master):
	wout = open("output/analytics_" + business_id, "w+")

	all_tc = master[0][8] + master[1][8] + master[2][8] + master[3][8] + master[4][8]
	all_sc = master[0][7] + master[1][7] + master[2][7] + master[3][7] + master[4][7]
	all_rc = master[0][6] + master[1][6] + master[2][6] + master[3][6] + master[4][6]

	wout.write("ANALYTICS FOR BUSINESS: " + business_id + "\n\n")

	wout.write("STAR COUNTS:\n")
	count = 1
	for m in master:
		wout.write(str(count) + " Star: " + str(m[6]) + "\n")
		count += 1

	wout.write("AVG: " + str(all_rc/5) + "\n")

	wout.write("\nAVERAGE REVIEW LENGTH:\n")
	count = 1
	for m in master:
		wout.write(str(count) + " Star: " + str(m[8]/m[6]) + "\n")
		count += 1

	wout.write("AVG: " + str(all_tc/all_rc) + "\n")

	wout.write("\nAVERAGE REVIEW LENGTH:\n")
	count = 1
	for m in master:
		wout.write(str(count) + " Star: " + str(m[8]/m[7]) + "\n")
		count += 1

	wout.write("AVG: " + str(all_tc/all_sc))


def build(filename, business_id, run_an):

	master = [
	[[], {}, [], {}, [], {}, 0, 0, 0], 
	[[], {}, [], {}, [], {}, 0, 0, 0], 
	[[], {}, [], {}, [], {}, 0, 0, 0], 
	[[], {}, [], {}, [], {}, 0, 0, 0], 
	[[], {}, [], {}, [], {}, 0, 0, 0]]

	json_data = open(filename)

	bus_id = business_id

	line = json_data.readline()

	print("|\n|  > BUILD_MODEL.build()")

	bus_exists = False

	while line:

		review_struct = json.loads(line)

		rid = review_struct["review_id"]
		bid = review_struct["business_id"]

		if bid == bus_id:

			bus_exists = True

			rev_text = review_struct["text"].lower()
			star = review_struct["stars"]
			useful = review_struct["useful"]

			if star == 1:
				master = get_deets(1, rev_text, useful, master)
			elif star == 2:
				master = get_deets(2, rev_text, useful, master)
			elif star == 3:
				master = get_deets(3, rev_text, useful, master)
			elif star == 4:
				master = get_deets(4, rev_text, useful, master)
			elif star == 5:
				master = get_deets(5, rev_text, useful, master)
			else:
				print("Star Problem")
				print(line)

		line = json_data.readline()

	if run_an == True:
		analytics(bus_id, master)

	if bus_exists == True:
		return master
	else:
		return False