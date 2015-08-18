####################################################################

#Imports

#Body

def get_words(file_):
	with open(file_) as f:
		lines_in_file = f.read().split()	#Creates a list of words
		#Convert list to dict so it is usable in create_word_dict
		lines_in_file_dict = {line:1 for line in lines_in_file}				#1 is just an arbitrary filler.			
		return lines_in_file_dict		


def create_word_dict(words_dict):
	'''Takes a list of words. If a given word doesn't have an 
	anagram existing in the dictionary, it is added to the
	dictionary under a new key (note, the keys are sets of 
	characters). If the set of characters used in the word
	already exist in the dictionary, then the word is appended
	to the list of anagrams in the values.
	'''
	anagram_dict = {}

	#Takes words from the dictionary of words and converts 
	#into a dictionary of anagrams
	for word, value in words_dict.iteritems():
		word_sorted = tuple(sorted(word))
		anagram_dict.setdefault(word_sorted, []).append(word)

	return anagram_dict


def print_anagrams(anagram_dict):
	'''The function is passed a dictionary of anagrams 
	and prints each set of anagrams, printing the sets with 
	the most words first.
	'''
	list_of_anagrams = anagram_dict.values()
	# list_of_anagrams = [anagram for anagram in list_of_anagrams if len(anagram)>1]
	list_of_anagrams = [anagram for anagram in list_of_anagrams if len(anagram)>1]

	list_of_anagrams = sorted(list_of_anagrams, key = len, reverse = True)

	print list_of_anagrams

def find_max_bingos(anagram_dict):
	'''Function finds the set of 8 letters that returns the 
	most possible bingos in scrabble.
	'''
	max_bingos = 0
	set_of_8_letters = None
	for key, value in anagram_dict.iteritems():
		if len(key) >= 8:
			if len(value) > max_bingos:
				max_bingos = len(value)
				set_of_8_letters = key
	print 'The following set of 8 letters returns the most possible bingos in scrabble {0}'.format(set_of_8_letters) 
	

####################################################################

def main():
	'''Reads a word list from a file, and prints all the sets
	of words that are anagrams.

	A set of anagrams are words that use all the same letters, exactly
	once, but in a different order. 
	Ex: ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
	'''
	print_anagrams(create_word_dict(get_words('words.txt')))
	find_max_bingos(create_word_dict(get_words('words.txt')))


if __name__ == "__main__":
	main()