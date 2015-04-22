import counter

sentence = "she wanted to race ."

words = sentence.split()
tagged_words = words
states = ['NOUN' , 'VERB' , 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'PRT', 'PRON', 'NUM', 'X', '$', '.', ',']
curr_state='$'
table=[]

def selectFirst(obj):
	return obj[0]

counter1=0
for word in words:
	observation = []	
	if curr_state=='$':
		for state in states:
			try:
				observation.append((counter.probabilities['$', state, word], '$'))
			except (KeyError): 
				observation.append((0.0, '$'))
		
		
	else:
		for toState in states:
			counter2 = 0
			currProbs=[]
			for fromState in states:
				
				try:
					prob= counter.probabilities[fromState, toState, word]
					#print fromState+ ' ' + toState + ' ' + word +' : '+ str(prob)
				except (KeyError): 
					prob = 0.0
				currProbs.append(table[counter1-1][counter2][0]*prob)
				counter2 +=1
			observation.append((max(currProbs), currProbs.index(max(currProbs))))
	
	
	#print observation	
	curr_state = states[observation.index(max(observation, key=selectFirst))]
	#print curr_state	
	table.append(observation)
	counter1 += 1

index = table[-1].index(max(table[-1], key=selectFirst))
for i in range(len(table)-1, -1, -1):
	
	tagged_words[i] += '-'+states[index]
	index = table[i][index][1]

print tagged_words
	


			 

			

		
	
