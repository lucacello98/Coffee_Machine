
# Importing the necessary library for platform-related functionalities
from platform import machine

# Importing sys for system exit functionality
import sys

# Defining the MENU dictionary with drinks and their ingredients and costs
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

# Defining the available resources (water, milk, and coffee) in the machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0,
}


# Function to check if there are enough resources to make the selected drink
def check_resources(answer):
    # Get the ingredients needed for the selected drink from MENU
    drink = MENU[answer]["ingredients"]

    # Check if there are enough resources for each ingredient
    for item in drink:
        if drink[item] > resources[item]:  # If required amount of ingredient is greater than what's available
            print(f"There is not enough {item} in the machine please refill")
            sys.exit()  # Exit the program if resources are insufficient

    # Deduct the required ingredients from resources after confirming availability
    for item in drink:
        resources[item] -= drink[item]

    return True  # Indicate that the resources check is successful


# Function to handle the insertion of coins
def insert_coin():
    # Collect coin inputs from the user
    quarters = int(input("How many quarters do you have? "))
    dimes = int(input("How many dimes do you have? "))
    nickels = int(input("How many nickels do you have? "))
    pennies = int(input("How many pennies do you have? "))

    # Calculate the total amount of money inserted
    return (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)


# Function to check if the money inserted is sufficient to buy the drink
def check_money(total, answer):
    # Get the cost of the selected drink
    cost = MENU[answer]['cost']

    # If the money inserted is less than the cost, refund the money and exit
    if cost > total:
        print(f"Sorry that is not enough your change of ${total} has been refunded")
        sys.exit()

    # If the inserted money is more than the cost, calculate the change to be given back
    elif total > cost:
        resources["money"] += cost
        return round(total - cost, 2)


# Variable to control the machine’s operation state
machine_on = True

# Main loop to keep the machine running until turned off
while machine_on:
    # Prompt the user for input to select a drink or perform an action
    answer = input("What would you like espresso, latte or cappuccino? ")

    # If the user inputs "report", show the available resources in the machine
    if answer == "report":
        print(resources)

    # If the user inputs "off", turn off the machine
    elif answer == "off":
        machine_on = False

    # If the user selects "espresso", check resources, insert money, and calculate change
    elif answer == "espresso":
        check_resources(answer)  # Check if enough resources are available for espresso
        total = insert_coin()  # Insert coins and get the total
        change = check_money(total, answer)  # Check if the total is enough and calculate change
        print(f"your change is ${change}, please enjoy your {answer}")  # Print the change and message

    # If the user selects "latte", perform similar steps as above
    elif answer == "latte":
        check_resources(answer)
        total = insert_coin()
        change = check_money(total, answer)
        print(f"your change is ${change}, please enjoy your {answer}")

    # If the user selects "cappuccino", perform similar steps as above
    elif answer == "cappuccino":
        check_resources(answer)
        total = insert_coin()
        change = check_money(total, answer)
        print(f"your change is ${change}, please enjoy your {answer}")

    # If the input is invalid, inform the user
    else:
        print("Invalid input please select espresso, latte or cappuccino")






