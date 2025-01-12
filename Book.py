import pymysql
import Tables
from User import get_user

#----------------------------------------------------------------------------------------
#Admin Operation on Books
def displayBook():
    
    print()
    print("Book Records: \n")    
    try:
        mycursor.execute(
            """
            SELECT
                bookRecords.bookID,
                bookRecords.bookName,
                bookRecords.author,
                bookRecords.publisher,
                userRecords.userName
            FROM 
                bookRecords
            LEFT JOIN 
                userRecords ON bookRecords.bookID=userRecords.bookID
            """
            )
        records=mycursor.fetchall()
        row_no=0
        
        if records:
            for rows in records :
                row_no+=1
                print("******************************","Row no.",row_no,"******************************")
                print("\t             BookID: ", rows[0])
                print("\t           BookName: ", rows[1])
                print("\t             Author: ", rows[2])
                print("\t          Publisher: ", rows[3])
                print("\t          Issued By: ", rows[4])
                print()
        else:
            print("No Book Records found.")
            
    except pymysql.Error as error:
        print(f"Failed to display 'Book records': {error}")
        
    input("Press Enter to return to the User Menu")    
    return

#----------------------------------------------------------------------------------------        

def get_book(BookID):
    try:
        mycursor.execute('SELECT bookID FROM bookRecords WHERE bookID=%s',(BookID,))
        valid_book = mycursor.fetchone()
        if valid_book:
            return True
    except pymysql.Error as e:
        print(f"Failed to execute query: {e}")
    return False

#-----------------------------------------------------------------------------------------

def insertBook():
    while True:
        try:
            BookID=input(" Enter BookID: ")
            BookName=input(" Enter Book Name: ")
            Author=input(" Enter Author Name: ")
            Publisher=input(" Enter Publisher Name: ")
            
            if not BookID or not BookName or not Author or not Publisher:
                raise ValueError("BookID, BookName, Author or Publisher cannot be empty")
            
            if get_book(BookID):
                ch=input("\n Book already exists in records. Please add a different Book!....\nOr Type 'No' to exit to Main Menu: ")
                if ch.lower() in ('no', 'n'):
                    break
                continue
            
            mycursor.execute('INSERT INTO bookRecords VALUES (%s, %s, %s, %s)',(BookID, BookName, Author, Publisher))
            mydb.commit()
            print("\n Book added sucessfully")
    
            ch=input("Do you wish to do add more Books?[Yes/No] : ")
            if ch.lower() in ('no', 'n'):
                break
            
        except ValueError as e:
            print(f"\n Error: {e}")
        except pymysql.Error as error:
            print(f"Failed to add new Book in 'BookRecords': {error}")
            break    
    return

#----------------------------------------------------------------------------------------        

def deleteBook():
    while True:
        try:
            BookID=input(" Enter BookID whose details to be deleted : ")
            
            if not BookID:
                raise ValueError("BookID cannot be empty")
            
            if not get_book(BookID):
                ch=input("\n Book does not exists in records. Please choose a different Book!....\nOr Type 'No' to exit to Main Menu: ")
                if ch.lower() in ('no', 'n'):
                    break
                continue
            
            mycursor.execute('DELETE FROM bookRecords WHERE bookID=%s',(BookID,))
            mydb.commit()
            print("\n Book deleted sucessfully")
            
            ch=input("\n Do you wish to do add more Books?[Yes/No] : ")
            if ch.lower() in ('no', 'n'):
                break
        except ValueError as e:
            print(f"\n Error: {e}")    
        except pymysql.Error as error:
            print(f"Failed to delete Book from 'BookRecords': {error}")
            break            
    return

#----------------------------------------------------------------------------------------    

