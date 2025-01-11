import pymysql
import Tables
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
def insertBook():
    while True:
        try:
            BookID=input(" Enter BookID: ")
            BookName=input(" Enter Book Name: ")
            Author=input(" Enter Author Name: ")
            Publisher=input(" Enter Publisher Name: ")
            
            if not BookID or not BookName or not Author or not Publisher:
                raise ValueError("BookID, BookName, Author or Publisher cannot be empty")
            
            data=(BookID, BookName, Author, Publisher)
            query="INSERT INTO bookRecords VALUES (%s, %s, %s, %s)"
            mycursor.execute(query,data)
            mydb.commit()
            print("Book added sucessfully")
    
            ch=input("Do you wish to do add more Books?[Yes/No] : ")
            if ch.lower() in ('no', 'n'):
                break
            
        except ValueError as e:
            print(f"Error: {e}")
        except pymysql.Error as error:
            print(f"Failed to add new Book in 'BookRecords': {error}")
    
    return

#----------------------------------------------------------------------------------------        
def deleteBook():
    while True:
        try:
            BookID=input(" Enter BookID whose details to be deleted : ")
            
            check_query="SELECT bookID FROM bookRecords WHERE bookID=%s"
            mycursor.execute(check_query, (BookID,))
            valid_name=mycursor.fetchone()
            
            if not valid_name:
                print("Entered Book does not exists. Please enter a different one!...")
                continue
            
            delete_query="DELETE FROM bookRecords WHERE bookID=%s"
            mycursor.execute(delete_query,(BookID,))
            mydb.commit()
            print("Book deleted sucessfully")
            
            ch=input("Do you wish to do add more Books?[Yes/No] : ")
            if ch.lower() in ('no', 'n'):
                break
            
        except pymysql.Error as error:
            print(f"Failed to delete Book from 'BookRecords': {error}")
            
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
                
            ch=input("Do you wish to do add more Books?[Yes/No] : ")
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
            
            check_query="SELECT bookID FROM bookRecords WHERE bookID=%s"
            mycursor.execute(check_query, (BookID,))
            valid_name=mycursor.fetchone()
            
            if not valid_name:
                print("Entered Book does not exists. Please enter a different one!...")
                continue
            
            query="UPDATE bookRecords SET bookname = %s, Author = %s, Publisher = %s WHERE bookID = %s" 
            data=(BookName,Author,Publisher,BookID)
            mycursor.execute(query,data)
            mydb.commit()
            print("Book's record updated succesfully")
            
            ch=input("Do you wish to do add more Books?[Yes/No] : ")
            if ch.lower() in ('no', 'n'):
                break
            
        except pymysql.Error as error:
            print(f"Failed to add new Book in 'BookRecords': {error}")
            
    return
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#User Operation on Books
def BookList():
    
    print()
    print("Book Records: \n")
    
    try:
        mycursor.execute("""SELECT * from bookRecords""")
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
        username=input("Enter your Username:")
        
        if not username:
            raise ValueError("Username cannot be empty")
        
        mycursor.execute("Select bookID FROM userRecords WHERE userName={0}".format("\'"+username+"\'"))
        checking=mycursor.fetchone()
        
        if checking==(None,):
            print()
            print("Available Books: \n")
            mycursor.execute(
                """
                SELECT 
                    booksRecords.bookID,
                    booksRecords.bookName, 
                    booksRecords.author,
                    booksRecords.publisher,
                    userRecords.userName
                FROM 
                    booksRecords
                LEFT JOIN 
                    userRecords ON booksRecords.bookID=userRecords.bookID
                """
                )
            records=mycursor.fetchall()
            row_no=0
            
            if records:
                for rows in records:
                    if rows[5]==None:
                        
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
            Issue=input("Enter the BookID available to be issued:")
            
            if not Issue:
                raise ValueError("BookId cannot be empty")
            
            query="UPDATE userRecords SET bookID=%s WHERE userName = %s" 
            data=(Issue,username)
            mycursor.execute(query,data)
            mydb.commit()
            print("Book Successfully Issued")
            
            input("Press any key to return to the User Menu")
            return
        else:
            print("Book Already Issued, Kindly Return That first")
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
        username=input("Enter your Username:")
        mycursor.execute("SELECT userName, userRecords.bookID, bookName\
                        FROM library.userRecords INNER JOIN library.bookRecords\
                        ON bookRecords.bookID=userRecords.bookID\
                        WHERE userName={0}".format("\'"+username+"\'"))
        records=mycursor.fetchall()
        row_no=0
        if records:
            for rows in records :
                row_no+=1
                print("******************************","Issued Book","******************************")
                print("\t           UserName: ", rows[0])
                print("\t             BookID: ", rows[1])
                print("\t           BookName: ", rows[2])
                print()
            input("Press any key to return to the User Menu")
            return
        else:
            print("No Book Issued")
            input("Press Enter to return to the User Menu")
            
    except pymysql.Error as error:
        print(f"Failed to display issued books in 'Book Records': {error}")
        
    return
#----------------------------------------------------------------------------------------
def returnBook():
    try:
        print()
        data=()
        Username=input("Enter your Username:")
        Rec=input("Enter BookID to be return:")
        
        if not Username or not Rec:
            raise ValueError("Username or BookID cannot be empty")
        
        query="""UPDATE userRecords SET bookID = %s WHERE userName= %s and bookID=%s"""            
        data=(None,Username,Rec)
        mycursor.execute(query,data)
        mydb.commit()
        print("Return Successfull")
        input("Press Enter to return to the User Menu")
    
    except ValueError as e:
        print(f"Error: {e}")        
    except pymysql.Error as error:
        print(f"Failed to return Issue Book from 'BookRecords': {error}")
        
    return   
#----------------------------------------------------------------------------------------

mydb=pymysql.connect(host="localhost",user="root",passwd="-@Z5qDk:",database="library")
mycursor=mydb.cursor()
