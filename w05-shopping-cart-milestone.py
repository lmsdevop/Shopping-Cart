# Importations
import time

# Setting the variables
cart = []
price = []
item_cart = ''
item_price = ''
choice = ''

#Programming starts
print("\nWelcome to BestGuy Market!")
time.sleep(3)
while choice != 5:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item (IN CONSTRUCTION)")
    print("4. Compute total (IN CONSTRUCTION)")
    print("5. Quit")
    choice = input("Please enter an action: ")

    #validating the choice
    while '5' < choice or '1' > choice:
        print("\nPlease select a valid number")
        choice = input("Please enter an action: ")
        continue
    int_choice = int(choice)

    #adding a item
    if 1 == int_choice:
        item_cart = input("\nWhat item would you like to add? ").capitalize()
        cart.append(item_cart)
        while True:
            try:
                item_price = float(input(f"What is the price of '{item_cart}'? "))
                break
            except ValueError:
                print("Only numbers are valid")
        price.append(item_price)
        print(f"'{item_cart}' has been added to the cart.")
        time.sleep(1)

    #viewing the cart
    elif 2 == int_choice:
        print("\nThe contents of the shopping cart are:")
        for i in range(len(cart)):
            print(f"{i+1}. {cart[i]} - ${price[i]: .2f}")
        time.sleep(2)

    #quiting the market
    elif 5 == int_choice:
        print("\nThank you for coming, return often!")
        time.sleep(2)
        break
    

            