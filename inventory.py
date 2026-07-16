"""Shoe inventory management system.

This module provides a command-line interface to manage a shoe inventory.
The inventory is stored in a text file named 'inventory.txt', where each line."""

import os
from tabulate import tabulate

FILE_NAME = 'inventory.txt'
shoes_list = []  # Global list to store shoe objects in memory

class Shoe:
    """Class representing a shoe in the inventory."""

    def __init__(self, country, code, product, cost, quantity):
        self.country = countryCountry,Code,Product,Cost,Quantity
South Africa,SKU44386,Air Max 90,2300,20
China,SKU90000,Jordan 1,3200,50
Vietnam,SKU63221,Blazer,1700,19
United States,SKU29077,Cortez,970,60
Russia,SKU89999,Air Force 1,2000,43
Australia,SKU57443,Waffle Racer,2700,4
Canada,SKU68677,Air Max 97,3600,13
Egypt,SKU19888,Dunk SB,1500,26
Britain,SKU76000,Kobe 4,3400,32
France,SKU84500,Pegasus,2490,28
Zimbabwe,SKU20207,Air Presto,2999,7
Morocco,SKU77744,Challenge Court,1450,11
Israel,SKU29888,Air Zoom Generation,2680,6
Uganda,SKU33000,Flyknit Racer,4900,9
Pakistan,SKU77999,Air Yeezy 2,4389,67
Brazil,SKU44600,Air Jordan 11,3870,24
Columbia,SKU87500,Air Huarache,2683,8
India,SKU38773,Air Max 1,1900,29
Vietnam,SKU95000,Air Mag,2000,2
Israel,SKU79084,Air Foamposite,2430,4
China,SKU93222,Air Stab,1630,10
South Korea,SKU66734,Hyperdunk,1899,7
Australia,SKU71827,Zoom Hyperfuse,1400,15
France,SKU20394,Eric Koston 1,2322,17
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def __str__(self):
        """String representation of the shoe."""
        return (f"Country: {self.country} | Code: {self.code} | "
                f"Product: {self.product} | Cost: {self.cost} | "
                f"Quantity: {self.quantity}")
    
    def get_cost(self):
        return self.cost
    
    def get_quantity(self):
        return self.quantity
    
def save_inventory_file():
    """OVERWRITE the inventory file with the current shoe list."""
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
         file.write("Country,Code,Product,Cost,Quantity\n")
        
         for shoe in shoes_list:
                file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},"
                    f"{shoe.cost},{shoe.quantity}\n"
            )

def read_shoes_data():
    """Reads data from inventory.txt, creating the file if missing."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', encoding='utf-8') as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            
    shoes_list.clear()

    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        next(file)

        for line in file:
            parts = line.strip().split(',')
            
            if len(parts) == 5:
                country, code, product, cost, quantity = parts
                shoes_list.append(Shoe(country, code, product, cost, quantity))
                                     
        print("-> Shoes data successfully loaded.\n")

def view_all():
    """Displays all shoes in a tabular format."""
    if not shoes_list:
        print("No shoes in inventory.\n")
        return
        
    data = [
        [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]
        for shoe in shoes_list
    ]

        
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
        
    print("\n" + tabulate(data, headers=headers, tablefmt="grid"))
    print()

def capture_shoes():
    """Allows user to add a new shoe to the inventory."""
    try:
        country = input("Enter shoe country: ")
        code = input("Enter shoe code: ")
        product = input("Enter shoe product name: ")
        cost = float(input("Enter shoe cost: "))
        quantity = int(input("Enter shoe quantity: "))

        shoes_list.append(Shoe(country, code, product, cost, quantity))
            
        save_inventory_file()
            
        print(f"\n-> Success: Shoe '{product}' added!\n")
    
    except ValueError:
        print("\n-> Error: Invalid number for cost or quantity. Try again.\n")


def re_stock():
    """Finds the shoe with the lowest quantity and updates stock."""
    if not shoes_list:
        print("\n-> Inventory is empty.\n")
        return

    lowest_shoe = min(shoes_list, key=lambda s: s.quantity)
    
    print(f"\n--- Re-stocking ---")
    print(f"Lowest quantity: {lowest_shoe.product} ({lowest_shoe.quantity})")
    
    choice = input("Restock this item? (y/n): ").strip().lower()
    
    if choice == 'y':
        try:
            add_qty = int(input("Enter quantity to add: "))
            lowest_shoe.quantity += add_qty
            save_inventory_file()
            
            print(f"\n-> Success: Quantity updated to {lowest_shoe.quantity}.\n")
        
        except ValueError:
            print("\n-> Invalid input. Operation canceled.\n")
    else:
        print("\n-> Operation canceled.\n")

def search_shoe():
    """Searches for a shoe by code."""
    code = input("\nEnter shoe code to search: ").strip()
    
    match = next((s for s in shoes_list if s.code == code), None)
    
    print("\n--- Shoe Details ---")
    print(match if match else 'No shoe found.')
    print()


def value_per_item():
    """Calculates and prints total value for each shoe."""
    if not shoes_list:
        print("\n-> Inventory is empty.\n")
        return
        
    print("\n--- Total Value Per Item ---")
    for s in shoes_list:
        total_value = s.cost * s.quantity
        print(f"{s.product} ({s.code}) - Total Value: ${total_value:.2f}")
    print()


def highest_qty():
    """Determines the highest quantity shoe and lists it for sale."""
    if not shoes_list:
        print("\n-> Inventory is empty.\n")
        return
        
    highest_shoe = max(shoes_list, key=lambda s: s.quantity)
    print(f"\n--- Special Sale Item ---")
    print(f"{highest_shoe.product} is marked for sale! "
          f"({highest_shoe.quantity} in stock)\n")
    

def main_menu():
    """Main menu for the inventory management system."""
    
    read_shoes_data()
    
    menu = """
Select an option:
1. View all shoes
2. Add a new shoe
3. Re-stock lowest quantity shoe
4. Search shoe by code
5. Calculate value per item
6. Mark highest quantity shoe for sale
7. Exit Program
"""
    def reload_data():
        shoes_list.clear()
        read_shoes_data()

    actions = {
        '1': view_all,
        '2': capture_shoes,
        '3': re_stock,
        '4': search_shoe,
        '5': value_per_item,
        '6': highest_qty
    }
    while True:
        print(menu)
        choice = input("Enter your choice: ").strip()

        if choice in actions:
            actions[choice]()
        elif choice == '7':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\n-> Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
