import random
def Welcome():
    print("Welcome to the Monty Hall Problem")
    print("Alpha")

def Doors():
    doors = ["Door One", "Door Two", "Door Three"]
    a = ["goat","goat","car"]
    for i in doors :
        set_dict = {i :random.choice(a)}
    for j in doors:
        set_dict[j] = random.choice(a)  
    x = set_dict[i]
    y = set_dict[j]
    if x == "car":
        for k in doors:
            set_dict[k] = "goat"
    elif y == "car":
        for k in doors:
            set_dict[k] = "goat"
    else:
        for k in doors:
            set_dict[k] = "car"
    print(set_dict)
    print(doors)
    print("Beta")
Doors()