import random
print("======================================================================")
print()
print()
text = input(" Welcome to Password generator! please enter to random your password!")
print()
print()
print("                       V                               ")
print()
def number():
    return str(random.randint(0, 9)) 

def alpha():
    return chr(random.randint(65, 65 + 26 - 1))

def symbol():
    cs = ['!', '?', '@', '#', '&', ';', ':']
    i = random.randint(0, 6)
    return cs[i]
# The following lines of code were adapted from [1]

option_length = input("enter password length (default 6-12) (optional) : ")
if option_length.isdigit():
    l = int(option_length)
else:
    l = random.randint(6, 12)

include_capital = input("include capital character ('n' for no): ") != 'n'
include_number = input("include number character ('n' for no): ")  != 'n'
include_symbol = input("include symbol character ('n' for no): ") != 'n'

password = []
# The following lines of code were adapted from [2]
if include_capital:
    password.append(alpha())
if include_number:
    password.append(number())
if include_symbol:
    password.append(symbol())

while len(password) != l:
    type = random.randint(1, 4)
    if type == 1 and include_number:
        password.append(number())
    elif type == 2 and include_capital:
        password.append(alpha())
    elif type == 3 and include_symbol:
        password.append(alpha().lower())
    else:
        password.append(alpha().lower())
# The following lines of code were adapted from [3]

print() 
print()
print(''.join(password))
print()
print("======================================================================")
