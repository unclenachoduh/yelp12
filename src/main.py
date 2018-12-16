# Run complete system [Currently Draft]

# System packages
import json, sys, operator, os

# Local Packages
import build_model, topic, reprev, repsent, exsum

# Text Generation Packages
# import absum

# External Packages
import nltk

json_file = "yelp_dataset/yelp_academic_dataset_review.json"
# json_file = "output/VUtazCTIc0aoOrQprP_s-Q.json"
# bus_id = "VUtazCTIc0aoOrQprP_s-Q"
# bus_id = sys.argv[1]

businesses = []

if len(sys.argv) == 3:
	if sys.argv[1] == "-b":
		businesses = open(sys.argv[2]).read().split("\n")
elif len(sys.argv) == 2:
	businesses.append(sys.argv[1])
else:
	print("Bad arguments. ")
	raise ValueError("Bad arguments. Should be '[bus_id]' or '-b [bus_file]'")


run_analytics = False

for bus_id in businesses:

	print("\n+----- YELP12 Sytem Running -----+\n|")
	print("|  BID:", bus_id)

	model_data = build_model.build(json_file, bus_id, run_analytics)

	if model_data:

		model_num = 0

		wout = open("output/OUTPUT_" + bus_id, "w+")

		wout.write("YELP12 OUTPUT FOR BUSINESS: " + bus_id + "\n\n")

		topics = []
		sentences = []
		reviews = []
		summaries = []

		i = 0
		for model in model_data:
			model_num += 1
			print("|\n|  > STAR NUMBER:", model_num)

			tw_results = topic.words(model, model_data, i)
			i += 1

			topic_words = " ".join(sorted(tw_results[0]))

			# token_score = itfdf
			token_score = tw_results[1]

			topics.append(topic_words)

			rep_rev = reprev.review(model, token_score)

			reviews.append(rep_rev)

			rep_sent = repsent.sentence(model, token_score)

			sentences.append(rep_sent)

			ext_sum = exsum.summary(model, token_score)

			summaries.append(ext_sum)

			# # ABSTRACTIVE SUMMARY
			# os.mkdir("UncleNachoDuhTempFolder")
			# tout = open("UncleNachoDuhTempFolder/temp", "w+")

			# for sent in model[2]:
			# 	tout.write(sent + "\n")

			# ab_sum = absum.summary(model)

			# os.remove("UncleNachoDuhTempFolder/temp")
			# os.rmdir("UncleNachoDuhTempFolder")

		wout.write("REPRESENTATIVE SENTENCE\n\n")

		star_count = 1
		for sentence in sentences:
			wout.write("STARS: " + str(star_count) + "\n" )
			wout.write(sentence + "\n\n")
			star_count += 1

		wout.write("REPRESENTATIVE REVIEWS\n\n")
		star_count = 1
		for review in reviews:
			wout.write("STARS: " + str(star_count) + "\n" )
			wout.write(review + "\n\n")
			star_count += 1

		wout.write("EXTRACTIVE SUMMARY\n\n")
		star_count = 1
		for summary in summaries:
			wout.write("STARS: " + str(star_count) + "\n" )
			wout.write(summary + "\n\n")
			star_count += 1

		wout.write("TOPIC WORDS\n\n")
		star_count = 1
		for topic_w in topics:
			wout.write("STARS: " + str(star_count) + "\n" )
			wout.write(topic_w + "\n\n")
			star_count += 1
			
	else:
		print("|")
		print("|  X Business not found")
		
	print("|")
	print("|     Thank you for flying")
	print("|  Uncle Nacho, Duh Airlines :)")
	print("|\n+------ YELP12 Sytem Ended ------+\n")