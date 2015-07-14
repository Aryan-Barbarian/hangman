
from db.word_db import WordDB

class Game(object):
	def __init__(self, knower, guesser):
		knower.game = self # Knows the word
		guesser.game = self # Guesses
		self.knower = knower
		self.guesser = guesser

		self.word = "_" * self.knower.word_length()

		self.guesses = set()
		self.wrongs = set()

		self.turn = 0;

	def display_word(self):
		to_print1 = ""
		to_print2 = ""
		for i in range(len(self.word)):
			char = self.word[i]
			to_print1 += char + " "
			to_print2 += str(i) + " "
		print(to_print1)
		print(to_print2)

	def play(self):
		guess = self.guesser.guess()
		self.handle_guess(guess)
		# self.printbuff()
		# print("Guess: {}".format(guess))
		# print("Word now: ")
		# self.display_word()
		# print("Number of possible words: {}".format(len(self.guesser.word_db.words)))
 	# 	self.printbuff()
		return "_" in self.word


	def handle_guess(self, guessed_letter):
		if guessed_letter in self.guesses:
			return;

		self.guesses.add(guessed_letter)
		result = self.knower.handle_guess(guessed_letter)
		if not result:
			self.wrongs.add(guessed_letter)
		else:
			new_word = ""
			for i in range(len(self.word)):
				if i in result:
					new_word += guessed_letter
				else:
					new_word += self.word[i]
			self.word = new_word

	def printbuff(self):
		print("*"*20)

class Knower(object):

	def __init__(self, word):
		self.word = word.upper()

	def handle_guess(self, guessed_letter):
		if guessed_letter in self.word:
			to_send = list();
			for i in range(len(self.word)):
				if guessed_letter == self.word[i]:
					to_send.append(i)
			return to_send
		else:
			return False

	def word_length(self):
		return len(self.word)

class Guesser(object):

	def __init__(self):
		self.game = None
		self.word_db = WordDB(word_file="./db/linux_words.txt")

	def guess(self):
		if self.game is not None:
			game_word = self.game.word
			no_contains = self.game.wrongs
			self.word_db = self.word_db.filter(game_word, no_contains)
			guesses = self.game.guesses
			for letter, num_occurrences in self.word_db.common_letters():
				if letter not in guesses:
					return letter
			game_word = self.game.word
			no_contains = self.game.wrongs
			self.word_db = self.word_db.filter(game_word, no_contains)
		print("Could Not Guess!")
		return None

def play():
	
	word_db = WordDB(word_file="./db/linux_words.txt")
	words = " ".join([word_db.random_word() for i in range(100)])
	for word in words.split():
		guesser = Guesser()
		knower = Knower(word)
		game = Game(knower, guesser)
		while game.play():
			pass;

		pad_len = 30 - len(word);

		print("{}{} : {}".format(word, " " * pad_len, len(game.wrongs)))
	


play()