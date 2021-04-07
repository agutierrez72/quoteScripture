import random
import copy
import os

#Class for Scripture: contains book, address, and text of each verse
class Memory_Verse:
	def __init__(self, book, address, verse):
		"""This is the constructor of the verse class"""    
		self.book = book
		self.address = address
		self.verse = verse

	def myfunc(self):
		"""This is the display/print function for the verse class"""
		print("This verse is in " + self.book)
		txt = "The address of this verse is {}:{}"
		print(txt.format(self.address[0], self.address[1]))
		print(self.verse)
		print

def printList(sz, list):
	"""This function prints the verses in the list"""
	for x in range(0, sz):
		list[x].myfunc()

def start():
	"""This function initializes a list of verses by adding the first verse"""
	#first verse added to Scripture Library
	book = "Colossians"
	address = [3, 12]
	verse = "Therefore, as the elect of God holy and beloved, put on tender mercies, kindness, meekness, and long suffering."

	#verse1 = Memory_Verse(book, address, verse)
	#verse1.myfunc()

	list = []
	list.append(Memory_Verse(book, address, verse))
	list[0].myfunc()

	return list

#Function to allow user to add a new scripture to stored lists
def addScripture(sz, list):
	"""This function allows user to add new scriptures to the stored list of verses"""
	#User can add new scriptures to list
	size = sz
	newVerse = bool(True)
	# list = start()
	while(newVerse):
		address = []
		print("\nLet's Memorize some Verses!\n")
		book = raw_input("Book: ")
		address.append(input("chapter: "))
		address.append(input("verse: "))
		verse = raw_input("scripture: ")

		list.append(Memory_Verse(book, address, verse))
		list[size].myfunc()

		addNew = raw_input("add another scripture? (Y/N)")

		#ask user if they would like to add another verse
		if(addNew == "N" or addNew == "n"):
			print("no more scriptures to be added")
			newVerse = bool(False)
			

		# list[size].myfunc()
		size = size + 1
	return size

#Function to allow user to practice writing scripture all the way through until all words are input correctly in succession
def practiceScripture(size, list):
	"""Function requires user to input verse from the start repeatedly 
	until entire verse has been entered in the correct order"""
	#Quiz portion of program
	print("\nTest Time!")

	# list = start()

	#splitVerse is the list of words user enters in order
	splitVerse = (list[size].verse).split()

	#splitShuffle is a list of all words of scripture rendered in random order
	splitShuffle = copy.deepcopy(splitVerse)
	random.shuffle(splitShuffle)

	#solution is a list of blanks and words user has entered correctly
	solution = []
	#solution_index is a list of indexes from solution list that are still stored as blanks
	solution_index = []

	for x in range(len(splitVerse)):
		solution.append('______')
		solution_index.append(x)

	#print list of shuffled words in verse
	print(' '.join(str(x) for x in splitShuffle))

	#display solution (appears like hangman)
	print(' '.join(str(x) for x in solution))

	#compare user input to stored verse,
	# store words in solution array if user inputs correctly
	# user has to reenter entire phrase each time prompted
	while len(solution_index) > 0:
		#let's allow user to enter multiple words before submitting
		print("\nComplete the verse!")
		user_input = raw_input()

		#store user input as an array
		splitInput = user_input.split()

		score = "{} Mistakes, {} Words Remaining"
		errors = 0

		#for all words entered by user
		for x in range(len(splitInput)):
	    	#if the solution still contains blanks
			if(solution_index.count(x) > 0):
	    		#if user entry index equals correct scripture entry
				if splitInput[x] == splitVerse[x]:
					#replace solution blank with user entry input
					solution[x] = splitInput[x]
					#delete index from blanks in solution list
					solution_index.remove(x)
					#remove correct word from remaining scrambled words in splitShuffle list
					splitShuffle.remove(splitInput[x])
				else:
					errors += 1

		os.system('clear')

		print(score.format(errors, len(solution_index)))

		#print list of shuffled words in verse
		print(' '.join(str(x) for x in splitShuffle))
		#print('\n')

		#display solution (appears like hangman)
		print(' '.join(str(x) for x in solution))
	#end While
	print("\nPerfect! Scripture completed (: ")

# return list

list = start()
practiceScripture(0, list)
# size = addScripture(1, list)
# printList(size, list)
# size = addScripture(size, list)
# printList(size, list)