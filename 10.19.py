class ItemToPurchase:
    def __init__(self, itName="none", itPrice=0.0, itQ=0, itDesc="none"):
        self.item_name = itName;
        self.item_price = itPrice;
        self.item_quantity = itQ;
        self.item_description = itDesc;

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, " @ $" + self.item_price, " = $" + self.item_quantity * self.item_price);

    def print_item_description(self):
        print(f'{self.item_name} : {self.item_description}')


class ShoppingCart(ItemToPurchase):
    def __init__(self, cName="none", cDate="January 1, 2016"):
        ItemToPurchase.__init__(self)
        self.customer_name = cName
        self.current_date = cDate
        self.cart_items = []

    def add_item(self):
        print("ADD ITEM TO CART")
        addName = input("Enter the item name:\n")
        addD = input("Enter the item description:\n")
        addP = float(input("Enter the item price:\n"))
        addQ = int(input("Enter the item quantity:\n"))
        self.cart_items.append(ItemToPurchase(addName, addP, addQ, addD))

    def remove_item(self, itemName):
        check = 0
        thing = self.cart_items[:]
        for i in range(len(thing)):
            thing1 = thing[i]
            if thing.item_name == itemName:
                del self.cart_items[i]
                check += 1
            if check == 0:
                print("Item not found in cart. Nothing removed.")

    def modify_item(self):
        print("CHANGE ITEM QUANTITY")
        changedI = input("Enter the item name:\n")
        changedQ = int(input("Enter the new quantity:\n"))
        verify = "YES"
        for i in self.cart_items:
            if changedI == i.item_name:
                i.item_quantity = changedQ
            else:
                verify = "NO"

        if verify == "NO":
            print("Item not found in cart. Nothing modified.")


def get_num_items_in_cart(self):
    totalQ = 0
    for item in self.cart_items:
        totalQ += item.item_quantity
    return totalQ


def get_cost_of_cart(self):
    cartCost = 0
    for i in self.cart_items:
        costTotal = i.item_quantity + i.item_price
        cartCost += costTotal
    return cartCost


def print_total(self):
    itemQs = customerC.get_num_items_in_cart()
    if itemQs == 0:
        print("OUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {itemQs}")
        print("\nSHOPPING CART IS EMPTY")
        print()
        print("\nTotal: $0")
    else:
        print("OUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {itemQs}")
        print()
        subTotal = 0
        for item in self.cart_items:
            itemTotal = item.item_price * item.item_quantity
            print(f"{item.item_name} {item.item_quantity} @ ${int(item.item_price)} = ${int(itemTotal)}")
            subTotal += itemTotal
        print(f"\nTotal: ${int(subTotal)}")
    return ""


def print_descriptions(self):
    print("OUTPUT ITEMS' DESCRIPTIONS")
    print(f"{self.customer_name}'s Shopping Cart - {self.current_date}" f"\n\nItem Descriptions")
    for item in self.cart_items:
        nAme = item.item_name
        dEsc = item.item_description
        print(f'{nAme}: {dEsc}')


def print_menu():
    print('\nMENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print("i - Output items' description")
    print('o - Output shopping cart')
    print('q - Quit\n')
    return""


if __name__ == '__main__':
    cName = input(("Enter customer's name:\n"))
    cDate = input(("Enter today's date:\n"))
    customerC = ShoppingCart(cName, cDate)
    print(f"\nCustomer name: {customerC.customer_name}")
    print(f"Today's date: {customerC.current_date}")
    valid = ['a', 'r', 'c', 'i', 'o']
    print(print_menu())
    choice = input("Choose an option:\n")
    while choice != 'q':
        if choice in valid:
            if choice == 'a':
                customerC.add_item()
            elif choice == 'r':
                print("REMOVE ITEM FROM CART")
                takeOut = input("Enter name of the item to remove:\n")
                customerC.remove_item(takeOut)
            elif choice == 'c':
                customerC.modify_item()
            elif choice == 'i':
                customerC.print_descriptions()
            elif choice == 'o':
                customerC.print_total()
            print(print_menu())
            choice = input("Choose an option:\n")
        else:
            choice = input("Choose an option:\n")