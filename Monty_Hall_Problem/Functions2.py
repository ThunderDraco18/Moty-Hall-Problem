import random
def Welcome():
    print("Welcome to the Monty Hall Problem")
    print("Alpha")

def Doors():
    global doors
    doors = ["Door One", "Door Two", "Door Three"]
    a = ["goat","goat","car"]
    global set_dict 
    set_dict= {}
    set_dict["Door One"] = random.choice(a)
    set_dict["Door Two"] = random.choice(a)
    x = set_dict["Door One"]
    y = set_dict["Door Two"]
    if x == "car":
        set_dict["Door Three"] = "goat"
    elif y ==  "car":
        set_dict["Door Three"] = "goat"
    else:
        set_dict["Door Three"] = "car"

def Interface():
    global wins_count
    wins_count = 0
    global loose_count
    loose_count = 0
    Doors()
    global user_inp
    user_inp = input("Please select a Door: ")
    if user_inp.title() == "Door One":
        door_switch()
    elif user_inp.title() == "Door Two":
        door_switch()
    elif user_inp.title() == "Door Three":
        door_switch()
    else:
        print("No valid option given")

def door_switch():
    for i in doors:
        if set_dict[user_inp.title()] == "goat":
            if i != user_inp.title():
                    if set_dict[i] == "goat":
                        print(i + ": This door has a goat behind it.")
                        ask =  input("Do you wish to keep the door you selected or would you like to change? ")
                        if ask.title() == "Keep":
                            if set_dict[user_inp.title()] == "car":
                                print("You win")
                            else:
                                print("You lose")
                        elif ask.title() == "Change":
                            doors.remove(i)
                            doors.remove(user_inp.title)
                            print(doors)
                            if set_dict[doors[0]] == "car":
                                print("You Win")
                            elif set_dict[doors[0]] == "Goat":
                                print("You got a goat")
            print(set_dict)
        elif set_dict[user_inp.title()] == "car":
             if i != user_inp.title():
                    if set_dict[i] == "goat":
                        print(i + ": This door has a goat behind it.")
                        ask = input("Do you wish to keep the door you selected or would you like to change? ")
                        if ask.title() == "Change":
                           print("You loose");
                           loose_count = loose_count + 1 
                        elif ask.title() == "Keep":
                            print("You Win")
                            wins_count = wins_count + 1
                        print(set_dict)
                        break
    print("Wins: " + str(wins_count))
    print("looses: " + str(loose_count))


while 1>0:
    Interface()