#Class for Scripture: contains book, address, and text of each verse
class Memory_Verse:
	def __init__(self, book, address, verse):
		self.book = book
		self.address = address
		self.verse = verse

	def myfunc(self):
		print("This verse is in " + self.book)
		txt = "The address of this verse is {}:{}"
		print(txt.format(self.address[0], self.address[1]))
		print(self.verse)
		print

def start():
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

start()