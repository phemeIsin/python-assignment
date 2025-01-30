#a simple inventory emulator that you can use to add update and view inventory 
class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
            print(f"Updated {name}: New quantity is {self.items[name]}")
        else:
            self.items[name] = quantity
            print(f"Added {name}: Quantity is {quantity}")
    def get_item(self, name):
        if name in self.items:
            print(f"{name}: {self.items[name]}")
        else:
            print(f"{name} not found in inventory.")
    def total_quantity(self):
        total = sum(self.items.values())
        if total!=0:
            print(f"Total quantity of all items: {total}")
            print("The items are:\n" + "\n".join(f"{items}: {quantity}" for items, quantity in self.items.items()))
        else:
            print("Inventory is empty...\nExiting to the iventory menu.")
inventory = Inventory()
while True:
    print("\n\tInventory Menu")
    print("1. Add or Update Item")
    print("2. Retrieve Item Info")
    print("3. Display Total Quantity")
    print("4. Exit")
    choice = input("choose action:")
    if choice == "1":
        name = input("Enter item name: ").strip()
        try:
            quantity = int(input("Enter quantity: "))
            inventory.add_item(name, quantity)
        except ValueError:
            print("Invalid input! Quantity must be a number.")
    elif choice == "2":
        name = input("Enter item name: ").strip()
        inventory.get_item(name)   
    elif choice == "3":
        inventory.total_quantity()
    elif choice == "4":
        print("Exiting inventory system.")
        break
    else:
        print("Invalid choice. Please try again.")
