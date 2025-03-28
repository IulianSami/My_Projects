#8. 🛍️🏷️🛒  Meniu magazin cu introducere articole in inventar, modificare inventar si cumparare.
  
# --------------------------------------
#           Store Menu
# --------------------------------------
# 1. Enter inventory
# 2. Delete or modify product from inventory
# 3. View products
# 4. Add product to cart
# 5. View cart
# 6. Complete order
# 7. Exit
# --------------------------------------
# Choose an option:


from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Shopping cart (initially empty)
cart = {}

# List of products added to inventory and available with stock
products = {}

# Function to enter inventory
def initialize_inventory():
    global products
    print(Fore.CYAN + "Enter the available products in the store.")
    
    while True:
        name = input(Fore.YELLOW + "Product name (or 'stop' to finish): ").strip()
        if name.lower() == "stop":
            break
        
        try:
            price = float(input(Fore.YELLOW + f"Price for {name}: "))
            stock = int(input(Fore.YELLOW + f"Stock for {name}: "))
            products[name] = {"price": price, "stock": stock}
            print(Fore.GREEN + f"Product {name} has been successfully added!\n")
        except ValueError:
            print(Fore.RED + "Invalid data! Please enter a valid price and stock.")

# Function to delete or modify products
def modify_product():
    if not products:
        print(Fore.RED + "No products in inventory. Please enter inventory first.")
        return
    
    print(Fore.GREEN + "\nAvailable products:")
    for index, (product, info) in enumerate(products.items(), start=1):
        print(Fore.YELLOW + f"{index}. {product} - {info['price']} RON (Stock: {info['stock']})")
    
    product_name = input(Fore.YELLOW + "\nEnter the name of the product you want to modify or 'stop' to cancel: ").strip()
    if product_name.lower() == "stop":
        return

    if product_name in products:
        sub_option = input(Fore.YELLOW + "Do you want to modify the quantity or price? (quantity/price): ").strip().lower()
        
        if sub_option == "quantity":
            try:
                quantity = int(input(Fore.YELLOW + f"Enter the new quantity for {product_name}: "))
                if quantity >= 0:
                    products[product_name]["stock"] = quantity
                    print(Fore.GREEN + f"Stock for {product_name} has been updated to {quantity}.")
                else:
                    print(Fore.RED + "Quantity cannot be negative.")
            except ValueError:
                print(Fore.RED + "Please enter a valid quantity.")
        elif sub_option == "price":
            try:
                new_price = float(input(Fore.YELLOW + f"Enter the new price for {product_name}: "))
                if new_price > 0:
                    products[product_name]["price"] = new_price
                    print(Fore.GREEN + f"Price for {product_name} has been updated to {new_price} RON.")
                else:
                    print(Fore.RED + "Price must be positive.")
            except ValueError:
                print(Fore.RED + "Please enter a valid price.")
        else:
            print(Fore.RED + "Invalid option.")
    else:
        print(Fore.RED + "Product does not exist in inventory.")

# Function to view available products
def show_products():
    if not products:
        print(Fore.RED + "No products in inventory.")
        return
    
    print(Fore.GREEN + "\nAvailable products:")
    for index, (product, info) in enumerate(products.items(), start=1):
        print(Fore.YELLOW + f"{index}. {product} - {info['price']} RON (Stock: {info['stock']})")

# Function to add products to cart
def add_to_cart():
    if not products:
        print(Fore.RED + "No products in inventory.")
        return
    
    show_products()
    
    try:
        choice = int(input(Fore.YELLOW + "\nChoose the product number to add to cart: "))
        if 1 <= choice <= len(products):
            product_name = list(products.keys())[choice - 1]
            quantity = int(input(Fore.YELLOW + f"How many {product_name} do you want to add to the cart? "))
            if quantity <= products[product_name]["stock"]:
                cart[product_name] = cart.get(product_name, 0) + quantity
                products[product_name]["stock"] -= quantity
                print(Fore.GREEN + f"{quantity} pieces of {product_name} have been added to the cart!")
            else:
                print(Fore.RED + "Insufficient stock.")
        else:
            print(Fore.RED + "Invalid option.")
    except ValueError:
        print(Fore.RED + "Please enter a valid number.")

# Function to remove products from cart
def remove_from_cart():
    if not cart:
        print(Fore.RED + "Cart is empty.")
        return
    
    print(Fore.GREEN + "\nProducts in cart:")
    for index, (product, quantity) in enumerate(cart.items(), start=1):
        print(Fore.YELLOW + f"{index}. {product} - {quantity} pieces")
    
    try:
        choice = int(input(Fore.YELLOW + "\nChoose the product number to remove: "))
        product_name = list(cart.keys())[choice - 1]
        remove_quantity = int(input(Fore.YELLOW + f"How many pieces to remove? (0 to cancel): "))
        if remove_quantity >= cart[product_name]:
            products[product_name]["stock"] += cart.pop(product_name)
        else:
            cart[product_name] -= remove_quantity
            products[product_name]["stock"] += remove_quantity
    except:
        print(Fore.RED + "Error while removing.")

# Main function
def main():
    while True:
        print(Fore.YELLOW + "\n1. Enter inventory\n2. Modify product\n3. View products\n4. Add product to cart\n5. Remove product from cart\n6. Exit")
        try:
            option = int(input(Fore.YELLOW + "Choose: "))
            if option == 1:
                initialize_inventory()
            elif option == 2:
                modify_product()
            elif option == 3:
                show_products()
            elif option == 4:
                add_to_cart()
            elif option == 5:
                remove_from_cart()
            elif option == 6:
                print(Fore.GREEN + "Goodbye!")
                break
        except:
            print(Fore.RED + "Invalid option.")

if __name__ == "__main__":
    main()
