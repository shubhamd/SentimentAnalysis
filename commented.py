import nltk 
from nltk.corpus import stopwords 


customStopwords = ['band','they','them'] 


p = open('postweets.txt','r')
poslines = p.readlines() 
p.close()

""" poslines is an array of all the positive sentences. p.readlines() splits the input file into an array component lines. 

['I love their new album\n', 'I want to go and see them live\n', 'I like this band\n',
 'I love the lead singer he is so dreamy\n', 'I adore them they are so great\n', 'They are brilliant\n', 
 'They are the best\n', 'I love this band so much\n', 'I think this band are great\n', 'This band for president\n',
  'This band are better than North Korea\n', 'I want to see this band live\n', 'I love them they are the best']

"""
n = open('negtweets.txt', 'r')
neglines = n.readlines()
n.close()
# same as that of poslines 

neglist =[] 
poslist =[]

for i in range(len(neglines)):
	neglist.append("negative")

""" -here we created a list which contains as much "negative" as the number of lines in negtweets.txt 
	-why ? 
	-hold on :p 
"""
for i in range(len(poslines)):
	poslist.append("positive")
	
	#same as above 

postagged = zip(poslines,poslist)
negtagged = zip(neglines,neglist)
taggedTweets = postagged + negtagged 
tweets = [] 
for (sentence,sentiment) in taggedTweets :
	words = [i.lower() for i in sentence.split() ]
	tweets.append((words,sentiment)) 
#print tweets	
"""

****'words' at each iteration assumes following values resp. 


['i', 'love', 'their', 'new', 'album']
['i', 'want', 'to', 'go', 'and', 'see', 'them', 'live']
['i', 'like', 'this', 'band']
['i', 'love', 'the', 'lead', 'singer', 'he', 'is', 'so', 'dreamy']
['i', 'adore', 'them', 'they', 'are', 'so', 'great']
['they', 'are', 'brilliant']
['they', 'are', 'the', 'best']
['i', 'love', 'this', 'band', 'so', 'much']
['i', 'think', 'this', 'band', 'are', 'great']
['this', 'band', 'for', 'president']
['this', 'band', 'are', 'better', 'than', 'north', 'korea']
['i', 'want', 'to', 'see', 'this', 'band', 'live']
['i', 'love', 'them', 'they', 'are', 'the', 'best']
['this', 'band', 'is', 'awful']
['this', 'is', 'terrible']
['they', 'make', 'me', 'feel', 'bad']
['this', 'band', 'are', 'not', 'that', 'great']
['this', 'is', 'absolutely', 'atrocious']
['i', 'dislike', 'them']
['this', 'band', 'are', 'the', 'worst']
['what', 'the', 'hell', 'is', 'this', 'crap']
['this', 'band', 'should', 'die']
['i', 'hate', 'this', 'band']
['this', 'band', 'make', 'me', 'want', 'to', 'die']
['my', 'ears', 'are', 'dying']
['they', 'suck', 'they', 'are', 'terrible']


tweets : is an array of tuples. each tuple contains 
a tweet with splitted words and associated sentiment tag. 

[
	(['i', 'love', 'their', 'new', 'album'], 'positive'), 
	(['i', 'want', 'to', 'go', 'and', 'see', 'them', 'live'], 'positive'),
 	(['i', 'like', 'this', 'band'], 'positive'), 
 	(['i', 'love', 'the', 'lead', 'singer', 'he', 'is', 'so', 'dreamy'], 'positive'), 
 	(['i', 'adore', 'them', 'they', 'are', 'so', 'great'], 'positive'),
  	(['they', 'are', 'brilliant'], 'positive'), 
  	(['they', 'are', 'the', 'best'], 'positive'),
   	(['i', 'love', 'this', 'band', 'so', 'much'], 'positive'), 
   	(['i', 'think', 'this', 'band', 'are', 'great'], 'positive'), 
   	(['this', 'band', 'for', 'president'], 'positive'), 
   	(['this', 'band', 'are', 'better', 'than', 'north', 'korea'], 'positive'), 
   	(['i', 'want', 'to', 'see', 'this', 'band', 'live'], 'positive'), 
   	(['i', 'love', 'them', 'they', 'are', 'the', 'best'], 'positive'),
    (['this', 'band', 'is', 'awful'], 'negative'), 
    (['this', 'is', 'terrible'], 'negative'), 
    (['they', 'make', 'me', 'feel', 'bad'], 'negative'), 
    (['this', 'band', 'are', 'not', 'that', 'great'], 'negative'), 
    (['this', 'is', 'absolutely', 'atrocious'], 'negative')...... and so on...
 ]   
"""	

