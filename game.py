from db.word_db import WordDB
from players import HumanGuesser, HumanKnower, AIKnower, AIGuesser
from config import stickman, usuage

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
				self.display_stickman()
		print("YOU WON IN {} GUESSES".format(len(self.guesses)))

	def display_stickman(self):
		num_wrong = len(self.wrongs)
		if num_wrong >= len(stickman):
			num_wrong = len(stickman) - 1
		print(stickman[num_wrong])

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
			else:
				best = self.guesser.best_letter()
				print("The AI suggests \"{}\"".format(best))

		elif name == "word":
			new_word = move[1]
			print(new_word)
			if self.validate_word(new_word):
				self.started = False
				self.guesser.reset()
				self.word = new_word.upper()
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
