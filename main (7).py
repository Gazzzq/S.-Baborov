import random 
random_value = random.randint (1, 100)
attempt=0
print("компьютер загадал число от 1 до 100 и у вас 10 попыток")
for i in range(1,11):
    choice= int(input("введите число"))
    if choice > random_value:
        print("много")
    elif choice < random_value:
        print("мало")
    else:
        print(f"вы угадали число с {i}-ой попытки")
        
    
                