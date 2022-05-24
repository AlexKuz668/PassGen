import random


# Support def(s)
def number_check(number):
    try:
        int_number = int(number)
        return int_number
    except ValueError:
        return 'False'

# Main defs
def generate_password(chars,length):
    password = ''
    for var in range(length):
        password += random.choice(chars)
    return password

def main():
    chars = input('Enter accepted characters selection\n')
    while chars.isalnum() == False:
        print('It seems you have entered characters that cannot be used')
        chars = input('Enter accepted characters selection\n') 
    length = input('Enter the password length\n')
    length_num = number_check(length)
    while length_num == 'False': 
        print('Write the number, please')
        length = input('Enter the password length\n') 
        length_num = number_check(length) 
    print(generate_password(chars=chars,length=length_num))

if __name__ == '__main__':
    main()
