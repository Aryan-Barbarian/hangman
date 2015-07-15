
class Guesser(object):
	def __init__(self, game):
		self.game = game
		self.word_db = game.word_db

	def best_letter(self):
		game_word = self.game.visible_word()
		no_contains = self.game.wrongs
		self.word_db = self.word_db.filter(game_word, no_contains)
		guesses = self.game.guesses
		for letter, num_occurrences in self.word_db.common_letters():
			if letter not in guesses:
				return letter

	def move(self):
		pass

	def reset(self):
		self.word_db = self.game.word_db

class AIGuesser(Guesser):
	def move(self):
		return "guess {}".format(self.best_letter())

class HumanGuesser(Guesser):
	def move(self):
		return raw_input("> ")

class Knower(object):
	def __init__(self, game):
		self.game = game
		self.word_db = game.word_db

	def get_word(self):
		pass


class AIKnower(Knower):
	def get_word(self):
		return self.word_db.random_word()

class HumanKnower(Knower):
	def get_word(self):
		return raw_input("Before you start, what's the word?")
