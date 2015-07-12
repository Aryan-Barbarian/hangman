
class Game(object):

	def __init__(self, word_length):
		self.no_contain = set()
		self.word_length = word_length;
		self.word = "_" * word_length
		self.word_db = 

	def display_word(self):
		
		for i in range(len(self.word)):
			to_print1 += char + " "
			to_print2 += i + " "
		
		self.printbuff()
		print(to_print1)
		print(to_print2)
		self.printbuff()
