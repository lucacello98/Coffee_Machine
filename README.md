
Description:
A simple Python-based coffee machine simulator that allows users to select and purchase drinks such as espresso, latte, and cappuccino. The program manages resources (water, milk, and coffee) and tracks the money inserted by the user. It also checks whether the resources are sufficient to make the selected drink and gives the option to check available resources, purchase drinks, or turn off the machine.

Features:
Drink Selection: Choose from three drinks: espresso, latte, and cappuccino.
Resource Management: The program keeps track of available resources (water, milk, coffee) and ensures they are sufficient for making the selected drink.
Money Handling: The program accepts coin inputs (quarters, dimes, nickels, and pennies), checks if the amount inserted is sufficient, and returns the change if applicable.
Reports: View the current available resources by typing `report`.
Exit: Type `off` to turn off the coffee machine.

How It Works:
Drink Selection: The user is prompted to select a drink (espresso, latte, or cappuccino).
Resource Check: The program checks if there are enough resources (water, milk, coffee) to make the selected drink. If resources are insufficient, the program will exit.
Coin Insertion: The user is prompted to insert coins (quarters, dimes, nickels, pennies) to pay for the drink.
Money Check: The program checks if the inserted amount is sufficient to purchase the selected drink. If not, the money is refunded. If the amount is sufficient, the cost is deducted from the resources, and the machine prepares the drink.
Change: If the inserted money is greater than the cost of the drink, the program calculates and gives back the change.
Report: The user can type `report` to check the current available resources in the machine.
Turn Off: The user can type `off` to turn off the coffee machine.



