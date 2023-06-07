# Importations
import time

# Setting the variables
cart = []
price = []
item_cart = ''
item_price = ''
choice = ''

# Programming starts
print("\nWelcome to BestGuy Market!")
time.sleep(2)
while choice != 5:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    choice = input("Please enter an action: ")

    # validating the choice
    while '5' < choice or '1' > choice:
        print("\nPlease select a valid number")
        choice = input("Please enter an action: ")
        continue
    int_choice = int(choice)

    # adding a item
    if 1 == int_choice:
        item_cart = input("\nWhat item would you like to add? ").capitalize()
        cart.append(item_cart)
        while True:
            try:
                item_price = float(
                    input(f"What is the price of '{item_cart}'? "))
                break
            except ValueError:
                print("Only numbers are valid")
        price.append(item_price)
        time.sleep(1)
        print(f"'{item_cart}' has been added to the cart.")
        time.sleep(1)

    # viewing the cart
    elif 2 == int_choice:
        print("\nThe contents of the shopping cart are:")
        for i in range(len(cart)):
            print(f"{i+1}. {cart[i]} - ${price[i]: .2f}")
        time.sleep(2)

    # removing an item
    elif 3 == int_choice:
        if len(cart) < 1:
            print("\nThere are no itens to be remove")
            time.sleep(1)
        else:
            while True:
                try:
                    remove = int(
                        input("Which item would you like to remove? "))
                    try:
                        if remove-1 == cart.index(cart[remove-1]):
                            cart.pop(remove-1)
                            price.pop(remove-1)
                            break
                    except IndexError:
                        print(
                            "\nThis item wasn't in the list, select an Item from the list")
                        print("\nThe contents of the shopping cart are:")
                        for i in range(len(cart)):
                            print(f"{i+1}. {cart[i]} - ${price[i]: .2f}")
                except ValueError:
                    print("Please select a Valid Item: ")
            time.sleep(1)
            print('\nItem removed.')
            time.sleep(1)

    # Computing the total
    elif 4 == int_choice:
        time.sleep(1)
        print(
            f"\nThe total price of the items in the shopping cart is ${sum(price): .2f}")
        time.sleep(2)

    # Leaving the market
    elif 5 == int_choice:
        print('\nThank you for coming!')
        time.sleep(2)
        break
