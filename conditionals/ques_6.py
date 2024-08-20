password = input('Enter your password.... ')

if len(password)<= 6:
    print('Weak password')
elif len(password)>=7 and len(password)<=8:
    print('Medium password')
else :
    print('Strong password')