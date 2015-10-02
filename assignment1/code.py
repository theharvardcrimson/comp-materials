import collections, string, operator

### swapchars
def swapchars(sentence):
	cnt = collections.Counter()
	countSentence = ''.join(filter(str.isalpha, sentence))
	for char in countSentence:
		cnt[char]+=1
	maxChar = cnt.most_common(1)[0][0]
	minChar = cnt.most_common()[len(cnt)-1][0]
	mapping = string.maketrans(maxChar+minChar ,minChar+maxChar)
	print sentence.translate(mapping)

swapchars('I\'m just a chi-town coder with a nice flow.')

### sortcat
def sortcat(*args):
	num = args[0]
	words = sorted(args[1::], key=len)[::-1]
	print ''.join(words[:num])

sortcat(2, 'bc', 'c', 'abc')

### Blue's Clues
abbrev={}
with open("states.txt") as f:
	for line in f:
		(val, key) = line.strip().split(',')
		abbrev[key] = val

def clues(code):
	print abbrev[code]

clues("PA")

### Blue's Booze
def booze(state):
	for stateAbbrev, stateName in abbrev.iteritems():
		if stateName == state:
			print stateAbbrev

booze("Nebraska")

######################################################
# If there was more several more states abbreviations
# that needed to be searched, I would create a new
# dictionary where the state name was the key and the
# state abbrevation was the value and implement a 
# function similar to clues
######################################################
