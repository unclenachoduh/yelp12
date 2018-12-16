import json, sys, operator

import nltk

json_data = open("output/VUtazCTIc0aoOrQprP_s-Q.json")

line = json_data.readline()

bus_id = "VUtazCTIc0aoOrQprP_s-Q"

wout = open("output/analytics_" + bus_id, "w+")

# _count is a count of reviews per star

one_count = 0
two_count = 0
three_count = 0
four_count = 0
five_count = 0

# _revs is a list of rev text by star

one_revs = []
two_revs = []
three_revs = []
four_revs = []
five_revs = []

# _wc is the count of total words in all revs per star. Later used to calc avg words

one_wc = 0
two_wc = 0
three_wc = 0
four_wc = 0
five_wc = 0

# _words is a list of unique words by star
# _wd is a dictionary of words by star where k=w, v=[count, doc freq]

one_words = []
one_wd = {}
two_words = []
two_wd = {}
three_words = []
three_wd = {}
four_words = []
four_wd = {}
five_words = []
five_wd = {}

one_unq_sents = []

one_unq = []

i = 0
while line:
	review_struct = json.loads(line)

	rid = review_struct["review_id"]
	text = review_struct["text"].lower()
	star = review_struct["stars"]

	tokens = nltk.word_tokenize(text)

	sentences = nltk.sent_tokenize(text)

	if star == 1:
		one_count += 1
		one_revs.append(text)
		one_wc += len(tokens)

		local_words = []
		local_dict = {}

		for token in tokens:
			if token.isupper() or token.islower():
				if token not in one_wd:
					one_words.append(token)
					one_wd[token] = [1, 0]
				else:
					borrowed_list = one_wd[token]
					borrowed_list[0] += 1
					one_wd[token] = borrowed_list

				if token not in local_dict:
					local_words.append(token)
					local_dict[token] = 1


		for word in local_words:
			borrowed_list = one_wd[word]
			borrowed_list[1] += 1
			one_wd[word] = borrowed_list

		
		one_unq.append([text, local_words])



		for sent in sentences:
			sent_tokens = nltk.word_tokenize(sent)
			unq_sent_tokens = []
			for s in sent_tokens:
				if s not in unq_sent_tokens:
					unq_sent_tokens.append(s)

			one_unq_sents.append([sent, unq_sent_tokens])

	elif star == 2:
		two_count += 1
		two_revs.append(text)
		two_wc += len(tokens)
	elif star == 3:
		three_count += 1
		three_revs.append(text)
		three_wc += len(tokens)
	elif star == 4:
		four_count += 1
		four_revs.append(text)
		four_wc += len(tokens)
	elif star == 5:
		five_count += 1
		five_revs.append(text)
		five_wc += len(tokens)

		local_words = []
		local_dict = {}

		for token in tokens:
			if token.isupper() or token.islower():
				if token not in five_wd:
					five_words.append(token)
					five_wd[token] = [1, 0]
				else:
					borrowed_list = five_wd[token]
					borrowed_list[0] += 1
					five_wd[token] = borrowed_list

				if token not in local_dict:
					local_words.append(token)
					local_dict[token] = 1


		for word in local_words:
			borrowed_list = five_wd[word]
			borrowed_list[1] += 1
			five_wd[word] = borrowed_list

	#############################
	# ### REVIEW DATA
	# print("=====")
	# print(rid, star)
	# print(text)
	# print(tokens)
	# print(len(tokens))
	# for sentence in sentences:
	# 	print("::", sentence)
	##############################

	line = json_data.readline()


# print("ONE TOPIC WORDS")
one_tfid = {}

for w in one_words:
	# print(w, one_wd[w])

	# tfdf = (one_wd[w][0]) * (one_wd[w][1])

	# one_tfid[w] = tfdf * (1 / one_wd[w][1])

	gen_score = (1 / one_wd[w][0]) * (one_wd[w][1])

	one_tfid[w] = gen_score

# one_scores = sorted(one_tfid.items(), key=operator.itemgetter(1), reverse=False)

# cc = 0
# for score in one_scores:
# 	if score[1] != 1.0:
# 		print(score)
# 	cc += 1
	# if cc > 50:
	# 	break

# Set length of generated summary to 1.25 of average 
one_sum_length = (one_wc/one_count) * 1.25

print("")
print("REPRESENTATIVE SUMMARY")

rep_rev_dict = {}

for oner in one_unq:
	rep_rev_score = 0
	for w in oner[1]:
		rep_rev_score += one_tfid[w]

	if len(oner[1]) < (one_wc/one_count):

		rep_rev_dict[oner[0]] = rep_rev_score


rep_rev_results = sorted(rep_rev_dict.items(), key=operator.itemgetter(1), reverse=True)

# ccc = 0
# for x in rep_rev_results:
# 	print(x)
# 	ccc += 1
# 	if ccc > 10:
# 		break

print(rep_rev_results[0][0])

print("")

print("EXTRACTIVE SUMMARY")

ext_sum_dict = {}

for ones in one_unq_sents:
	ext_sum_score = 0
	for w in ones[1]:
		if w in one_tfid:
			ext_sum_score += one_tfid[w]

	if len(ones[1]) < (one_wc/one_count):

		ext_sum_dict[ones[0]] = ext_sum_score


ext_sum_results = sorted(ext_sum_dict.items(), key=operator.itemgetter(1), reverse=True)

ext_sum_len = 0
ext_sum_arr = []

for s in ext_sum_results:
	tokes = nltk.word_tokenize(s[0])

	if ext_sum_len + len(tokes) < one_sum_length:
		ext_sum_arr.append(s[0])
		ext_sum_len += len(tokes)

ext_sum = "\n".join(ext_sum_arr)

print(ext_sum)

# print("FIVE TOPIC WORDS")
# five_tfid = {}

# for w in five_words:
# 	# print(w, one_wd[w])

# 	# tfdf = (one_wd[w][0]) * (one_wd[w][1])

# 	# one_tfid[w] = tfdf * (1 / one_wd[w][1])

# 	five_tfid[w] = (1 / five_wd[w][0]) * (five_wd[w][1])

# five_scores = sorted(five_tfid.items(), key=operator.itemgetter(1), reverse=True)

# cc = 0
# for score in five_scores:
# 	print(score)
# 	cc += 1
# 	if cc > 50:
# 		break


#####################################
### ANALYTICS

# print("STAR COUNTS:")

# print(one_count, two_count, three_count, four_count, five_count)

# all_count = one_count + two_count + three_count + four_count + five_count

# print("AVERAGE LENGTH:")
# print(one_wc/one_count, two_wc/two_count, three_wc/three_count, four_wc/four_count, five_wc/five_count)

# all_wc = one_wc + two_wc + three_wc + four_wc + five_wc

# print(all_wc/all_count)

### ANALYTICS
#####################################

# one_count
# two_count
# three_count
# four_count
# five_count

# one_revs
# two_revs
# three_revs
# four_revs
# five_revs

# one_wc
# two_wc
# three_wc
# four_wc
# five_wc