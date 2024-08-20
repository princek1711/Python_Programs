# Leap year cheacker


def askValue():
    giveValue = int(input('Enter year to check leap year...'))
    return giveValue

def year(value = askValue()):    
    while True:
        if value%100 == 0 and value%400 == 0:
                result = f"{value} is not leap year"
                print(result)
                break
        else:
            if value%4 == 0 or value%400 == 0:
                print(f"{value} is leap year")
                break

# askValue()
year()