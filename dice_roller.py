from random import randint 

def dice_roll(num): 
    roll = randint(1,num)
    return roll

roll_again = "y"

while roll_again == "y": 
    sides = int(input("How many sides does the dice have? "))
    number = int(input("How many times do you want to roll the dice? "))
    total = 0
    results = []
    for i in range(number): 
        result = dice_roll(sides)
        results.append(result)
        total += result 
    print(f"Your rolls are {results}")
    print(f"The sum of your rolls is {total}")
    roll_again = input("Do you want to roll again? (y/n)")

