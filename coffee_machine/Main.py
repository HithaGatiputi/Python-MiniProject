MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

def coins():
    print("Please insert the coins.")
    total = int(input("how many quarters?  ")) * 0.25
    total += int(input("how many dimes?  ")) * 0.10
    total += int(input("how many nickles?  ")) * 0.5
    total += int(input("how many pennies?  "))* 0.01
    return total

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

def transaction_successful(payment,cost):
    if payment >= cost:
        change = round(payment - cost , 2)
        global profit
        profit += cost
        print(f"Here is ${change} in change.")
        return True
    else :
        print("Sorry that's not enough money. Money refunded.")
        return False


end = False

while not end:
    order = input("What would you like? (espresso - 1.5/latte - 2.5/cappuccino - 3): ")
    if order == "report":
        print(f"Water:{resources['water']}ml ")
        print(f"Milk:{resources['milk']}ml ")
        print(f"Coffee:{resources['coffee']}g ")
        print(f"Money: ${profit}")
    elif order == "off":
        end = True
    else:
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            payment = coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(order,drink["ingredients"])



