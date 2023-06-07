import time
import tkinter as tk
from tkinter import messagebox, ttk

def add_item():
    item_cart = item_entry.get().capitalize()
    item_price = price_entry.get()
    try:
        item_price = float(item_price)
        cart.append(item_cart)
        price.append(item_price)
        item_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        result_label.configure(text=f"'{item_cart}' has been added to the cart.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid price.")

def view_cart():
    cart_contents = "\nItems in the shopping cart:\n\n"
    for i in range(len(cart)):
        cart_contents += f"{i+1}. {cart[i]} - ${price[i]:.2f}\n"
    if len(cart) == 0:
        cart_contents = "The cart is empty."
    messagebox.showinfo("Shopping Cart", cart_contents)

def remove_item():
    try:
        remove = int(remove_entry.get()) - 1
        if remove >= 0 and remove < len(cart):
            cart.pop(remove)
            price.pop(remove)
            result_label.configure(text="Item removed.")
            message_removed = "Item removed"
            messagebox.showinfo("Remove", message_removed)
        else:
            messagebox.showerror("Error", "Please select a valid item.")
    except ValueError:
        messagebox.showerror("Error", "Please select a valid item.")

def compute_total():
    total = sum(price)
    result_label.configure(text=f"The total price of the items in the shopping cart is ${total:.2f}")

def quit_program():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()

# Setting the variables
cart = []
price = []

# Creating the GUI window
root = tk.Tk()
root.title("BestGuy Market")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

# Add item section
add_item_label = tk.Label(root, text="Add Item", font=("Arial", 14), bg="#f2f2f2")
add_item_label.pack(pady=10)

item_frame = tk.Frame(root, bg="#f2f2f2")
item_frame.pack()

item_label = tk.Label(item_frame, text="Item:", font=("Arial", 12), bg="#f2f2f2")
item_label.grid(row=0, column=0, padx=5)

item_entry = tk.Entry(item_frame, font=("Arial", 12))
item_entry.grid(row=0, column=1, padx=5)

price_label = tk.Label(item_frame, text="Price:", font=("Arial", 12), bg="#f2f2f2")
price_label.grid(row=1, column=0, padx=5)

price_entry = tk.Entry(item_frame, font=("Arial", 12))
price_entry.grid(row=1, column=1, padx=5)

add_button = tk.Button(root, text="Add", font=("Arial", 12), command=add_item)
add_button.pack(pady=10)

# View cart section
view_cart_button = tk.Button(root, text="View Cart", font=("Arial", 12), command=view_cart)
view_cart_button.pack()

# Remove item section
remove_item_label = tk.Label(root, text="Remove Item", font=("Arial", 14), bg="#f2f2f2")
remove_item_label.pack(pady=10)

remove_frame = tk.Frame(root, bg="#f2f2f2")
remove_frame.pack()

remove_label = tk.Label(remove_frame, text="Item number:", font=("Arial", 12), bg="#f2f2f2")
remove_label.grid(row=0, column=0, padx=5)

remove_entry = tk.Entry(remove_frame, font=("Arial", 12))
remove_entry.grid(row=0, column=1, padx=5)

remove_button = tk.Button(root, text="Remove", font=("Arial", 12), command=remove_item)
remove_button.pack(pady=10)

# Compute total section
compute_total_button = tk.Button(root, text="Compute Total", font=("Arial", 12), command=compute_total)
compute_total_button.pack()

# Result section
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f2f2f2")
result_label.pack(pady=10)

# Quit program section
quit_button = tk.Button(root, text="Quit", font=("Arial", 12), command=quit_program)
quit_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()