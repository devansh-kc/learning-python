year = int(input("please pprovide the year \n"))
 
if (year % 400 ==0)or(year %4 ==0 and year %100 !=0):
    print(f"the {year} is leap year")
    
else:
    print(f"the {year} is not a leap year")
 