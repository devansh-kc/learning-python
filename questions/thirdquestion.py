marks=  int(input("Please provide the marks"))

if marks >= 100:
    print("Invalid marks. Marks should be less than or equal to 100")
    exit()
if marks >=90 and marks <= 100 :
    print("Grade A")
elif marks >=80 and marks <=89 :
    print("Grade B")
elif marks >=70 and marks <=79 :
    print("Grade C")
elif marks >=60 and marks <=69 :
    print("Grade D")
else:
    print("Grade F")
    