def searchBook():
    while True:
        try:
            print()
            Search=input("Enter BookID to be Searched:")
            mycursor.execute("SELECT bookRecords.bookID,bookRecords.bookName,bookRecords.author,bookRecords.publisher,userRecords.userName\
                            FROM bookRecords\
                            LEFT JOIN userRecords ON bookRecords.bookID=userRecords.bookID\
                            WHERE bookRecords.bookID={0}".format("\'"+Search+"\'"))  
            records=mycursor.fetchall()
            row_no=0
            
            if records:
                for rows in records :
                    row_no+=1
                    print("******************************","Searched Book Record","******************************")
                    print("\t             BookID: ", rows[0])
                    print("\t           BookName: ", rows[1])
                    print("\t             Author: ", rows[2])
                    print("\t          Publisher: ", rows[3])
                    print("\t          Issued By: ", rows[4])
                    print()
            else:
                print("Search Unsuccesfull")
                
            ch=input("\n Do you wish to do add more Books?[Yes/No] : ")
            if ch.lower() in ('no', 'n'):
                break
              
        except pymysql.Error as error:
            print(f"Failed to load Book from 'BookRecords': {error}")            
    return

#----------------------------------------------------------------------------------------

def updateBook():
    while True:
        try:
            BookID=input(" Enter Book ID for whose details need to be updated : ")
            BookName=input(" Enter updated Book Name : ")
            Author=input(" Enter updated Author Name : ")
            Publisher=input(" Enter the updated Publisher Name : ")
            
            if not BookID or not BookName or not Author or not Publisher:
                raise ValueError("BookID, Bookname, Author or Publisher cannot be empty")
            
            if not get_book(BookID):
                ch=input("\n Book does not exists in records. Please choose a different Book!....\nOr Type 'No' to exit to Main Menu: ")
                if ch.lower() in ('no', 'n'):
                    break
                continue
            
            mycursor.execute('UPDATE bookRecords SET bookName=%s, Author=%s, Publisher=%s WHERE bookID=%s',(BookName, Author, Publisher, BookID))
            mydb.commit()
            print("Book's record updated succesfully")
            
            ch=input("\n Do you wish to do add more Books?[Yes/No] : ")
            if ch.lower() in ('no', 'n'):
                break
        
        except ValueError as e:
            print(f"\n Error: {e}")    
        except pymysql.Error as error:
            print(f"Failed to add new Book in 'BookRecords': {error}")
            break            
    return
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#User Operation on Books
def BookList():
    
    print()
    print("Book Records: \n")
    
    try:
        mycursor.execute('SELECT * from bookRecords')
        records=mycursor.fetchall()
        row_no=0
        
        if records:
            for rows in records :
                row_no+=1
                print("******************************","Row no.",row_no,"******************************")
                print("\t             BookID: ", rows[0])
                print("\t           BookName: ", rows[1])
                print("\t             Author: ", rows[2])
                print("\t          Publisher: ", rows[3])
                print()
        else:
            print("No Book Record found.")
    
    except pymysql.Error as error:
        print(f"Failed to display Book list from 'BookRecords': {error}")
        
    input("Press any key to return to the User Menu")    
    return
    
