import random

game_over = False

word_list = ["aardvark","monkey", "camel"]
chosen_word = random.choice(word_list)

placeholder = ""
lenght = len(chosen_word)

for position in range (lenght):
    placeholder += "_"

correct_order = []
lives = 6

while not game_over:
    guess = input("Guess the latter:").lower()

    if guess in correct_order:
        print(f"You have guessed this latter: {guess}")

    display = ""

    for latter in chosen_word:
        if latter == guess:
            display += latter  
            correct_order.append(latter)          

        elif latter in correct_order:
            display += latter

        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1
        print("You gueesed wrong, ouch.")
        print(f'Remaning lives at {lives}')
    elif lives == 0:
        print("You lose.")
        game_over = True
    
    print(display)

    if "_" not in display:
        game_over = True
        print("You win!")
            