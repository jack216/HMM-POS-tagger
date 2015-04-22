import nltk
brown_tag_sents = nltk.corpus.brown.tagged_sents(tagset='universal')
counts = {}
for sentence in brown_tag_sents:
	for i in range(0, len(sentence)):
		if i == 0:
			counts[('$', sentence[i][1], sentence[i][0].lower() )] =1
		key= (sentence[i-1][1], sentence[i][1], sentence[i][0].lower() )
		if counts.has_key(key):
			counts[key] += 1
		else:
			counts[key] = 1.0

def total_count(prev_state):
	keys = counts.keys()
	count = 0.0
	for i in keys:
		if i[0] == prev_state:
			count += counts[i]
	return count
total_counts = {}
total_counts['NOUN']= total_count('NOUN')
total_counts['VERB']= total_count('VERB')
total_counts['ADJ']= total_count('ADJ')
total_counts['ADP']= total_count('ADP')
total_counts['ADV']= total_count('ADV')
total_counts['CONJ']= total_count('CONJ')
total_counts['DET']= total_count('DET')
total_counts['PRT']= total_count('PRT')
total_counts['PRON']= total_count('PRON')
total_counts['NUM']= total_count('NUM')
total_counts['X']= total_count('X')
total_counts['$']= total_count('$')
total_counts['.']= total_count('.')
total_counts[',']= total_count(',')



probabilities ={}
keys = counts.keys()
for key in keys:
	probabilities[key]= counts[key]/ total_counts[key[0]]

probabilities['START', '$', '$'] =1
	