def IssueBook():
    try:
        UserName=input("Enter your Username:")
        
        if not UserName:
            raise ValueError("Username cannot be empty")
        
        if not get_user(UserName):
            print("Username does not exists. Please Enter a correct Username!...")
            input("Press any key to return to the User Menu")
            return
        
        mycursor.execute("Select bookID FROM userRecords WHERE userName={0}".format("\'"+UserName+"\'"))
        checking=mycursor.fetchone()
        
        if checking==(None,):
            print()
            print("Available Books: \n")
            mycursor.execute(
                """
                SELECT 
                    bookRecords.bookID,
                    bookRecords.bookName, 
                    bookRecords.author,
                    bookRecords.publisher,
                    userRecords.userName
                FROM 
                    bookRecords
                LEFT JOIN 
                    userRecords ON bookRecords.bookID=userRecords.bookID
                WHERE
                    userName IS NULL
                """
                )
            records=mycursor.fetchall()
            row_no=0
            
            if records:
                for rows in records:
                    row_no+=1
                    print("******************************","Row no.",row_no,"******************************")
                    print("\t             BookID: ", rows[0])
                    print("\t           BookName: ", rows[1])
                    print("\t             Author: ", rows[2])
                    print("\t          Publisher: ", rows[3])
                    print()
            else:
                print("Sorry, there are no available books in the Library")
                print("Please Wait for some time till someone return the book you want")
                input("Press any key to return to the User Menu")
                return
            
            data=()                             
            Issue=input("Enter a Book's BookID from the display above: ")
            
            if not Issue:
                raise ValueError("BookId cannot be empty")
            
            if not get_book(Issue):
                ch=input("\n INCORRECT BookID...Enter a correct BookID from display above!...\nOr Type 'No' to exit to User Menu: ")
                if ch.lower() in ['no', 'n']:
                    return              
            
            mycursor.execute(
                'UPDATE userRecords SET bookID=%s WHERE userName=%s',
                (Issue,UserName)
                )
            mydb.commit()
            print("\n Book Successfully Issued")
            
            input("Press any key to return to the User Menu")
            return
        else:
            print(f"\n Status: Book Already Issued to {UserName}, Please kindly return previously issued book.......")
            input("Press any key to return to the User Menu")
    
    except ValueError as e:
        print(f"Error: {e}")        
    except pymysql.Error as error:
        print(f"Failed to Issue Book from 'BookRecords': {error}")        
    return
    
#----------------------------------------------------------------------------------------

def ShowIssuedBook():
    try:
        print()
        UserName=input("Enter your Username:")
        
        if not UserName:
            raise ValueError("Username cannot be empty")
        
        mycursor.execute("SELECT userName, userRecords.bookID, bookName\
                        FROM library.userRecords INNER JOIN library.bookRecords\
                        ON bookRecords.bookID=userRecords.bookID\
                        WHERE userName={0}".format("\'"+UserName+"\'"))
        records=mycursor.fetchall()
        row_no=0
        if records:
            for rows in records :
                row_no+=1
                print()
                print("******************************","Issued Book","******************************")
                print("\t           UserName: ", rows[0])
                print("\t             BookID: ", rows[1])
                print("\t           BookName: ", rows[2])
            input("Press any key to return to the User Menu")
            return
        else:
            print("No Book Issued")
            input("Press Enter to return to the User Menu")
            
    except ValueError as e:
        print(f"\n Error: {e}")        
    except pymysql.Error as error:
        print(f"Failed to display issued books in 'Book Records': {error}")        
    return

#----------------------------------------------------------------------------------------

def returnBook():
    try:
        print()
        UserName=input("Enter your Username:")
        BookID=input("Enter BookID to be return:")
        
        if not UserName or not BookID:
            raise ValueError("Username or BookID cannot be empty")
        
        if not get_user(UserName):
            print("Username does not exists. Please Enter a correct Username!...")
            input()
            return
        
        mycursor.execute('SELECT bookID FROM userRecords WHERE userName=%s',(UserName,))
        valid_id = mycursor.fetchone()
        
        if valid_id==(BookID,):
            mycursor.execute(
                'UPDATE userRecords SET bookID=%s WHERE userName=%s AND bookID=%s',
                (None, UserName, BookID)
                )
            mydb.commit()
            print("Return Successfull")
        else:
            print(f"Entered BookID is INCORRECT or No Book is Issued to {UserName}.\n Please Enter a correct BookID or First check if any book is issued to {UserName}")
            input("Press Enter to return to the User Menu")
        
    
    except ValueError as e:
        print(f"Error: {e}")        
    except pymysql.Error as error:
        print(f"Failed to return Issued Book from 'BookRecords': {error}")        
    return
   
#------------------------------------------------------------------------------------------
mydb=pymysql.connect(host="localhost",user="root",passwd="-@Z5qDk:",database="library")
mycursor=mydb.cursor()
