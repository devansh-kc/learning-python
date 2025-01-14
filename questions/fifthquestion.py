distance = int(input("provide the distance"))

if distance < 3:
    print("walk")
elif distance >3 and distance <15:
    print("bike")
elif distance >15 :
    print("Car")
    
    
    
order_size= "Medium"
extra_shot= True
if extra_shot:
    cofee =order_size+" Coffe with an extrashot"

else:
    cofee = order_size + " Coffe without extrashot"

print(cofee)
