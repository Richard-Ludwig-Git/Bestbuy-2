import product

class Store:
    """handles the key methods and init for the store and holds products"""
    in_store = []
    def __init__(self, item_list):
        """init of the store list"""
        self.in_store = item_list


    def remove_product(self, product_to_delete):
        """delete a product from the store(list)"""
        if product in Store.in_store:
            Store.in_store.remove(product_to_delete)


    def get_total_quantity(self):
        """getter for the total amount of products in the store"""
        total_quantity = 0
        for item in self.in_store:
            total_quantity += item.quantity
        print("--------------------------------------------")
        print(f"Total of {total_quantity} items in store")
        print("--------------------------------------------")


    def get_all_products(self):
        """getter for all products, active in the store"""
        active_products = []
        print("-------------------------------------------------------")
        counter = 1
        for item in self.in_store:
            if item.is_active():
                active_products.append(item)
                print(f"{counter}. ", end="")
                item.show()
                counter += 1

        print("-------------------------------------------------------")


    def order(self, shopping_list):
        """sumup of the total order price, out of the shopping list"""
        total_price = 0
        for item in shopping_list:
            total_price += item[0].buy(item[1])
        return total_price