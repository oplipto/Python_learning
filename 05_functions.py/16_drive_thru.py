def get_item(item_number):
    items = {
        1: '🍔 Cheeseburger',
        2: '🍟 Fries',
        3: '🥤 Soda',
        4: '🍦 Ice Cream',
        5: '🍪 Cookie'
    }

    return items.get(item_number, 'Invalid item number')

def welcome():
    print('Welcome to the drive-thru!')
    print('Here are the items on the menu:')
    print('1. Cheeseburger')
    print('2. Fries')
    print('3. Soda')
    print('4. Ice Cream')
    print('5. Cookie')
    print('6. Quit')


def main():
    welcome()
    while True:
        choice = int(input('Enter the item number you want to order: '))
        if choice == 6:
            print('Thank you for visiting the drive-thru!')
            break
        
        else:
            try:
                item_number = int(choice)
                
                if 1 <= item_number <= 5:
                   item_name = get_item(item_number)
                   print(f'You ordered: {item_name}')

                else:
                    print('Invalid Choice - Please enter a number between 1 and 5')

            except ValueError:
                
                print('Invalid input - Please enter a number between 1 and 5')


if __name__ == "__main__":
    main()

