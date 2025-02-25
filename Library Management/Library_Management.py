import os

def explore_donate(path, idbk):
    while True:
        try:
            id = int(input("\nEnter Book ID number: "))
            if str(id) in idbk:
                print(f"Book ID already taken by: {idbk[str(id)]}\n")
                continue
            if id <= 0:
                print("\nID number cannot be negative!!")
                continue
        except ValueError:
            print("\nInvalid Input!! Please type a valid ID number...")
            continue
        break 

    name = input("Enter Book Name: ").title().strip()
    author = input("Enter the author of Book: ").title().strip()

    with open(path, "a") as file:
        file.write(f'\n{id}\t{name}\tby {author}')
    
    print("\nBook added to library successfully!\n")

def explore_display(path):
    print("\nID\tBook Title\t\tAuthor")
    print("-------------------------------------------")
    with open(path, "r") as file:
        for line in file:
            print(line.strip())
            print('\n')

def login(idst, library_file, path1):
    while True:
        try:
            idss = int(input("\nEnter your ID number: "))
            if idss <= 0:
                print("\nID number cannot be negative!!")
                continue
            elif str(idss) in idst:
                pasw = input("Enter your Password: ")
                if pasw == idst[str(idss)]:
                    user = f"{idss}.txt"
                    path = os.path.join(library_file, user)
                    print("\nLogin Successful!!\nWelcome back, reader!!")
                    return path
                else:
                    print("Incorrect password!!\n")
                    continue
            else:
                print("\nWelcome to the Library!\nNew user registration:")
                name = input("\nEnter Your Name: ")
                pasw = input("Create your Password: ")
                print("\nAccount created successfully!\nLogin with same account for future accessings!!\n")

                idst[str(idss)] = pasw
                with open(path1, "a") as fl:
                    fl.write(f"\n{idss}\t{name}\t{pasw}")

                user = f"{idss}.txt"
                pathn = os.path.join(library_file, user)
                with open(pathn, "w") as file:
                    file.write("")
                return pathn
        except ValueError:
            print("\nInvalid Input!! Please type a valid ID number...")

def issue(idbk, npath, path):
    while True:
        try:
            bookid = int(input("Enter Book ID: "))
            if bookid <= 0:
                print("Book ID cannot be negative.")
                continue
            elif str(bookid) in idbk:
                print(f"Issuing book: {idbk[str(bookid)]}")
                
                lines_to_keep = []
                deleted_line = None
                
                with open(path, "r") as file:
                    for line in file:
                        parts = line.strip().split("\t")
                        if parts[0] == str(bookid):
                            deleted_line = line
                        else:
                            lines_to_keep.append(line)
                
                if deleted_line:
                    with open(path, "w") as file:
                        file.writelines(lines_to_keep)

                    with open(npath, "a") as fil1:
                        fil1.write(deleted_line.strip() + "\n")

                    print("Book issued successfully!\n")
                else:
                    print("Book not found!")
            else:
                print("\nBook not available.\nCheck for available books (0)")
            return
        except ValueError:
            print("Enter a valid Book ID...")

def rtrn(idbk, npath, path):
    while True:
        try:
            bookid = int(input("Enter Book ID: "))
            if bookid <= 0:
                print("Book ID cannot be negative or zero.")
                continue  

            found = False  
            lines_to_keep = []  
            deleted_line = None  

            with open(npath, "r") as file:
                for line in file:
                    parts = line.strip().split("\t")
                    if parts[0] == str(bookid):
                        deleted_line = line
                        found = True
                        print(f"Returning book: {parts[1]}, {parts[2]}\n")
                    else:
                        lines_to_keep.append(line)

            if found:
                with open(npath, "w") as file:
                    file.writelines(lines_to_keep)

                with open(path, "a") as file:
                    file.write(deleted_line.strip() + "\n")

                print("Book returned successfully!\n")
                return 
            print("\nBook not available.\nCheck for available books (0)")
            return
        except ValueError:
            print("Enter a valid Book ID...")

def main():
    print("\nWelcome to Kirthan's Library Management Project!!")
    idbk = {}
    idst = {}
    library_file = "Library"
    books = "Books.txt"
    reader = "Readers.txt"

    path = os.path.join(library_file, books)
    path1 = os.path.join(library_file, reader)

    if not os.path.exists(library_file):
        os.makedirs(library_file)
        with open(path, "w") as file:
            file.write(
'''121\tHarry Potter Series\tby J.K. Rowling
232\tThe Lord of the Rings\tby J.R.R. Tolkien
153\tThe Diary of a Young Girl\tby Anne Frank
423\tA Brief History of Time\tby Stephen Hawking
215\tThinking, Fast and Slow\tby Daniel Kahneman
126\tThe Great Gatsby\tby F. Scott 
786\tWings of Fire\tby Dr. APJ Abdul Kalam''')
        with open(path1, "w") as file:
            file.write('Reader_ID\tName\tPassword')

    while True:
        with open(path, "r") as file:
            for line in file:
                idl, title, author = line.strip().split("\t")
                idbk[idl] = (title, author)

        with open(path1, "r") as file:
            for line in file:
                stid, name, pas = line.strip().split("\t")
                idst[stid] = pas

        print("\nLibrary Management:\n")
        print("0. Librarian Access")
        print("1. Explore library")
        print("2. Login as Reader")
        print("3. Quit")
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            while True:
                print("\n1. Display Available Books")
                print("2. Donate New Book")
                print("3. Return to Main Menu")
                choice1 = input("\nEnter your choice: ").strip()

                if choice1 == "1":
                    explore_display(path)
                elif choice1 == "2":
                    explore_donate(path, idbk)
                elif choice1 == "3":
                    break
                else:
                    print("Invalid Input")
        
        elif choice == "2":
            npath = login(idst, library_file, path1)
            while True:
                print("\n0.Display available books\n1. Issue a Book\n2. Return a Book\n3. Your Issued Books\n4. Logout")
                choice2 = input("Enter your choice: ").strip()
                if choice2 == "1":
                    issue(idbk, npath, path)
                elif choice2 == "2":
                    rtrn(idbk, npath, path)
                elif choice2 == "3":
                    explore_display(npath)
                elif choice2 == "0":
                    explore_display(path)
                elif choice2 == "4":
                    break

        elif choice == "0":
            print("List of all Readers of Library!!\n")
            with open(path1, "r") as fl:
                for l in fl:
                    print(f"{l}\n")
 
        elif choice == "3":
            print("\nThank you!!\nVisit Library Frequently!!!\n\nA library is the delivery room for the birth of ideas, a place where history comes to life.\n\t\t\t\t — Norman Cousins")
            break
        else:
            print("Invalid Input!!")

main()