def getwords(tweets):
	allwords=[]
	for (words,sentiment) in tweets :
		allwords.extend(words)
	return allwords
#print getwords(tweets)

"""
getwords returns a list of all the words in negative tweets and positive tweets

['i', 'love', 'their', 'new', 'album', 'i', 'want', 'to', 'go', 'and', 'see', 'them', 'live', 
'i', 'like', 'this', 'band', 'i', 'love', 'the', 'lead', 'singer', 'he', 'is', 'so', 'dreamy',
'i', 'adore', 'them', 'they', 'are', 'so', 'great', 'they', 'are', 'brilliant', 'they', 'are',
'the', 'best', 'i', 'love', 'this', 'band', 'so', 'much', 'i', 'think', 'this', 'band', 'are',
'great', 'this', 'band', 'for', 'president', 'this', 'band', 'are', 'better', 'than', 'north',
'korea', 'i', 'want', 'to', 'see', 'this', 'band', 'live', 'i', 'love', 'them', 'they', 'are',
'the', 'best', 'this', 'band', 'is', 'awful', 'this', 'is', 'terrible', 'they', 'make', 'me',
'feel', 'bad', 'this', 'band', 'are', 'not', 'that', 'great', 'this', 'is', 'absolutely', 
'atrocious', 'i', 'dislike', 'them', 'this', 'band', 'are', 'the', 'worst', 'what', 'the',
'hell', 'is', 'this', 'crap', 'this', 'band', 'should', 'die', 'i', 'hate', 'this', 'band',
'this', 'band', 'make', 'me', 'want', 'to', 'die', 'my', 'ears', 'are', 'dying', 'they',
'suck', 'they', 'are', 'terrible']


"""		
def getwordfeatures(listofwords):
	wordfreq = nltk.FreqDist(listofwords)
	words = wordfreq.keys()
	return words
"""

	wordfreq contains the FreqDist of all the words in the given dataset (= positive + negative tweets)
	
	<FreqDist: 
	'this': 15, 
	'band': 12, 
	'i': 11, 
	'are': 10, 
	'they': 7, 
	'is': 5,
	'the': 5,
	'love': 4,
	'them': 4,
	'great': 3, ...>
	



"""
	
"""
 words = wordfreq.keys()

 so the "words" array contains this(words without repetition/ keys of a hashmap) :

['this', 'band', 'i', 'are', 'they', 'is', 'the', 'love', 'them', 'great', 'so', 'to', 
'want', 'best', 'die', 'live', 'make', 'me', 'see', 'terrible', 'absolutely', 'adore', 
'album', 'and', 'atrocious', 'awful', 'bad', 'better', 'brilliant', 'crap', 'dislike', 
'dreamy', 'dying', 'ears', 'feel', 'for', 'go', 'hate', 'he', 'hell', 'korea', 'lead', 
'like', 'much', 'my', 'new', 'north', 'not', 'president', 'should', 'singer', 'suck', 
'than', 'that', 'their', 'think', 'what', 'worst']

"""
wordlist = getwordfeatures(getwords(tweets))
wordlist = [i for i in wordlist if not i in customStopwords ]
wordlist = [i for i in wordlist if not i in stopwords.words('english')]

