#UHID 2037080
#Paul Brzozowski
#Fall 2022



# creating class and defining ItemToPurchase
class ItemToPurchase:
    # default constructor that sets variable values to default
    def init(self):
        self.item_name = 'None'
        self.item_price = int(0)
        self.item_quantity = int(0)

    # print_item_cost prints out cost of items
    def print_item_cost(self):
        print(self.item_name + ' ' + str(self.item_quantity) + ' @ $' + str(self.item_price) + ' = $' + str(self.item_price * self.item_quantity))


# creating objects for item 1 and item 2
item_1 = ItemToPurchase()
item_2 = ItemToPurchase()

if __name__ == '__main__':
    # asks for input for item 1
    print('Item 1')
    item_1.item_name = input('Enter the item name:\n')
    item_1.item_price = int(input('Enter the item price:\n'))
    item_1.item_quantity = int(input('Enter the item quantity:\n'))
    print()

    # asks for input for item 2
    print('Item 2')
    item_2.item_name = input('Enter the item name:\n')
    item_2.item_price = int(input('Enter the item price:\n'))
    item_2.item_quantity = int(input('Enter the item quantity:\n'))
    print()

    # prints total cost for item 1 and item 2 separately
    print('TOTAL COST')
    item_1.print_item_cost()
    item_2.print_item_cost()

    # adds item 1 and item 2 costs for total
    total = item_1.item_price * item_1.item_quantity + item_2.item_price * item_2.item_quantity

    print()
    print('Total: $' + str(total))