import pymysql
import Tables
#---------------------------------------------------------------------------------------------------------                 
def displayAdmin():
    
    print()
    print("Admin Records: \n")
    
    try:
        mycursor.execute("SELECT * FROM adminRecords")
        records=mycursor.fetchall()
        
        if records:
            row_no=0
            for rows in records :
                row_no+=1
                print("******************************","Row no.",row_no,"******************************")
                print("\t             AdminID: ", rows[0])
                print("\t            Password: ", rows[1])
                print()
        else:
            print("No Admin Records found.")
            
    except pymysql.Error as error:
        print(f"Failed to display 'Admin Records' : {error}")
    
    input("Press Enter to continue")
    
    return
#---------------------------------------------------------------------------------------------------------         
def insertAdmin():
    while True:
        try:
            AdminID=input("Enter AdminID: ")
            Password=input(" Enter Password to be set: ")
            
            if not AdminID or not Password:
                raise ValueError("AdminID or Password cannot be empty")
            
            check_query="SELECT adminID FROM adminRecords WHERE adminID=%s"
            mycursor.execute(check_query,(AdminID,))
            existing_user = mycursor.fetchone()
            
            if existing_user:
                print("Administrator ID already taken. Please choose a different AdminID!..")
                continue
            
            data=(AdminID,Password)
            query="INSERT INTO adminRecords VALUES (%s, %s)"
            mycursor.execute(query,data)
            mydb.commit()
            print("Administrator added sucessfully")

            ch=input("Do you wish to do add more Administrators?[Yes/No] : ")
            if ch.lower() in ('no', 'n'):
                break
        
        except ValueError as e:
            print(f"Error: {e}")    
        except pymysql.Error as error:
            print(f"Failed to add Administrator in 'AdminRecords': {error}")
            
            
#---------------------------------------------------------------------------------------------------------         
def deleteAdmin():
    while True:
        try:
            AdminID=input(" Enter AdminID whose details to be deleted : ")
  
            check_query="SELECT adminID FROM adminRecords WHERE adminID=%s"
            mycursor.execute(check_query, (AdminID,))
            valid_name=mycursor.fetchone()
            
            if not valid_name:
                print("Entered Administrator ID is not found. Please enter a different one!...")
                continue
            
            delete_query="DELETE FORM adminRecords WHERE adminID=%s"
            mycursor.execute(delete_query,(AdminID,))
            mydb.commit()
            print("Administrator deleted sucessfully")
            
            ch=input("Do you wish to delete more Administrators?[Yes/No] : ")
            if ch.lower() in ('no', 'n'):
                break
        
        except ValueError as e:
            print(f"Error: {e}")
        except pymysql.Error as error:
            print(f"Failed to delete Administrator from 'AdminRecords': {error}")
            
    return
#---------------------------------------------------------------------------------------------------------     
def searchAdmin():
    while True:
        try:
            Search=input(" Enter AdminID to be Searched: ")  
            mycursor.execute("SELECT * FROM adminRecords where adminID={0}".format("\'"+Search+"\'"))
            records=mycursor.fetchall()
            row_no=0
            
            if records:
                for rows in records :
                    row_no+=1
                    print("******************************","Searched Admin Record","******************************")
                    print("\t             AdminID: ", rows[0])
                    print("\t            Password: ", rows[1])
                    print()
            else:
                print("Search Unsuccesfull")
                
            ch=input("Do you wish to Search more Administrators?[Yes/No] : ")
            if ch.lower() in ('no', 'n'):
                break
        
        except pymysql.Error as error:
            print(f"Failed to load AdminID from 'Admin Records': {error}")
            
    return
#--------------------------------------------------------------------------------------------------------- 
def updateAdmin():
    while True:
        try:
            AdminID=input(" Enter Admin ID for whose details need to be updated : ")
            Password=input(" Enter new Password : ")
            
            if not AdminID or not Password:
                raise ValueError("AdminID or Password cannot be empty")
            
            check_query="SELECT adminID FROM adminRecords WHERE adminID=%s"
            mycursor.execute(check_query, (AdminID,))
            valid_name=mycursor.fetchone()
            
            if not valid_name:
                print("Entered Administrator ID does not exists. Please enter a different one!...")
                continue
            
            query="UPDATE adminRecords SET password = %s WHERE adminID=%s"
            data=(Password,AdminID)
            mycursor.execute(query,data)
            mydb.commit()
            print("Administrator record updated sucessfully.")
            
            ch=input("Do you wish to Search more Administrators?[Yes/No] : ")
            if ch.lower() in ('no', 'n'):
                break
        
        except ValueError as e:
            print(f"Error: {e}")
        except pymysql.Error as error:
            print(f"Failed to update 'Admin Records': {error}")
            
    return
#--------------------------------------------------------------------------------------------------------- 
mydb=pymysql.connect(host="localhost",user="root",passwd="-@Z5qDk:",database="library")
mycursor=mydb.cursor()
     
