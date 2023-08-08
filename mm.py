class SnackInventory:
    def __init__(self):
        self.inventory = {}


    def add_snack(self, snack_id, name, price):
        if snack_id in self.inventory:
            print("Snack ID already exists. Please choose a different ID.")
        else:
            self.inventory[snack_id] = {'name': name, 'price': price, 'availability': 'yes'}
            print(f"Snack '{name}' with ID {snack_id} added to inventory.")


    def remove_snack(self, snack_id):
        if snack_id in self.inventory:
            snack_name = self.inventory[snack_id]['name']
            del self.inventory[snack_id]
            print(f"Snack '{snack_name}' with ID {snack_id} removed from inventory.")
        else:
            print("Snack ID not found in inventory.")

    def update_availability(self, snack_id, availability):
        if snack_id in self.inventory:
            self.inventory[snack_id]['availability'] = availability
            print(f"Availability of snack with ID {snack_id} updated to '{availability}'.")
        else:
            print("Snack ID not found in inventory.")

    def display_inventory(self):
        print("Snack Inventory:")
        print("{:<10} {:<20} {:<10} {:<12}".format("ID", "Name", "Price", "Availability"))
        print("=" * 50)
        for snack_id, snack_info in self.inventory.items():
            print("{:<10} {:<20} ${:<10.2f} {:<12}".format(snack_id, snack_info['name'], snack_info['price'],
                                                          snack_info['availability']))

    def sell_snack(self, snack_id):
        if snack_id in self.inventory:
            if self.inventory[snack_id]['availability'] == 'yes':
                snack_name = self.inventory[snack_id]['name']
                self.inventory[snack_id]['availability'] = 'no'
                print(f"Sold one {snack_name}.")
            else:
                print("Snack is not available for sale.")
        else:
            print("Snack ID not found in inventory.")


def main():
    inventory = SnackInventory()

    while True:
        print("\nMumbai Munchies: The Canteen Chronicle")
        print("1. Add Snack")
        print("2. Remove Snack")
        print("3. Update Snack Availability")
        print("4. Display Inventory")
        print("5. Sell Snack")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            snack_id = input("Enter Snack ID: ")
            name = input("Enter Snack Name: ")
            price = float(input("Enter Snack Price: "))
            inventory.add_snack(snack_id, name, price)

        elif choice == '2':
            snack_id = input("Enter Snack ID: ")
            inventory.remove_snack(snack_id)

        elif choice == '3':
            snack_id = input("Enter Snack ID: ")
            availability = input("Enter Availability (yes/no): ")
            inventory.update_availability(snack_id, availability)

        elif choice == '4':
            inventory.display_inventory()

        elif choice == '5':
            snack_id = input("Enter Snack ID: ")
            inventory.sell_snack(snack_id)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
