# Returns a an extractive summary from the data based on the CLASSY model
import operator

def calc_scores(model, weight, remaining_space, short, black_list):
	sum_dict = {}

	for sent in model[2]:
		sent_score = 0
		for t in model[3][sent]:
			if t not in black_list and t in weight:
				sent_score += weight[t]

		if len(model[3][sent]) < remaining_space and len(model[3][sent])  > 5:

			sum_dict[sent] = sent_score

			if len(model[3][sent]) < short:
				short = len(model[3][sent])


	results = sorted(sum_dict.items(), key=operator.itemgetter(1), reverse=True)

	return [results[0][0], short] 

def summary(model, weight):

	max_len = 50

	remaining_space = max_len

	smallest = remaining_space - 1

	sum_len = 0
	sum_sents = []

	black_list = {}

	while remaining_space > smallest:

		results = calc_scores(model, weight, remaining_space, smallest, black_list)

		sum_sents.append(results[0])
		remaining_space -= len(model[3][results[0]])

		for x in model[3][results[0]]:
			black_list[x] = 1

		smallest = results[1]


	ext_sum = "\n\n".join(sum_sents)

	return ext_sum