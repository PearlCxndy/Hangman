

import random


def load_words(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    f.close()
    return lines
    

def trim_lines(lines):
    s = []
    for line in lines:
        s.append(line.strip())
    return s

while True:
    word_file = "hangman_words.txt"
    init_hp = 3
    hp = init_hp
    total_score = 0



    words = trim_lines(load_words(word_file))

    word = words[random.randint(0, len(words) - 1)].lower()
    print()
    print("============================================================================")


    guess = [" "]

    while hp > 0:

        hint = []
        
        for c in word:
            
            if c in guess:
                hint.append(c)
            else: 
                hint.append("_")
        
        print(" ".join(hint))
        print()

        if "_" not in hint:
            break

        c = input("enter characters : ")
        if len(c) != 1:
            print("Please type only one character.")
            print()
            continue

        if c in word:
            guess.append(c)
        else: 
            hp = hp - 1

        print(f"Your hp is now {hp}! ")
    if hp > 0:
        score = len(word) + hp
        total_score += score
        print(f"score is {score} ")
        print(f"total score is {total_score} " )
    else:
        print(f"lose! the answer is {word}")
    if input("enter 'q' for quit:") == 'q':
       break;