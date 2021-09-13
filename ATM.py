print()
print()

import random
print()

print("WELCOME TO ATM BANKING MACHINE!")
print()

pin = "1234"
print()

max_incorrect = 3

def ensureInputInt(message):
    while True:
        txt = input(message)
        if txt.isdigit():
            return int(txt)

def main():

    incorrect_count = 0

    while True:
        user_pin = input("please input your pin here: ")
        if user_pin == pin:
            break
        incorrect_count = incorrect_count + 1
        if incorrect_count == max_incorrect:
            print("card has been retained")
            return

        else:
            print("wrong pin , try again!")
    
    balance = random.randint(100, 1000)

    while True:
        print("--------------------------")

        todo = input(
            "1 check your balance\n" + 
            "2 withdraw the money\n" +
            "3 deposit the money\n" +
            "4 exit\n" + 
            "Please select the option : "
        )

        if todo == "1":
            print(f"balance is: £ {balance}")
        elif todo == "2":
            amount = ensureInputInt("withdraw amount: ")
            if balance - amount >= 0:
                balance = balance - amount
            else:
                print("cannot withdraw!")
        elif todo == "3":
            amount = ensureInputInt("deposit amount: ")
            balance = balance + amount
        
                
        elif todo == "4":
            return
        else:
            print("command not found")
print("--------------------------")    

main()