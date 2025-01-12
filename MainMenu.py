import Operations
def Adminmenu() :
    while True:
        print("\t\t\t Admin Menu \n")
        print("==============================================================")
        print("1. Book Management")
        print("2. User Management")
        print("3. Admin management")
        print("4. User Feedback and Ratings Table")
        print("5. Logout ")
        print("===============================================================")
        try:
            choice=int(input("Enter Choice between 1 to 5-------> : "))
            if 1 <= choice <= 5:
                if choice==1:
                    Operations.BookManagement()
                elif choice==2:
                    Operations.UserManagement()
                elif choice==3:
                    Operations.AdminManagement()
                elif choice==4:
                    Operations.FeedbackTable()
                elif choice==5:
                    print("Thanks for visiting our Library:))")
                    print("Logged out of the system")
                    break
            else:
                raise ValueError
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 5.")
    

def Usermenu() :
    while True:
        print("\t\t\t User Menu \n")
        print("==============================================================")
        print("1. Book Centre")
        print("2. Feedback and Ratings")
        print("3. Logout ")
        print("===============================================================")
        try:
            choice=int(input("Enter Choice between 1 to 3-------> : "))
            if 1 <= choice <= 3:
                if choice==1:
                    Operations.BookCentre()
                elif choice==2:
                    Operations.Feedback()
                elif choice==3:
                    print("Thanks for visiting our Library:))")
                    print("Logged out of the system")
                    break
            else:
                raise ValueError
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 3")
            
            
   
