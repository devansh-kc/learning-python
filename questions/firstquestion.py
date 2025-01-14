from numbers import Number


age=  int(input("Please enter your age :"))
if age <= 13:
    print(f"your age is {age} and you are an child")

elif age > 13 and age <= 19:
    print(f"your age is {age} and you are an teenager")
elif age> 19 and age <= 59 :
    
    print(f"your age is {age} and you are an Adult")
else:
    print(f"your age is {age} and you are an senior citizen")

