from pymongo import MongoClient
from bson import ObjectId

Client = MongoClient('mongodb+srv://schoolDB:schoolDB@cluster0.xforb.mongodb.net/', tlsAllowInvalidCertificates=True)
print('\n',Client)


db = Client['schoolDB_manger']
schoolDB_collection = db['schoolDB_collection']

def listAllStudent():
    totalStudent = 0

    for list in schoolDB_collection.find():
            totalStudent +=1 
            # print(list)
            # print(schoolDB_collection.find())
            print(f"ID:{list['_id']}\nName:{list['name']}\nRoll no.:{list['roll']}\n{'-'*30}")

    print(f'Total no. of student {totalStudent}')   
    
def addStudent(name,roll):
    schoolDB_collection.insert_one({'name': name, 'roll': roll})

def updateStudentDetails(roll,newName,newRoll):
    
    schoolDB_collection.update_one(
        # {'roll':roll}, 
        # #for finding which student data have to change (Method 1)
        {'_id':ObjectId(roll)}, 
        #for finding which student data have to change (Method 2)
        # but have to give object id insted of roll no.
        {'$set':{'name':newName, 'roll':newRoll}} #for setting values
        )
    
    #     result = schoolDB_collection.update_one(
    #     {'_id': roll}, # Assuming _id is not ObjectId
    #     {'$set': {'name': newName, 'roll': newRoll}}
    # )
    #     print(f'Matched: {result.matched_count}, Modified: {result.modified_count}')

def deleteStudentDetailes(roll):
    # schoolDB_collection.delete_one({'roll':roll})
    schoolDB_collection.delete_one({'_id':roll})

def main():
    while True:
        
        menuList = f"{'-'*30}\n1. LIST STUDENT\n2. ADD STUDENT\n3. UPDATE STUDENT DATA\n4. DELETE STUDENT DATA\n5. EXIT\n{'-'*30}"
        print(menuList)
        select = input('\nPRESS ANY ONE BETWEEN 1 TO 5 :')
        
        match select:
            case '1':
                listAllStudent()

            case '2':
                name = input('Enter name :')
                roll = input('Enter roll no. :')
                addStudent(name,roll)

            case '3':
                listAllStudent()
                roll = input('Enter existing roll no. or Object Id:')
                newName = input("Enter new name :")
                newRoll = input("Enter new roll no. :")
                updateStudentDetails(roll,newName,newRoll)

            case '4':
                listAllStudent()
                roll = input('Enter roll no.:')    
                deleteStudentDetailes(roll)

            case '5':
                exit()    

if __name__ == '__main__':
    main()
