class Book():
    def __init__(self,id,title,author):
        self.id = id
        self.title = title
        self.author = author
    def display(self):
        print(self.id,self.title,self.author)
class library():
    def __init__(self):
        self.books = {}
        self.borrowed = {}
    def display(self):
        if len(self.books) == 0:
            print("no book available")
            return

        print('\n all books')
        for i in self.books.values():
            if i.id in self.borrowed:
                print(i.id,i.title,i.author,"borrowed")
            else:
                print(i.id,i.title,i.author,"available")
    def search(self):
        search = input("enter author ").lower()
        found = 0

        for x in self.books.values():
            if search in x.title.lower() or search in x.author.lower():
                if x.id in self.borrowed:
                    print(x.id,x.title,x.author,"borrowed")
                else:
                     print(x.id,x.title,x.author,"available")
                found = True
        if not found:
            print("book not found")
    def borrow(self):
        id = input("enter book id to borrow")
        if id not in self.books:
            print("book not found")
            
        elif id in self.borrowed:
            print("book borrowed")
        else:
            name = input("enter your name")
            student_id = input("enter your id")
            self.borrowed[id] = {"name":name,"student_id":student_id}
            print("book borrowed")

    def Return(self):
        id = input("enter book id to return: ")
        if id not in self.books:
            print("book not found")
        elif id not in self.borrowed:
            print("book already available")
        else:
            del self.borrowed[id]
            print("book returned")

def main():
    librar = library()
    librar.books["101"] = Book("101","The Hobbit","J.R.R Tolkien")
    librar.books["102"] = Book("102","1984","George Orwell")
    librar.books["103"] = Book("103","Harry Potter","J.K Rowling")
    librar.books["104"] = Book("104","Wings of Fire","APJ Abdul Kalam")
    librar.books["105"] = Book("105","INDIA 2020","APJ Abdul Kalam")

    while True:
        print("\n Library Management")
        print("1.Display books")
        print("2.Search book")
        print("3.Borrow book")
        print("4.Return book")
        print("5.Exit")

        choice = int(input("enter your choice"))
        if choice == 1:
            librar.display()
        elif choice == 2:
            librar.search()
        elif choice == 3:
            librar.borrow()
        elif choice == 4:
            librar.Return()
        elif choice == 5:
            print("thank you")
            break
        else:
            print("invalid choice")

if __name__ == '__main__':
    main()
          
