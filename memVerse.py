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


# return list

list = start()
size = addScripture(1, list)
for x in range(0, size):
        list[x].myfunc()
size = addScripture(size, list)
for x in range(0, size):
        list[x].myfunc()