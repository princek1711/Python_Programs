# RV School student details manager project 
import json

def exitFunc():
    print(f"{'-'*50}\nExiting...\n{'-'*50}")

def showList(details):
    print("-" * 70)
    for index, detail in enumerate(details, start=1):
        name = detail.get('name', 'Unknown Name')  
        roll = detail.get('roll', 'Unknown Roll')  
        print(f"{index}. {name}, Roll no.: {roll}")
    print('-' * 70)
    
def loadData():
    try:
        with open('schoolDatabase.txt','r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []

def saveDetails(details):
    with open('schoolDatabase.txt','w') as file:
        json.dump(details,file)

def addStudentDetails(details):
    while True:  
        name = input("Enter student name Or Hit enter for exit:")
        if name == "":
            exitFunc()
            break
        
        try:
         roll = int(input("Enter roll no. :  "))
         student_exist = False

         for student in details:
             if student['roll'] == roll:
                 print(f"Roll no. {roll} already exist")
                 student_exist = True
                 
             
         if not student_exist:
            details.append({"name": name,"roll": roll})     
            saveDetails(details)
            print("Student added successfully.")


        except ValueError:
            print("Invalid roll no. Please enter a valid roll no.")   

def updateStudentDetails(details):
    showList(details)
    while True:
        try:
            userInput =input("Enter roll no. of student Or Hit enter for exit :") 
            if userInput == '':
                exitFunc()
                break

            index = int(userInput)  

        except ValueError:
                print("Invalid roll no. Please! Enter a valid integer")    
                continue   

        found = False 
        for student in details:

            if student['roll'] == index:
                found = True
                print("Hit enter for exit")
                choice = input("What do you wanna change name,roll no., or both? :")
                
                match choice:
                    case 'name':
                        new_name = input("Enter new name :")
                        student['name'] = new_name

                    case 'roll':
                        try:
                            new_roll_no = int(input("Enter new roll no. :"))
                            student['roll'] = new_roll_no
                        except ValueError:
                            print("Invalid roll no. Please! Enter a valid integer")

                    case 'both':
                        new_name = input("Enter new name :")
                        student['name'] = new_name
                        new_roll_no = int(input("Enter new roll no. :"))
                        student['roll'] = new_roll_no

                    case "":
                        exitFunc()
                        break

        if not found:            
                print("Sorry! Invalid input given")
                break

def deleteStudentDetails(details):
    showList(details)
    while True:
        try:
            userInput =input("Enter roll no. of student Or Hit enter for exit :") 
            if userInput == '':
                print(f"{'-'*50}\nExiting...\n{'-'*50}")
                break

            index = int(userInput)  

        except ValueError:
            print("Invalid roll no. Please! Enter a valid integer")    
            continue

        found = False
        for i, student in enumerate(details):
            if student['roll'] == index:
                found = True
                del details[i]
                print(f"Student data with {index} has been deleted")
                saveDetails(details)
                showList(details)
                break

        if not found:
            if not details:  # Check if the details list is empty
                print(f"{'-'*50}\nThere is no data to delete.\n{'-'*50}\n")
                break
            else:
                 print("Sorry! No student found with that roll number.")
                           
def main():
    print(f"Welcome to the RV School\n{"*"*50}")
    details = loadData()
    while True:
        menuList = "1. Press 1 for add new student details\n2. Press 2 for make any updation in existing student details\n3. Press 3 for delet your any existing student details\n4. Press 4 for see student data base\n5. Press 5 for exit"
        print(menuList)
        choice  = input("\nEnter your choice..")
        if choice == '':
            exitFunc()
            break
        elif choice != '':
            choice = int(choice)

            match choice:
                case 1:
                    addStudentDetails(details)
                case 2:
                    updateStudentDetails(details)
                case 3:
                    deleteStudentDetails(details)
                case 4:
                    showList(details)
                case 5:
                    exitFunc()
                    break
                case _:
                    print(f"\n{'-'*50}\nInvaild Choice\n{'-'*50}\n")
                    # break
   
if __name__ == "__main__":
    main()