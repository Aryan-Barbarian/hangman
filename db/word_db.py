import random
# TODO: Make this fully immutable
class WordDB(object):

	def __init__(self, word_counts=None, word_file=None):
		if word_counts is not None:
			self.word_counts = word_counts
		elif word_file is not None:
			self.word_counts = self.process_file(word_file)
		else:
			raise Exception("You must provide either a word list or a word file")
		# print(self.word_counts[:50])


	"""
	words, length, num_each_letter
	"""
	def process_file(self, filepath):
		words_with_counts = list()
		with open(filepath) as f:
			for line in f:
				line = line.split("\t")
				if len(line) > 1:
					word, count = line
				else:
					continue
				word = word.upper().replace("\n","")
				count = int(count)
				words_with_counts.append((word, count))
		return words_with_counts

	# MUST BE UPPER CASE AND ONLY LETTERS
	def get_num_letters(self, word, dilation = 1):
		ans = [0 for i in range(26)]

		for char in word:
			index = ord(char) - ord("A")
			if index < 26:
				ans[index] += dilation
		return ans

	def filter(self, game_word, no_contain):
		word_len = len(game_word)
		def fn(word_with_count):
			word, count = word_with_count
			if len(word) != word_len:
				return False
			for i in range(word_len):
				if game_word[i] != "_" and game_word[i] != word[i]:
					return False
			for char in no_contain:
				if char in word:
					return False
			return True

		new_words =  filter(fn, self.word_counts)
		return WordDB(word_counts=new_words);

	def get_letter_sums(self):
		ans = [0 for i in range(26)]
		for word, count in self.word_counts:
			letter_count = self.get_num_letters(word, count)
			for i in range(26):
				ans[i] += letter_count[i]
		return ans

	def common_letters(self, no_contain=set()):
		letter_sums = self.get_letter_sums()
		letter_sums = [(chr(ord("A") + i), letter_sums[i]) for i in \
			range(len(letter_sums))]
		letter_sums = filter(lambda (letter, sum): letter not in no_contain, letter_sums)
		return sorted(letter_sums, reverse=True, key = lambda (letter, num): num)


	def random_word(self):
		index = random.randint(0, len(self.word_counts))
		print(self.word_counts[index - 10: index + 10])
		ans = self.word_counts[index]
		return ans[0]

	def copy(self):
		return WordDB(word_counts=self.word_counts[:])