import sqlite3

con = sqlite3.connect('schoolDB.db')
cursor = con.cursor()

def askdetail():  #OK
     name = input("Enter your name :")
     roll = int(input("Enter your roll no. :"))
     return name,roll

def exitfun():    #OK
     print(f"{'-'*50}\nExiting......\n{'-'*50}\n")
     
cursor.execute('''     
    CREATE TABLE IF NOT EXISTS schoolDB (
               roll INTEGER PRIMARY KEY,
               name TEXT NOT NULL
    )
''') 

def addData(name,roll): #OK
    cursor.execute("INSERT INTO schoolDB (name, roll) VALUES (?, ?)", (name,roll))
    con.commit()


def updateData(existingRoll,new_name,new_roll): #OK
    cursor.execute("UPDATE schoolDB SET name = ?, roll = ? WHERE roll = ?",(new_name,new_roll,existingRoll))
    con.commit

def deletData(roll):  #Ok
    cursor.execute("DELETe from schoolDB where roll = ?",(roll,))
    print(f"{'-'*50}\n Student data deleted sucessfully\n{'-'*50}")
    con.commit

def showdata(): #OK
    cursor.execute("SELECT * FROM schoolDB")
    for row in cursor.fetchall():
        print(row)
        print("-" * 70)



def main(): #OK
    while True:
            menuList = "\n1. Press 1 for add new student details\n2. Press 2 for make any updation in existing student details\n3. Press 3 for delet your any existing student details\n4. Press 4 for see student data base\n5. Press 5 for exit"
            print(menuList)
            choice  = input("\nEnter your choice..") 

            if choice == '1':
                 name,roll = askdetail()
                 addData(name,roll)
            
            elif choice == '2':
                 showdata()
                 existingRoll = input("Enter roll no. :")
                 new_name = input("Enter updated name :")
                 new_roll = input("Enter updated roll no :")
                 updateData(existingRoll,new_name,new_roll)
            
            elif choice == '3':
                 showdata()
                 existingRoll = input("Enter roll no. :")
                 deletData(existingRoll)

            elif choice == '4':
                 showdata()

            elif choice == "5":
                 con.close()
                 exitfun()
                 break     

            else:
                 print("Invalid Choice")     




if __name__ == '__main__':  #OK
     main()