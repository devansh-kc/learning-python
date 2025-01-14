age=  int(input("What is your age :"))
day =str.lower(input("What day is it : "))
price = 12 if age >= 18 else 8


if  day =="wednesday":
    print(f"your age is {age} and today is {day} and the price of ticket is {price-2} ")
else:
    print(f"your age is {age} and today is {day} and the price of ticket is {price} ")


    