import random

class WordDB(object):

	def __init__(self, words=None, word_file=None):
		if words is not None:
			self.words = words
		elif word_file is not None:
			self.words = self.process_file(word_file)
		else:
			self.words = list()

	"""
	words, length, num_each_letter
	"""
	def process_file(self, filepath):
		header = ["word", "length"] + [chr(ord("A") + i) for i in range(26)]
		all_words = list()
		num_words = 0
		with open(filepath) as f:
			for line in f:
				word = "".join(line.split()).upper();
				if word.find("'S") != -1: # Deal with later
					continue;
				all_words.append(word)
		return all_words

	# MUST BE UPPER CASE AND ONLY LETTERS
	def get_num_letters(self, word):
		ans = [0 for i in range(26)]

		for char in word:
			index = ord(char) - ord("A")
			if index < 26:
				ans[index] = 1
		return ans

	def filter(self, game_word, no_contain):
		word_len = len(game_word)
		def fn(word):
			if len(word) != word_len:
				return False
			for i in range(word_len):
				if game_word[i] != "_" and game_word[i] != word[i]:
					return False
			for char in no_contain:
				if char in word:
					return False
			return True

		new_words =  filter(fn, self.words)
		return WordDB(words=new_words);

	def get_letter_sums(self):
		ans = [0 for i in range(26)]
		for word in self.words:
			letter_count = self.get_num_letters(word)
			for i in range(26):
				ans[i] += letter_count[i]
		return ans

	def common_letters(self):
		letter_sums = self.get_letter_sums()
		letter_sums = [(chr(ord("A") + i), letter_sums[i]) for i in \
			range(len(letter_sums))]
		return sorted(letter_sums, reverse=True, key = lambda (letter, num): num)

	def random_word(self):
		return random.choice(self.words)
