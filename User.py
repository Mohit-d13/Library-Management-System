import pymysql
import Tables
        
#--------------------------------------------------------------------------------------------------------------------------------        
def displayUser():
    
    print()
    print("User Records: \n")
    
    try:
        mycursor.execute(
            """
            SELECT 
                userRecords.userName,
                userRecords.password,
                bookRecords.bookName,
                bookRecords.bookID
            FROM 
                userRecords
            LEFT JOIN 
                bookRecords ON userRecords.bookID=bookRecords.bookID
            """
            )
    
        records=mycursor.fetchall()
    
        if records:
            row_no=0
            for rows in records:
                row_no+=1
                print("******************************","Row no.",row_no,"******************************")
                print("\t           UserName: ", rows[0])
                print("\t           Password: ", rows[1])
                print("\t        Book Issued: ", rows[2])
                print("\t         Its BookID: ", rows[3])
                print()
        else:
            print("No User Records found.")
            
    except pymysql.Error as error:
        print(f"Failed to display User Records: {error}")
        
    input("Press any key to return to the User Menu")
        
    return
#--------------------------------------------------------------------------------------------------------------------------------             
def insertUser():
    while True:
        try:
            UserName=input(" Enter Username: ")
            Password=input(" Enter Password to be Set: ")
            
            if not UserName or not Password:
                raise ValueError("Username or Password cannot be empty")
            
            check_query="SELECT userName FROM userRecords WHERE userName=%s"
            mycursor.execute(check_query,(UserName,))
            existing_user = mycursor.fetchone()
            
            if existing_user:
                print("Username is already taken. Please choose a different username!..")
                continue
            
            data=(UserName, Password, None)
            query="INSERT INTO userRecords VALUES (%s, %s, %s)"
            mycursor.execute(query,data)
            mydb.commit()
            print("User added sucessfully")
        
            ch=input("Do you wish to do add more Users?[Yes/No] : ")
            if ch.lower() in ('no', 'n'):
                break
            
        except ValueError as e:
            print(f"Error: {e}")
        except pymysql.Error as error:
            print(f"Failed to add User in 'User Records': {error}")
            
    return

#--------------------------------------------------------------------------------------------------------------------------------             
def deleteUser():
    while True:
        try:
            print()
            Username=input(" Enter Username whose details to be deleted : ")  
            query="DELETE FROM userRecords WHERE userName=%s"
            mycursor.execute(query,(Username,))
            valid_name = mycursor.fetchone()
            
            if not valid_name:
                print("Entered username does not exists. Please try again!....")
                continue
            
            mydb.commit()
            print("User deleted sucessfully")
            
            ch=input("Do you wish to delete more Users?[Yes/No] : ")
            if ch.lower() in ('no','n'):
                break
            
        except pymysql.Error as error:
            print(f"Failed to delete User from 'User Records': {error}")
            
    return
#--------------------------------------------------------------------------------------------------------------------------------         
def searchUser():
    while True:
        try:
            print()
            Search=input(" Enter Username to be Searched: ")  
            mycursor.execute("SELECT userName, password , bookName, userRecords.bookID\
                        FROM library.userRecords LEFT JOIN library.bookRecords\
                        ON bookRecords.bookID=userRecords.bookID\
                        WHERE userRecords.userName={0}".format("\'"+Search+"\'"))
            records=mycursor.fetchall()
            row_no=0
            if records:
                for rows in records :
                    row_no+=1
                    print("******************************","Searched User Record","******************************")
                    print("\t           UserName: ", rows[0])
                    print("\t           Password: ", rows[1])
                    print("\t        Book Issued: ", rows[2])
                    print("\t         Its BookID: ", rows[3])
                    print()
            else:
                print("Search Unsuccesfull")
                
            ch=input("Do you wish to Search more Users?[Yes/No] : ")
            if ch.lower() in ('no','n'):
                break
            
        except pymysql.Error as error:
            print(f"Failed to load User from 'User Records': {error}")
            
    return
#--------------------------------------------------------------------------------------------------------------------------------     
def updateUser():
    while True:
        try:
            UserName=input(" Enter Username: ")
            Password=input(" Enter Password to be Set: ")
            
            if not UserName or not Password:
                raise ValueError("Username or Password cannot be empty")
            
            check_query="SELECT userName FROM userRecords WHERE userName=%s"
            mycursor.execute(check_query,(UserName,))
            existing_user = mycursor.fetchone()
            
            if existing_user:
                print("Username does not exists. Please try a different username!..")
                continue
            
            update_query="UPDATE userRecords SET password=%s WHERE userName=%s"
            data=(Password, UserName)
            mycursor.execute(update_query,data)
            mydb.commit()
            print("User updated sucessfully")
        
            ch=input("Do you wish to do add more Users?[Yes/No] : ")
            if ch.lower() in ('no', 'n'):
                break
            
        except ValueError as e:
            print(f"Error: {e}")
        except pymysql.Error as error:
            print(f"Failed to add User in 'User Records': {error}")
            
    return  
#--------------------------------------------------------------------------------------------------------------------------------     
mydb=pymysql.connect(host="localhost",user="root",passwd="-@Z5qDk:",database="library")
mycursor=mydb.cursor()

        
