
from db.word_db import WordDB
class Game(object):
	def __init__(self, knower, guesser):
		player1.game = self # Knows the word
		player2.game = self # Guesses
		self.knower = knower
		self.guesser = guesser

		self.word = "_" * self.knower.word_length()

		self.guesses = set()
		self.wrongs = set()

		self.turn = 0;

	def display_word(self):
		for i in range(len(self.knower.word)):
			to_print1 += char + " "
			to_print2 += i + " "
		self.printbuff()
		print(to_print1)
		print(to_print2)
		self.printbuff()


	def play(self):
		guess = guesser.guess()
		handle_guess(guess)
		

		return "_" in self.word


	def handle_guess(self, guessed_letter):
		if guessed_letter in self.guesses:
			return;

		self.guesses.add(guessed_letter)
		result = self.knower.handle_guess(guessed_letter)

		if result is None:
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
			to_send = "";
			for i in range(len(self.word)):
				if guessed_letter == self.word[i]:
					to_send.append(i)
			return to_send
		else:
			return False

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
			for letter, num_occurrences in self.word_db.common_letters:
				if letter not in guesses:
					return letter
		print("Could not guess!")
		return None

def play():
	guesser = Guesser()
	knower = Knower("hello")
	game = Game(word_len, knower, guesser)
	
	while game.play():
		game.display_word()
	


play()