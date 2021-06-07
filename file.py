class Book:
    def __init__(self, title=None):
        self.title=title
    def __str__(self):
        book_title = "Title of Book:\t\t\t{}\n".format(self.title)
        return book_title
    def getTitle(self):
        return self.title
    def setTitle (self, title):
        self.title = title
class Library(Book):
    number = 0
    @classmethod
    def numberField(cls):
        cls.number = cls.number + 1
    def __init__(self, title=None,Lib_id=None):
        super().__init__(self)
        self.title = title
        self.lib_id= Lib_id
        self.bookId= "B" + str(self.number)
        self.numberField()
    def getBookID(self):
        return self.bookId
    def setID(self, bookId, title, Lib_id):
        self.title =Lib_id
        self.bookId = bookId

    def __str__(self):
        bookInfo = "Title Of Book:\t\t\t{}\n".format(self.title)
        bookInfo +=  "Library ID:\t\t\t{}\n".format(self.lib_id)
        bookInfo += "Book Count Value:\t\t\t{}\n".format(self.bookId)
        return bookInfo

def main():
    Library_book1 = Library("Much Ado About Nothing", "MD1234")
    Library_book2 = Library("King Lear", "KL12345")
    Library_book3 = Library("Hamilton", "H012345")
    print(Library_book1)
    print(Library_book2)
    print(Library_book3)
if __name__ == '__main__':
    main()

