print("Simple Library Management System")

book_list = []
def library_management():
   while True:
    user_choice = int(input("\n\n\n\n\n 1.add book \n 2.delete book \n3.list book \n4.exit \n Enter your choice 1-4:"))
    if user_choice == 1:
        print("add your book")
        book_name = input(":")
        book_list.append(book_name)
    elif user_choice == 2:
     print("Enter your book name\n")
     book_name - input(":")
     book_list.remove(book_name)
    elif user_choice == 3:
       print(book_list)
    elif user_choice == 4:
       print("Thanks for using ")
       break
library_management()

print("Thanks for using simple library management system take love from mahatab :3")