# Robin Anstett
def encoder(pword):
    encoded_str = ''
    for digit in pword:
        temp = int(digit) + 3
        encoded_str += str(temp)
    return encoded_str

if __name__ == '__main__':
    running = True
    while running:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        option = int(input('Please enter an option: '))

        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            running = False
        else:
            print('Invalid option! Please select option 1, 2, or 3.')
