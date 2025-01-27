class VendingMachine:
    def __init__(self):
        self.categories = {
            "Drinks": {
                "1": {"name": "Coke", "price": 1.50, "stock": 9},
                "2": {"name": "Water", "price": 1.00, "stock": 9},
                "3": {"name": "Coffee", "price": 2.50, "stock": 10},
                "7": {"name": "Apple Juice", "price": 2.00, "stock": 8},
                "8": {"name": "Orange Juice", "price": 1.80, "stock": 10}
            },
            "Snacks": {
                "4": {"name": "Chips", "price": 1.20, "stock": 8},
                "5": {"name": "Chocolate", "price": 2.00, "stock": 7},
                "6": {"name": "Biscuits", "price": 1.50, "stock": 10},
                "9": {"name": "Peanut Bar", "price": 1.75, "stock": 6},
                "10": {"name": "Chocolate Cookies", "price": 2.25, "stock": 5}
            }
        }

    def display_menu(self):
        print("\n--- Vending Machine Menu ---")
        for category, items in self.categories.items():
            print(f"\n{category}:")
            for code, item in items.items():
                print(f"  [{code}] {item['name']} - ${item['price']} ({item['stock']} in stock)")
    def select_item(self, code):
        for category, items in self.categories.items():
            if code in items:
                return items[code]
        return None

    def update_stock(self, code):
        for category in self.categories.values():
            if code in category:
                category[code]["stock"] -= 1
    def suggest_item(self, selected_code):
        if selected_code in self.categories["Drinks"]:
            return "Would you like to have some chocolates with your drink? (Code: 5)"
        elif selected_code in self.categories["Snacks"]:
            return "How about having a refreshing coffee? (Code: 3)"
        return ""

    def run(self):
        while True:
            self.display_menu()
            code=input("\nEnter the code of the item you want to purchase (or 'N' to quit): ")
            if code.lower() == 'n':
                print("Thank you. Feel free to make yourself comfortable by using the vending machine!")
                break

            item=self.select_item(code)
            if not item:
                print("Invalid code. Please try again.")
                continue
            if item["stock"] <= 0:
                print(f"Sorry, {item['name']} is out of stock.")
                continue
            print(f"You selected {item['name']} which costs ${item['price']:.2f}.")
            money=float(input("Insert money: $"))

            if money < item["price"]:
                print("Insufficient funds. Transaction failed. Please retrieve your money.")
                continue

            change=money - item["price"]
            self.update_stock(code)
            print(f"Dispensing {item['name']}... Enjoy!")
            print(f"Your change is ${change:.2f}.")

            suggestion = self.suggest_item(code)
            if suggestion:
                print(suggestion)

# Run the vending machine
vending_machine = VendingMachine()
vending_machine.run()