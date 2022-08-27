# Create an algorithm that generates a random password and saves it to a csv file along with the account details
from if_yes_no import y_n   # returns yes if user inputs y or yeah instead of yes. The same with no and n
import os.path
import random
from csv import DictWriter
from datetime import date


# header names for the csv file we will create to store our data
header_names = ['Account', 'Username', 'Password', 'Date']
today = date.today()

# check if the file already exists and if not, create one.
if os.path.exists('saved_passwords.csv'):
    pass
else:
    with open('saved_passwords.csv', 'w') as my_file:
        writer_h = DictWriter(my_file, fieldnames=header_names)
        writer_h.writeheader()
        my_file.close()

data = {}

# string of all the letters of the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# string of the letters of the alphabet in CAPS
alphabet_caps = alphabet.upper()

# turn the string of the letters into a list
alpha = list(alphabet)

# string -> list of the all CAPS letters
beta = list(alphabet_caps)

# a list of symbols
symbols = ['.', '!', '/', '?', '%', '-']

# an empty list to append numbers to use in the password
gamma = []

for i in range(10):
    gamma.append(i)


# the function that takes random letters, numbers and, if the user agrees,
# symbols(that are always placed as the last character) and generates a password that gets appended to the csv file
def password():
    z = 0

    while z == 0:

        print('Welcome to the random password generator. This will be saved automatically in your CSV file.'
              '(press "q" to quit at anytime!) ')

        # Ask the user how many characters he wants his password to be. Must be a number so handle any Value errors
        while True:
            try:
                x = input('Please enter a number of characters you want your password to be: ').lower()
                x = int(x)
                if x == 0:
                    print("Can't be zero!")
                    continue
                break
            except ValueError:
                if x == 'q':
                    z += 1
                    break
                print('Please only enter a number!')
        if z != 0:
            print('You quit. See you next time!')
            break
        b = {'random': alpha + beta + gamma}
        c = b['random']
        d = []
        random_symbols = random.choice(symbols)  # choose a random symbol from the symbols list
        for i in range(x):
            p = random.choice(c)
            d.append(p)

        without_symbols = "".join(str(v) for v in d)  # makes the items inside the lists into str before joining them
        with_symbols = without_symbols + random_symbols  # adding a random symbol at the end of the string
        # Ask which account it is for. (Facebook,Tweeter,G-mail ect)
        while True:
            password_account = input('Which account is this password for? ')
            if password_account == 'Q':
                z += 1
                break
            if password_account == 'q':
                z += 1
                break
            yes_or_no = input(f'For {password_account} ? ').lower()
            if y_n(yes_or_no) == 'yes':
                break
            elif y_n(yes_or_no) == 'no':
                print("Let's try again.")
            elif yes_or_no == 'q':
                z += 1
                break
            else:
                print("Please answer with yes or no next time. Let's try again. ")
        if z != 0:
            print('You quit. See you next time!')
            break
        # Ask for the account username
        while True:
            account_username = input("What's your account user name? ")
            if account_username == 'q':
                z += 1
                break
            elif account_username == 'Q':
                z += 1
                break
            correct = input(f'Is {account_username} correct? ').lower()
            if y_n(correct) == 'yes':
                break
            elif y_n(correct) == 'no':
                print('Type it again.')
            elif correct == 'q':
                z += 1
                break
            else:
                print("Please answer yes or no. Let's try again.")
        if z != 0:
            print('You quit. See you next time!')
            break
        data['Account'] = password_account
        data['Username'] = account_username

        while True:  # ask the user if they want a symbol at the end of their password or not and print it
            ask_for_symbols = input('Do you want your password to have a random symbol at the end? ').lower()
            if y_n(ask_for_symbols) == 'yes':
                print(with_symbols)
                data['Password'] = with_symbols
                data['Date'] = today
                break
            elif y_n(ask_for_symbols) == 'no':
                print(without_symbols)
                data['Password'] = without_symbols
                data['Date'] = today
                break
            elif ask_for_symbols == 'q':
                z += 1
                break
            else:
                print('Answer yes or no please. ')
        if z != 0:
            print('You quit. See you next time!')
            break

        # open the csv file and add the new data to it
        with open('saved_passwords.csv', 'a') as my_file_2:
            writer_o = DictWriter(my_file_2, fieldnames=header_names)
            writer_o.writerow(data)
            my_file_2.close()
        break


password()
