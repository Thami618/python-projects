
print("Welcome to trasure island, lets play!!")
which_way = input("Which Way do you want to go? L or R\n").lower()
swim_or_wait = input("Do you want to swim or wait\n").lower()
which_door = input("Which do R B Y?\n").lower()


if which_way == "Left":
    if swim_or_wait == "Wait":
        if which_door == "Yellow":
             print("You win") 
        elif which_door == "Blue":
            print("Game Over")
        elif which_door == "Red":
            print("Game Over")
    elif swim_or_wait == "Swim":
        print("Game Over")
else:
    print("Game Over")
