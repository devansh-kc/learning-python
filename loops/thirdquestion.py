number = int(input("Please enter the number:"))
for num in range(1, 11 ):
    if num ==5:
        continue
    print(number,"x", num, "=", number * num)
    
    
    
# #  forth question
string=  input("Enter the word to be reversed: ")
reversedString =""
for char in string:
    reversedString =char + reversedString
    


# fifth question
string ="i want to fuck you so bad that . I will be mad"


for char in string:
    print(char)
    if string.count(char) ==1:
        print("Char is",char)
        break

    
    
# sixth question

number=  99


factorial =1

while  number >0 :
    factorial  =  factorial * number
    number=  number-1
    
    
print(factorial)


# seventh question"

while True:
    number=  int(input("Please provide the number between 1 and 10: "))
    if number <= 1 and number <=10:
        print("Thanks")
        break
    else:
        print("Invalid number, Try again")



        
# eight question
number = int(input("Please provide the number to check that the number is a prime number or not"))

is_prime =True

if number >1:
        for i in range (2,number):
            if (number % i) ==0:
                is_prime= False
                break


print((number, is_prime))
                
                
items = ["apple", "banana", "orange", "apple", "mango"]
unique_Item=  set()


for item in items:
    if item in unique_Item:
        print("dulpicate: ",  item)
        break
    unique_Item.add(item)
    print(unique_Item)
            

        
        

#  tenth question
import time


wait_time=  1
max_retries=  5
attempts =0

while attempts < max_retries:
    print( "attempts", attempts+1,"wait time =",+wait_time, "secs" )
    time.sleep(wait_time)
    wait_time *=2
    attempts +=1
    

