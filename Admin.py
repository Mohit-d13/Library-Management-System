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
    
#---------------------------------------------------------------------------------------------------------         

def get_admin(AdminID):
    try:
        mycursor.execute('SELECT adminID FROM adminRecords WHERE adminID=%s',(AdminID,))
        valid_name = mycursor.fetchone()
        if valid_name:
            return True

    except pymysql.err.OperationalError as e:
        print(f"Failed to connect to database....Connection Error: {e}")
    
    return False   

#-------------------------------------------------------------------------------------------------------------

def insertAdmin():
    while True:
        try:
            AdminID=input(" Enter AdminID: ")
            Password=input(" Enter Password to be set: ")
            
            if not AdminID or not Password:
                raise ValueError("\n AdminID or Password cannot be empty")
            
            if get_admin(AdminID):
                ch=input("\nAdministrator ID already taken. Please choose a different AdminID!....\nOr Type 'No' to exit to Main Menu: ")
                if ch.lower() in ('no', 'n'):
                    break
                continue
            
            mycursor.execute('INSERT INTO adminRecords VALUES(%s, %s)',(AdminID,Password))
            mydb.commit()
            print("\n Administrator added sucessfully")

            ch=input("\n Do you wish to do add more Administrators?[Yes/No] : ")
            if ch.lower() in ('no', 'n'):
                break
        
        except ValueError as e:
            print(f"Error: {e}")    
        except pymysql.Error as error:
            print(f"Failed to add Administrator in 'AdminRecords': {error}")
            break
                        
#---------------------------------------------------------------------------------------------------------         

def deleteAdmin():
    while True:
        try:
            AdminID=input(" Enter AdminID whose details to be deleted : ")
            
            if not AdminID:
                raise ValueError("AdminID cannot be empty")
  
            if not get_admin(AdminID):
                ch=input("\n Entered Adminstrator ID does not exists. Please Enter a correct one!....\nOr Type 'No' to exit to Main Menu: ")
                if ch.lower() in ('no', 'n'):
                    break
                continue
            
            mycursor.execute('DELETE FROM adminRecords WHERE adminID=%s',(AdminID,))
            mydb.commit()
            print("\n Administrator deleted sucessfully")
            
            ch=input("Do you wish to delete more Administrators?[Yes/No] : ")
            if ch.lower() in ('no', 'n'):
                break
        
        except ValueError as e:
            print(f"Error: {e}")
        except pymysql.Error as error:
            print(f"Failed to delete Administrator from 'AdminRecords': {error}")
            break
            
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
                    print()
                    print("******************************","Searched Admin Record","******************************")
                    print("\t             AdminID: ", rows[0])
                    print("\t            Password: ", rows[1])
            else:
                print("Search Unsuccessfull")
                
            ch=input("\n Do you wish to Search more Administrators?[Yes/No] : ")
            if ch.lower() in ('no', 'n'):
                break
        
        except pymysql.Error as error:
            print(f"Failed to load AdminID from 'Admin Records': {error}")
            break
            
    return
#--------------------------------------------------------------------------------------------------------- 
def updateAdmin():
    while True:
        try:
            AdminID=input(" Enter Admin ID for whose details need to be updated : ")
            Password=input(" Enter new Password : ")
            
            if not AdminID or not Password:
                raise ValueError("AdminID or Password cannot be empty")
            
            if not get_admin(AdminID):
                ch=input("\nEntered Adminstrator ID does not exists. Please Enter a correct one!....\nOr Type 'No' to exit to Main Menu: ")
                if ch.lower() in ('no', 'n'):
                    break
                continue
            
            mycursor.execute('UPDATE adminRecords SET password=%s WHERE adminID=%s',(Password,AdminID))
            mydb.commit()
            print("Administrator record updated sucessfully.")
            
            ch=input("Do you wish to Search more Administrators?[Yes/No] : ")
            if ch.lower() in ('no', 'n'):
                break
        
        except ValueError as e:
            print(f"Error: {e}")
        except pymysql.Error as error:
            print(f"Failed to update 'Admin Records': {error}")
            break
            
    return
#--------------------------------------------------------------------------------------------------------- 
mydb=pymysql.connect(host="localhost",user="root",passwd="-@Z5qDk:",database="library")
mycursor=mydb.cursor()
     
