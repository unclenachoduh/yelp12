# Returns a list of topic words based on itfdf score

import operator

def out_data(all_model, ind):

	giant_model = {}
	inds = []

	if ind == 0:
		inds = [1,2,3,4]
	elif ind == 1:
		inds = [0,2,3,4]
	elif ind == 2:
		inds = [0,1,3,4]
	elif ind == 3:
		inds == [0,1,2,4]
	elif ind == 4:
		inds == [0,1,2,3]

	for index in inds:
		for token in all_model[index][0]:
			if token not in giant_model:
				giant_model[token] = all_model[index][1][token]
			else:
				borrowed = giant_model[token]
				borrowed[0] += all_model[index][1][token][0]
				borrowed[1] += all_model[index][1][token][1]
				giant_model[token] = borrowed

	return giant_model


def words(model, all_model, ind):
	itfdf = {}

	tfdf_idf = {}

	for t in model[0]:

		out_model = out_data(all_model, ind)
		in_model = model[1]

		out_tf = 1
		out_df = 1

		if t in out_model:
			out_df += out_model[t][1]
			out_tf += out_model[t][0]

		out_itf = 1 / out_tf
		out_idf = 1 / out_df

		in_tf = in_model[t][0]
		in_itf = 1/ in_tf
		in_df = (in_model[t][1])

		itfdf_score = in_itf * in_df
		itfdf[t] = itfdf_score

		tfdf_idf_score = in_tf * in_df * out_itf * out_idf
		tfdf_idf[t] = tfdf_idf_score

	scoring_metric = tfdf_idf
	# scoring_metric = itfdf

	scores = sorted(scoring_metric.items(), key=operator.itemgetter(1), reverse=True)

	topic_words = []
	limit = 25
	for score in scores:
		if limit > 0:
			topic_words.append(score[0])
			limit -= 1

	return [topic_words, itfdf, tfdf_idf]