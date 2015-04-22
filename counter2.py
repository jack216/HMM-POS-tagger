import nltk
brown_tag_sents = nltk.corpus.brown.tagged_sents(tagset='universal')
countsT = {}
countsE = {}
for sentence in brown_tag_sents:
	for i in range(0, len(sentence)):
		if i == 0:
			countsT[('$', sentence[i][1] )] =1.0
			countsE[sentence[i][1], sentence[i][0].lower()] = 1.0
		keyT= (sentence[i-1][1], sentence[i][1] )
		if countsT.has_key(keyT):
			countsT[keyT] += 1
		else:
			countsT[keyT] = 1.0

		keyE= (sentence[i][1], sentence[i][0] )
		if countsE.has_key(keyE):
			countsE[keyE] += 1
		else:
			countsE[keyE] = 1.0

def total_count(prev_state):
	keys = countsT.keys()
	count = 0.0
	for i in keys:
		if i[0] == prev_state:
			count += countsT[i]
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
probabilitiesT ={}
keys = countsT.keys()
for key in keys:
	probabilitiesT[key]= countsT[key]/ total_counts[key[0]]
#print countsT

probabilitiesE ={}
keys = countsE.keys()
for key in keys:
	probabilitiesE[key]= countsE[key]/ total_counts[key[0]]

