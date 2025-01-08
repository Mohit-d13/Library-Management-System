import pymysql

mydb=pymysql.connect(host="localhost",user="root",passwd="-@Z5qDk:")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS library")
mycursor.execute("USE library")

try:
    mycursor.execute("SHOW TABLES LIKE 'bookRecords' ")
    result = mycursor.fetchone()
    
    if not result: 
        mycursor.execute(
            """
            CREATE TABLE bookRecords (
            bookID VARCHAR(10) PRIMARY KEY,
            bookName VARCHAR(35) NOT NULL,
            author VARCHAR(30) NOT NULL,
            publisher VARCHAR(30) NOT NULL
            )
            """
        )
            
except pymysql.Error as error:
    print(f"Failed to create table 'bookRecords': {error} ")
    
mydb.commit()    
     
     
try:
    mycursor.execute("SHOW TABLES LIKE 'userRecords' ")
    result=mycursor.fetchone()
    
    if not result:
        mycursor.execute(
            """
            CREATE TABLE IF NOT EXISTS userRecords(
            userName VARCHAR(20) PRIMARY KEY,
            password VARCHAR(20) NOT NULL, 
            bookID VARCHAR(10) NOT NULL,
            FOREIGN KEY (bookID) REFERENCES bookRecords (bookID)
            )
            """
            )
except pymysql.Error as error:
    print(f"Failed to create table 'userRecord': {error}")
        
mydb.commit()

try:    
    mycursor.execute("SHOW TABLES LIKE 'adminRecords' ")
    result=mycursor.fetchone()
    if not result: 
        mycursor.execute(
            """
            CREATE TABLE IF NOT EXISTS adminRecords(
            adminID VARCHAR(30) PRIMARY KEY, 
            password VARCHAR(20) NOT NULL
            )
            """
            )
        
except pymysql.Error as error:
    print("Failed to create table 'adminRecords': {error}")
    
mydb.commit()
    

try:    
    mycursor.execute("SHOW TABLES LIKE 'feedbacks' ")
    result=mycursor.fetchone()
    
    if not result: 
        mycursor.execute(
            """
            CREATE TABLE IF NOT EXISTS feedbacks(
            feedbackID INTEGER PRIMARY KEY AUTO_INCREMENT,
            textFeedback TEXT DEFAULT NULL,
            rating VARCHAR(10) NOT NULL
            )
            """
            )
    
except pymysql.Error as error:
    print("Failed to create table 'feedbacks' : {error}")
    
mydb.commit()
mydb.close()


    

