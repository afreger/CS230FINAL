def show_inventory(stock):
    for product, quantity in stock.items():
        print(f'{quantity} {product}')

def main():
    stock = {'shirts': 25, 'pants': 19, 'sweaters': 5}

    while True:
        item_name = input("Enter item: ").strip().lower()

        if item_name == '*':
            show_inventory(stock)
        elif item_name in stock:
            print(f'{stock[item_name]} {item_name}')
        elif item_name == '':
            print('End of input')
            break
        else:
            print(f'{item_name.capitalize()} is not in the inventory.')

main()

