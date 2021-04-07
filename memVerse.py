

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