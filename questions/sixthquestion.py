password=  str(input("Please enter your password :\n"))

if len(password)>10 :
    print("your password is strong")
elif len(password)>6 and len(password) <10 :
    print("your password is medium")
else:
    print("Your password is very weak")
    
    