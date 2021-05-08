water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550

espresso = {"water": 250, "milk": 0, "coffee_beans": 16, "money": 4}
latte = {"water": 350, "milk": 75, "coffee_beans": 20, "money": 7}
cappuccino = {"water": 200, "milk": 100, "coffee_beans": 12, "money":6}

def home():
    print(f"""The coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{cups} of disposable cups
{money} of money\n""")
    
def adj_balance(coffee):
    global water, milk, coffee_beans, cups, money
    water -= coffee["water"]
    milk -= coffee["milk"]
    coffee_beans -= coffee["coffee_beans"]
    cups -= 1
    money += coffee["money"]

def check_resources(coffee):
    global water, milk, coffee_beans, cups, money
    if water > coffee["water"]:
        if milk > coffee["milk"]:
            if coffee_beans > coffee["coffee_beans"]:
                if cups > 0:
                    print("I have enough resources, making you a coffee!")
                    adj_balance(coffee)
                else: 
                    print("Sorry, not enough coffee beans!")
            else:
                print("Sorry, not enough coffee beans!")
        else:
            print("Sorry, not enough milk!")
    else:
        print("Sorry, not enough water!")
        

    
def buy():
    buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    if buy == "1":
        check_resources(espresso)
    elif buy == "2":
        check_resources(latte)
    elif buy == "3":
        check_resources(cappuccino)
    else:
        pass
    
def fill():
    global water 
    global milk
    global coffee_beans
    global cups
    add_water = int(input("Write how many ml of water do you want to add:\n> "))
    add_milk = int(input("Write how many ml of milk do you want to add:\n> "))
    add_coffee_beans = int(input("Write how many grams of coffee beans do you want to add:\n> "))
    add_cups = int(input("Write how many disposable cups of coffee do you want to add:\n> "))
    water += add_water
    milk += add_milk
    coffee_beans += add_coffee_beans
    cups += add_cups
    
def take():
    global money
    print(f"I gave you ${money}")
    money = 0 
    
while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action== "remaining":
        home()
    else:
        break