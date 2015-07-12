"""
words, length, num_each_letter
"""
def process_file(filepath):
	header = ["word", "length"] + [chr(ord("A") + i) for i in range(26)]
	all_words = list()
	num_words = 0
	with open(filepath) as f:
		for line in f:
			word = "".join(line.split()).upper();
			if word.find("'S") != -1: # Deal with later
				continue;
			length = len(word);
			num_letters = get_num_letters(word)
			row = [word, length] + num_letters
			all_words.append(row)
			num_words += 1
	return all_words



# MUST BE UPPER CASE AND ONLY LETTERS
def get_num_letters(word):
	ans = [0 for i in range(26)]

	for char in word:
		index = ord(char) - ord("A")
		if index < 26:
			ans[index] += 1

	return ans

a = process_file("linux_words.txt")