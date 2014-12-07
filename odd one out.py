import nltk
from nltk.corpus import wordnet as wn

def hypernyms(word):
	lemma = wn.lemmas(word)[0]
	synset = wn.synset(lemma)
	return set([w for s in vehicle.closure(lambda s:s.hypernyms()) for w in s.lemma_names])

def wordsToSynsets(words):
	synsets = list()
	for w in words:
		wordsSynsets = wn.synsets(w)
		if len(wordsSynsets) == 0:
			print("I don't know about " + w + ".")
			synsets.append(None)
		else:
			synsets.append(wordsSynsets[0])
	return synsets

def similarity(synsets):
	if len(synsets) < 2:
		return 1
	if len(synsets) == 2:
		return synsets[0].path_similarity(synsets[1])
	return similarity(synsets[0:2]) * similarity(synsets[1:])

def pick(l, index):
	l = list(l)
	v = l[index]
	del l[index]
	return l, v


# The game is played by passing words to this function. It'll return what it
# thinks is the odd one out.
def odd(*words):
	synsets = wordsToSynsets(words)
	hasNonNoun = False
	for i in range(len(synsets)):
		if synsets [i] is not None and synsets[i].pos != 'n':
			print(words[i] + " is not a noun. I can only play this game with nouns.")
			hasNonNoun = True
	if hasNonNoun:
		return None
	if any(x is None for x in synsets):
		return None
	oddestWordIndex = 0
	bestSim = 0
	for i in range(len(synsets)):
		ws, w = pick(synsets, i)
		sim = similarity(ws)
		if sim > bestSim:
			bestSim = sim
			oddestWordIndex = i
	return words[oddestWordIndex]
