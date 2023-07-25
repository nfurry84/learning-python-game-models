
from board_games.Tic_Tac_Toe_Engine import Tic_Tac_Toe_Engine
from cards import War

GAME_MENU_DICTIONARY = {'1': 'Tic Tac Toe',
                        '2': 'War',
                        '3': 'Thermonuclear War'}


def main():
    print('Would you like to play a game?')
    cycle_on = True
    while cycle_on:
        print_game_menu()
        selection = make_selection()
        match selection:
            case '1':
                cycle_on = False
                Tic_Tac_Toe_Engine().start_game()
            case '2':
                cycle_on = False
                War().start_game()
            case '3':
                print('Access Denied')
            case _:
                pass


def make_selection():
    valid_entries = GAME_MENU_DICTIONARY.keys()
    choice = ''
    while choice not in valid_entries:
        choice == input()
        if choice not in valid_entries:
            print('Invalid selection please try again')
        else:
            pass

    return choice


def print_game_menu():
    for menu_item in GAME_MENU_DICTIONARY:
        print(f'{menu_item.key}. {menu_item.value}')
    print('')
    print('')



if __name__ == '__main__':
    main()
