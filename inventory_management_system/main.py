class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def authenticate(self, username, password):
        return self.username == username and self.password == password

# Product Class
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity_change):
        new_quantity = self.stock_quantity + quantity_change
        if new_quantity < 0:
            print(f"Cannot reduce stock below zero for {self.name}. Available: {self.stock_quantity}")
            return False
        self.stock_quantity = new_quantity
        print(f"Stock for {self.name} updated. New quantity: {self.stock_quantity}")
        return True

users = []
products = {}

# Helper Functions
def safe_input(prompt, cast_func=int):
    while True:
        try:
            return cast_func(input(prompt))
        except ValueError:
            print("Invalid input, please try again.")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    for user in users:
        if user.authenticate(username, password):
            print(f"Welcome {username}!")
            return user
    print("Invalid credentials")
    return None

def register_user():
    while True:
        username = input("Enter new username: ")
        if any(user.username == username for user in users):
            print("Username already taken! Try again.")
            continue
        password = input("Enter new password: ")
        
        print("Select role:\n1. Admin\n2. User")
        role_choice = safe_input("Choose an option (1 or 2): ")
        if role_choice == 1:
            role = "Admin"
        elif role_choice == 2:
            role = "User"
        else:
            print("Invalid choice, please select 1 for Admin or 2 for User.")
            continue
        
        users.append(User(username, password, role))
        print("User registered successfully!")
        break

# Admin Functions
def add_product(admin_user):
    if admin_user.role != "Admin":
        print("Permission denied!")
        return
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    category = input("Enter category: ")
    price = safe_input("Enter price: ", float)
    stock_quantity = safe_input("Enter stock quantity: ")
    products[product_id] = Product(product_id, name, category, price, stock_quantity)
    print(f"Product {name} added successfully.")

def adjust_stock(admin_user):
    if admin_user.role != "Admin":
        print("Permission denied!")
        return
    product_id = input("Enter product ID to adjust stock: ")
    if product_id in products:
        quantity_change = safe_input("Enter quantity to add (positive) or remove (negative): ")
        products[product_id].update_stock(quantity_change)
    else:
        print("Product not found.")

def delete_product(admin_user):
    if admin_user.role != "Admin":
        print("Permission denied!")
        return
    product_id = input("Enter product ID to delete: ")
    if product_id in products:
        del products[product_id]
        print("Product deleted.")
    else:
        print("Product not found.")

def check_stock():
    for product in products.values():
        if product.stock_quantity < 10:
            print(f"Low stock alert: {product.name}")

def view_products():
    if not products:
        print("No products available.")
    else:
        for product in products.values():
            print(f"{product.product_id}: {product.name} ({product.category}) - {product.price}Rs, Stock: {product.stock_quantity}")

def search_product():
    search_name = input("Enter product name to search: ").lower()
    found = False
    for product in products.values():
        if search_name in product.name.lower():
            print(f"{product.product_id}: {product.name} ({product.category}) - {product.price}Rs, Stock: {product.stock_quantity}")
            found = True
    if not found:
        print("Product not found.")

# User Function
def buy_product(user):
    if user.role != "User":
        print("Permission denied!")
        return
    product_id = input("Enter product ID to buy: ")
    if product_id in products:
        quantity = safe_input("Enter quantity to buy: ")
        product = products[product_id]
        if product.update_stock(-quantity):  # Reduce stock by the purchased quantity
            total_price = quantity * product.price
            print(f"Invoice:\nProduct: {product.name}\nQuantity: {quantity}\nTotal: {total_price}Rs")
            if product.stock_quantity < 10:
                print(f"Low stock alert: {product.name}")
    else:
        print("Product not found.")

# Main Loop
def main():
    print("Welcome to the Inventory Management System!")
    while True:
        print("\n1. Login")
        print("2. Register New User")
        print("3. Exit")
        choice = safe_input("Choose an option: ")
        
        if choice == 1:
            user = login()
            if not user:
                continue

            if user.role == "Admin":
                while True:
                    print("\n--- Admin Menu ---")
                    print("1. Add Product")
                    print("2. View Products")
                    print("3. Delete Product")
                    print("4. Adjust Stock")
                    print("5. Check Stock Levels")
                    print("6. Search Product")
                    print("7. Logout")

                    choice = safe_input("Choose an option: ")

                    if choice == 1:
                        add_product(user)
                    elif choice == 2:
                        view_products()
                    elif choice == 3:
                        delete_product(user)
                    elif choice == 4:
                        adjust_stock(user)
                    elif choice == 5:
                        check_stock()
                    elif choice == 6:
                        search_product()
                    elif choice == 7:
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")

            elif user.role == "User":
                while True:
                    print("\n--- User Menu ---")
                    print("1. View Products")
                    print("2. Buy Product")
                    print("3. Check Stock Levels")
                    print("4. Search Product")
                    print("5. Logout")

                    choice = safe_input("Choose an option: ")

                    if choice == 1:
                        view_products()
                    elif choice == 2:
                        buy_product(user)
                    elif choice == 3:
                        check_stock()
                    elif choice == 4:
                        search_product()
                    elif choice == 5:
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        
        elif choice == 2:
            register_user()
        
        elif choice == 3:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
