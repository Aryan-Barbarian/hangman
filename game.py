from db.word_db import WordDB

usuage = """
help - Prints commands
auto <knower/guesser> - will make one of these automatic
start - starts the game
guess <letter> - guesses this letter
hint - prints the letter that the AI would pick
word <new_word> - Restarts the game if in progress and sets this as the word
clear - Clears the screen
"""

class Game(object):
	def __init__(self):
		self._word_db = WordDB(word_file="./db/count.txt")

		self.guesser = HumanGuesser(self)
		self.knower = HumanKnower(self)
		self.word = ""
		
		self.known_positions = set()
		self.guesses = set()
		self.wrongs = set()

		self.started = False

	def visible_word(self):
		ans = ""

		for i in range(len(self.word)):
			if i in self.known_positions:
				ans += self.word[i]
			else:
				ans += "_"
		return ans

	def display_word(self):
		to_print1 = ""
		to_print2 = ""
		visible = self.visible_word()
		for i in range(len(visible)):
			char = visible[i]
			to_print1 += char + " "
			to_print2 += str(i) + " "
		print(to_print1)
		print(to_print2)

	def clear_screen(self):
		print("\n" * 80)

	def play_game(self):
		while "_" in self.visible_word() or len(self.word) == 0:
			if not self.started:
				move = raw_input("> ").split()
			else:
				move = self.guesser.move().split()
			if len(move) != 0:
				self.play_turn(move)
				self.display_word()
		print("YOU WON IN {} GUESSES".format(len(self.guesses)))

	def display_stickman()

	def play_turn(self, move):
		name = move[0]
		
		if name ==  "help":
			print(usuage)

		elif name == "auto":
			if move[1] == "knower":
				self.knower = AIKnower(self)
			elif move[1] == "guesser":
				self.guesser = AIGuesser(self)
			elif move[1] == "all":
				self.guesser = AIGuesser(self)
				self.knower = AIKnower(self)
			else:
				print("Unknown argument: {}".format(move[1]))

		elif name == "nan":
			if move[1] == "knower":
				self.knower = HumanKnower(self)
			elif move[1] == "guesser":
				self.guesser = HumanGuesser(self)
			elif move[1] == "all":
				self.guesser = HumanGuesser(self)
				self.knower = HumanKnower(self)
			else:
				print("Unknown argument: {}".format(move[1]))
		
		elif name == "start":
			if len(self.word) == 0:
				new_word = self.knower.get_word() # TODO: Turn this to a do while loop
				while not self.validate_word(new_word):
					new_word = self.knower.get_word()
				self.word = new_word.upper()
			self.started = True
			self.clear_screen()
			print("Game started!")

		elif name == "guess":
			if not self.started:
				print("To make this move, you must first start the game")
			else:
				letter = move[1]
				self.handle_guess(letter)

		elif name == "hint":
			if not self.started:
				print("To make this move, you must first start the game")

		elif name == "word":
			new_word = move[1]
			if self.validate_word(new_word):
				self.started = False
				self.guesser.reset()
				self.word = word
				self.clear_screen()
				print("New Word Set")
			else:
				print("That is an invalid word")

		elif name == "clear":
			self.clear_screen()
		else:
			print("Unknown command: {}".format(name))
		
		return True

	@property
	def word_db(self):
	    return self._word_db.copy()
	
	def handle_guess(self, guessed_letter):
		guessed_letter = guessed_letter.upper()
		if guessed_letter in self.guesses:
			print("You've guessed this before")
			return;

		self.guesses.add(guessed_letter)
		correct = False
		for i in range(len(self.word)):
			if self.word[i] == guessed_letter:
				correct = True
				self.known_positions.add(i)
		if not correct:
			print("This is incorrect")
			self.wrongs.add(guessed_letter)
		else:
			print("Correct!")

	def printbuff(self):
		print("*"*20)

	def validate_word(self, word):
		return True # TODO: Implement this later

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
		self.word_db = game.word_db

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

def main():
	game = Game()
	game.play_game()

main()