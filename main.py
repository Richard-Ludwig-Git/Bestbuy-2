import product, store

product_list = [ product.Product("MacBook Air M2", price=1450, quantity=100),
                 product.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 product.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start():
    """Main Menu to run the user-choice funconality"""
    menu = {
        "1": best_buy.get_all_products,
        "2": best_buy.get_total_quantity,
        "3": make_order,
        "4": exit
    }
    while True:
        print("   Store Menu\n   ----------\n1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Quit")
        user_menu_choice = str(input("Please choose a number: "))
        menu[user_menu_choice]()


def make_order():
    """User order, with input validation and sumup"""
    best_buy.get_all_products()
    print("When you want to finish order, enter empty text")
    ordering = True
    total_payment = 0
    while ordering:
        userproduct_choice = input("Which product # do you want? ")
        userproduct_quantity = input("What amount do you want? ")
        if userproduct_quantity == "" and userproduct_quantity == "":
            ordering = False
            break
        if int(userproduct_quantity) > best_buy.in_store[int(userproduct_choice)-1].get_quantity():
            print(f"Sorry there are only {best_buy.in_store[int(userproduct_choice)-1].get_quantity()} in Stock left")
            continue
        if int(userproduct_choice) - 1 not in range(len(best_buy.in_store)):
            print("Error adding product to Cart")
            continue
        total_payment += best_buy.in_store[int(userproduct_choice)-1].buy(int(userproduct_quantity))
        print("Product added to Cart")
    print(f"--------------------------\nOrder made. Total amount {total_payment}€\n--------------------------\n")


def main():
    """Main function to start the program"""
    start()


if __name__ == "__main__":
    main()