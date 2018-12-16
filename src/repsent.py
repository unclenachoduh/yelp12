# Returns a representative sentence from the data based on ITFDF score per token
import operator

def sentence(model, itf):

	rep_sent_dict = {}

	for sent in model[2]:

		rep_sent_score = 0
		
		for t in model[3][sent]:
			rep_sent_score += itf[t]

		if len(model[3][sent]) < (model[8]/model[7]):

			rep_sent_dict[sent] = rep_sent_score

	rep_sent_results = sorted(rep_sent_dict.items(), key=operator.itemgetter(1), reverse=True)

	return rep_sent_results[0][0]