""" 
refinement of input data completed :

now wordlist contains :

['love', 'great', 'want', 'best', 'die', 'live', 'make', 'see', 'terrible', 'absolutely',
 'adore', 'album', 'atrocious', 'awful', 'bad', 'better', 'brilliant', 'crap', 'dislike',
  'dreamy', 'dying', 'ears', 'feel', 'go', 'hate', 'hell', 'korea', 'lead', 'like', 'much',
   'new', 'north', 'president', 'singer', 'suck', 'think', 'worst']
"""

def featureExtracter(doc):
	docwords=set(doc)     # we are converting it into doc, cuz "in" works faster with sets. 
	features = {}         # an empty dictionary, which will contains input sentence in hashed form. 
	for i in wordlist :
		features['contains(%s)'%i] = i in docwords
	return features 
training_set = nltk.classify.apply_features(featureExtracter, tweets)	
print training_set 	

"""

training_set contains : 
an array of tupples, each tuple contains two elements : 

1. list of key-value pairs(dictionary), in which each key is a word in a tweet. 				
2. sentiment of the tweet. 

**** following output shows contents of 'training_set' for the tweet "i love their new album."

"i" has been strpped off by the stopwords filtering. 
"love" is present. so the "contains(love)" is set to "True". 
"their" has been removed by stopwords fltering. 
"new" is present. --> contains(new) = True
"album" is present --> contains(album) = True
and at the end, "positive" is the second element in the first tuple of the list. 


same this is repeated for the remaining tweets in "tweets" list. 

[({'contains(korea)': False, 'contains(go)': False, 'contains(suck)': False, 'contains(new)': True, 'contains(hate)': False, 'contains(absolutely)': False, 'contains(ears)': False, 'contains(dying)': False, 'contains(think)': False, 'contains(singer)': False, 'contains(love)': True, 'contains(adore)': False, 'contains(feel)': False, 'contains(north)': False, 'contains(lead)': False, 'contains(album)': True, 'contains(president)': False, 'contains(dreamy)': False, 'contains(die)': False, 'contains(worst)': False, 'contains(bad)': False, 'contains(great)': False, 'contains(see)': False, 'contains(like)': False, 'contains(brilliant)': False, 'contains(terrible)': False, 'contains(want)': False, 'contains(best)': False, 'contains(hell)': False, 'contains(live)': False, 'contains(atrocious)': False, 'contains(awful)': False, 'contains(much)': False, 'contains(make)': False, 'contains(crap)': False, 'contains(better)': False, 'contains(dislike)': False}, 'positive'), ({'contains(korea)': False, 'contains(go)': True, 'contains(suck)': False, 'contains(new)': False, 'contains(hate)': False, 'contains(absolutely)': False, 'contains(ears)': False, 'contains(dying)': False, 'contains(think)': False, 'contains(singer)': False, 'contains(love)': False, 'contains(adore)': False, 'contains(feel)': False, 'contains(north)': False, 'contains(lead)': False, 'contains(album)': False, 'contains(president)': False, 'contains(dreamy)': False, 'contains(die)': False, 'contains(worst)': False, 'contains(bad)': False, 'contains(great)': False, 'contains(see)': True, 'contains(like)': False, 'contains(brilliant)': False, 'contains(terrible)': False, 'contains(want)': True, 'contains(best)': False, 'contains(hell)': False, 'contains(live)': True, 'contains(atrocious)': False, 'contains(awful)': False, 'contains(much)': False, 'contains(make)': False, 'contains(crap)': False, 'contains(better)': False, 'contains(dislike)': False}, 'positive'), ...]

"""


# finally, we feed this training_set to the NaiveBayesClassifier for training.

classifier = nltk.NaiveBayesClassifier.train(training_set)

# accept the input, break it into words, and pass it to the classifier.


while True:
	input = raw_input("Please write a sentence. write \"exit\" to quit.\n")
	if input == 'exit':
		break
	else:
		input = input.lower()
		input = input.split()
		print '\nWe think that the sentiment was ' + classifier.classify(feature_extractor(input)) + ' in that sentence.\n'
 
