books =[
    "The Alchemist",
    "Subhash Chandra Bose: The Mystery ",
    "Rich Dad Poor Dad",
    "Harry Potter",
    "The Great Gatsby",
    "Romeo and Juliet",
    "Art of staying silent",
    "Think and Grow Rich",
    "The laws of Human Nature"
]
while True:
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Exit") 
    
    choice = input("choice: ")
    
    if choice == "1":
        book = input("Book Name: ")
        books.append(book)
        print("Book added")
        
    elif choice == "2":
        print(" Available Books:")
        for book in books:
            print("*", book)
            
    elif choice == "3":
        name = input(" Enter book name you need:")
        if name in books:
            print("Book Found")
        else:
            print("Book not Found")
            
    elif choice == "4":
        name = input("Enter Book Name to Issue:")
        
        if name in books:
            books.remove(name)
            print("Book Issued Succesfully")
        else:
            print("Book not Available")
            
    elif choice == "5":
        print("Thank You for visiting Library!")
        break
             