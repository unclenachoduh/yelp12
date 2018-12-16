# Returns a representative review from the data based on ITFDF score per token
import operator

def review(model, itf):

	rep_rev_dict = {}

	for rev in model[4]:

		rep_rev_score = 0
		
		for t in model[5][rev]:
			rep_rev_score += itf[t]

		if len(model[5][rev]) < (model[8]/model[6]):

			rep_rev_dict[rev] = rep_rev_score

	rep_rev_results = sorted(rep_rev_dict.items(), key=operator.itemgetter(1), reverse=True)

	return rep_rev_results[0][0]