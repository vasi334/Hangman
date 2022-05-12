ui_prompt = """
Choose action.
- 'n' for start playing
- 'q' for quit the game
Your action: """

w = 'vasi'

stick_man = [
    """
    _______
    |     |
    |     o
    |     
    |""",

    """
    _______
    |     |
    |     o
    |     |
    |""",

    """
    _______
    |     |
    |     o
    |     |\\
    |""",

    """
    _______
    |     |
    |     o
    |    /|\\
    |""",

    """
    _______
    |     |
    |     o
    |    /|\\
    |    /
    """,

    """
    _______
    |     |
    |     o
    |    /|\\
    |    / \\
    """
]


def restart_game():
    a = input(ui_prompt)
    b = 6
    c = 0
    d = []
    return a, b, c, d

def game(word):
    contor = 6
    contor_stick_man = 0
    list_of_letters = []
    ui = input(ui_prompt)

    while contor > 0 and ui != 'q' and ui == 'n':
        letter = input('Type a letter: ')
        letters_guessed = 0
        if len(letter) == 1:
            if letter in list_of_letters:
                print('You already said that', end=" ")
            elif letter not in word:
                print('Wrong!', end=" ")
                contor -= 1
                list_of_letters.append(letter)
                print(stick_man[contor_stick_man])
                contor_stick_man += 1
            else:
                print("Good!")
                list_of_letters.append(letter)
                for letter in word:
                    if letter in list_of_letters:
                        print(letter, end=" ")
                        letters_guessed += 1
                    else:
                        print('_', end=" ")
        print("\n")
        if letters_guessed == len(word):
            print('\nCongratulations! You won!')
            ui, contor, contor_stick_man, list_of_letters = restart_game()

        if contor == 0:
            print('\nYou lost!')
            ui, contor, contor_stick_man, list_of_letters = restart_game()


game(w)
