import sys
import MainMenu
import Tables
import pymysql
#---------------------------------------------------------------------------------------------------------
def login_to_admin() : # Admin Login
    print("\n")
    print("|                       ~~  T  H  E    B  O  O  K    W  O  R  M  ~~                   |")
    print()
    print("                              LOGIN  TO YOUR ACCOUNT                                    \n")
    print("WARNING : Only three Attempts to login")
    for attempts in range(0,3) : # Only three Attempts to login then system will switch off 
        AdminID=input("\t  Enter AdminID : ")   #Original Admins:Kunal1020 -->123, Siddesh510 --> 786 ,Vishal305---> 675
        password=input("\t  Enter Password : ")
        
        print()
        mycursor.execute("SELECT password from adminRecords where adminID={0}".format("\'"+AdminID+"\'"))
        result=mycursor.fetchone()
        if result:
            temp,=result #coverting tuple to integer for comparing password
            if temp==password: # authenticated usernames and passwords
                print("\n\t\t    WELCOME {0} to THE BOOK WORM  \n ".format("\'"+AdminID+"\'"))
                MainMenu.Adminmenu()
                break
            else :
                print("\t INVALID PASSWORD OR USERNAME ! TRY AGAIN ")
                print("\t {0}st attempt is over \n ".format(attempts + 1))
                continue

        else :
            print("\t NO SUCH USERNAME ! TRY AGAIN ")
            print("\t {0}st attempt is over \n ".format(attempts + 1))
            continue

    else :
        print("\t Try again later \n ")
        print("\t System off  \n ")
        print("*---------------------------------------------------------------------------------* \n")
#---------------------------------------------------------------------------------------------------------
def login_to_user(): #User login
    
    print("\n")
    print("|                       ~~  T  H  E    B  O  O  K    W  O  R  M  ~~                   |")
    print()
    print("1.CREATE ACCOUNT")
    print("2.LOGIN TO YOUR ACCOUNT")
    ch=int(input("Enter choice-->"))
    if ch==1:
        data=()
        UserName=input("Enter your Name ")
        Password=input("Enter Password to be set:")
        data=(UserName, Password, None)
        query="INSERT INTO userRecords VALUES (%s, %s, %s)"
        mycursor.execute(query,data)
        mydb.commit()
        mycursor.execute("SELECT userName from userRecords where userName={0}".format("\'"+UserName+"\'"))
        result=mycursor.fetchone()
        if result:
            print("Account successfully created")
        else:
            print("Account already Exists")
        login_to_user()

    elif ch==2:
        print("WARNING : Only three Attempts to login at a time")
        for attempts in range(0,3) :  # Only three Attempts to login then system will switch off 
            UserName=input("\t  Enter UserID : ")   # Default Users:Kunal- UserID 101 and Passwd 1234,
                                                    #Vishal- UserID 102 and Passwd 3050,Siddhesh- UserID 103 and Passwd 5010
            password=input("\t  Enter Password : ")
            print()
            mycursor.execute("SELECT password from userRecords where userName={0}".format("\'"+UserName+"\'"))
            result=mycursor.fetchone()
            if result:
                temp,=result #coverting tuple to integer fro comparing password
                if temp==password: # authenticated usernames and passwords
                    print("\n\t\t    WELCOME {0} to THE BOOK WORM  \n ".format("\'"+UserName+"\'"))
                    MainMenu.Usermenu()
                    break
                else :
                    print("\t INVALID PASSWORD OR USERNAME ! TRY AGAIN ")
                    print("\t {0}st attempt is over \n ".format(attempts + 1))
                    continue

            else :
                print("\t NO SUCH USERNAME ! TRY AGAIN ")
                print("\t {0}st attempt is over \n ".format(attempts + 1))
                continue

        else :
            print("\t Try again later \n ")
            print("\t System off  \n ")
            print("*---------------------------------------------------------------------------------* \n")
    else:
        print("Enter valid choice")
        login_to_user()
#---------------------------------------------------------------------------------------------------------       
def menu() :
    print("\n\n")
    print("|*************************************************************************************|")
    print("|                       ~~  T  H  E    B  O  O  K    W  O  R  M  ~~                   |")
    print("|*************************************************************************************|")
    print("\n")
    print("                 ======================= MENU =======================                \n")
    print(" 1. Login as a ADMIN")
    print(" 2. Login as a USER")
    print(" 3. EXIT \n\n ") #exit

    while True :
        ch= input(" Select [ 1/2/3 ] : ")
        print()
        if ch== "1" :
            login_to_admin()
            break
        elif ch== "2" :
            login_to_user()
            break
        elif ch== "3" :
            cancel_request = input(" DO YOU WISH TO EXIT... [yes/no ] :  ")
            if cancel_request.lower() in ['yes','y'] :
                sys.exit()
            break
        else :
            print(" INVALID COMMAND ")
            print(" RETRY \n")
            continue
#--------------------------------------------------------------------------------------------------------- 
mydb=pymysql.connect(host="localhost",user="root",passwd="-@Z5qDk:",database="library")
mycursor=mydb.cursor()

if __name__ == "__main__":
    menu()
