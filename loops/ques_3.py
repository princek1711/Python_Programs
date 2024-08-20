# Multiplication Table Printer

userInput = int(input("Enter any number..."))

for num in range(1,userInput+1):
    for number in range(1,11):
        if(number == 5):
            continue
        print(num,"x",number,"=",num*number)
    print()    


    