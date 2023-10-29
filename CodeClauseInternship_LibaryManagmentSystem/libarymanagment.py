class Library:
  def __init__(self):
    self.noBooks = 0
    self.books = []
    
  def addBook(self, book):
    self.books.append(book)
    self.noBooks = len(self.books)

  def showInfo(self):
    print(f"The library has {self.noBooks} books. The books are:-")
    for book in self.books:
      print(book)


l1 = Library()
l1.addBook("**Think and Grow Rich**")
l1.addBook("**Rich Dad Poor Dad**")
l1.addBook("**Life's Amazing Secret**")
l1.addBook("**The Power of a Positive Attitude**")
l1.addBook("**Be a Winner**")
l1.showInfo()
    
  