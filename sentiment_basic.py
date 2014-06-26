import nltk

customstopwords = ['band', 'they', 'them']

p = open('postweets.txt', 'r')
postxt = p.readlines()
p.close()

n = open('negtweets.txt', 'r')
negtxt = n.readlines()
n.close()

neglist = []
poslist = []
 
for i in range(0,len(negtxt)):
	neglist.append('negative')
 
for i in range(0,len(postxt)):
	poslist.append('positive')
 
postagged = zip(postxt, poslist)
negtagged = zip(negtxt, neglist)
 
taggedtweets = postagged + negtagged

tweets = []
 
for (word, sentiment) in taggedtweets:
	word_filter = [i.lower() for i in word.split()]
	tweets.append((word_filter, sentiment))
 
def getwords(tweets):
	allwords = []
	for (words, sentiment) in tweets:
		allwords.extend(words)
	return allwords
 
def getwordfeatures(listoftweets):
	wordfreq = nltk.FreqDist(listoftweets)
	words = wordfreq.keys()
	return words
 
wordlist = getwordfeatures(getwords(tweets))

wordlist = [i for i in wordlist if not i in customstopwords]
def feature_extractor(doc):
	docwords = set(doc)
	features = {}
	for i in wordlist:
		features['contains(%s)' % i] = (i in docwords)
	return features
training_set = nltk.classify.apply_features(feature_extractor, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

while True:
	input = raw_input("Please write a sentence. write \"exit\" to quit.\n")
	if input == 'exit':
		break
	else:
		input = input.lower()
		input = input.split()
		print '\nWe think that the sentiment was ' + classifier.classify(feature_extractor(input)) + ' in that sentence.\n'
 
