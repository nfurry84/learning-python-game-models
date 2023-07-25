class Tic_Tac_Toe_Engine:
    """
    Tic Tac Toe game engine
    """
    board_row_template = [' ', ' ', ' ']

    def __init__(self):
        self.game_board = [list(self.board_row_template),
                           list(self.board_row_template),
                           list(self.board_row_template)]
        self.board_map = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
        self.positions = list(range(1, 10))
        self.settings = {'Player1': 'X', 'Player2': 'O'}

    def start_game(self):
        """
        Starts the tic tac toe game
        :return:
        """
        game_engine_running = True
        while game_engine_running:
            # Initialize a new game
            self.new_game()
            turn_counter = 0
            current_player = 'Player1'
            game_in_progress = True
            # Output current state to console - Should be new empty grid
            self.show_game_state()
            # Begin actual game loop
            while game_in_progress:
                self.take_turn(current_player) # Handle Player turn.
                turn_counter += 1
                self.show_game_state()

                # Check for win and End Game conditions
                # Game requires at minimum 5 turns to actually win.
                # No point in validating until at least 5 turns are played
                if turn_counter >= 5:
                    we_have_a_winner = self.did_player_win()
                    if we_have_a_winner:
                        print(f'{current_player} has won this game')
                        game_in_progress = False
                    elif self.is_board_full():
                        print('GAME OVER! Draw!')
                        game_in_progress = False

                # Switch player
                if current_player == 'Player1':
                    current_player = 'Player2'
                else:
                    current_player = 'Player1'

            game_engine_running = self.play_again()

    def take_turn(self, current_player):
        """

        :param current_player: name of current player should be 'Player1' or 'Player2'
        :return:
        """
        invalid_or_no_choice = True
        while invalid_or_no_choice:
            choice = input(f"{current_player} select an empty space or help or ? for help ")

            if choice.lower() == 'help' or choice == '?':
                print('Select an available position using the numpad coordinates')
                print(self.board_map[0])
                print(self.board_map[1])
                print(self.board_map[2])
                continue

            if choice.isdigit():
                selected_index = int(choice)
                if selected_index not in self.positions:
                    print('selected location has already been filled')
                    print('please try again.')
                else:
                    self.positions.pop(self.positions.index(selected_index))
                    symbol = self.settings[current_player]
                    y_dex = 0
                    if selected_index in self.board_map[0]:
                        invalid_or_no_choice = False
                        y_dex = self.board_map[0].index(selected_index)
                        self.game_board[0][y_dex] = symbol
                    elif selected_index in self.board_map[1]:
                        invalid_or_no_choice = False
                        y_dex = self.board_map[1].index(selected_index)
                        self.game_board[1][y_dex] = symbol
                    elif selected_index in self.board_map[2]:
                        invalid_or_no_choice = False
                        y_dex = self.board_map[2].index(selected_index)
                        self.game_board[2][y_dex] = symbol
                    else:
                        pass
            else:
                print('Selection must be a valid number between '
                      '1-9 and be a valid position in the board')

    def did_player_win(self):
        """
        Checks the current state of the game to see if a player has one or the game board is full
        :return: 0 for in progress, 1 for Player win or 2 for a Draw
        """

        board_matrix = self.game_board
        has_won = False
        # Diagonal
        has_won = has_won or self.validate_three(board_matrix[0][0],
                                                       board_matrix[1][1],
                                                       board_matrix[2][2])
        has_won = has_won or self.validate_three(board_matrix[2][0],
                                                       board_matrix[1][1],
                                                       board_matrix[0][2])
        # Horizontal
        has_won = has_won or self.validate_three(board_matrix[0][0],
                                                       board_matrix[0][1],
                                                       board_matrix[0][2])
        has_won = has_won or self.validate_three(board_matrix[1][0],
                                                       board_matrix[1][1],
                                                       board_matrix[1][2])
        has_won = has_won or self.validate_three(board_matrix[2][0],
                                                       board_matrix[2][1],
                                                       board_matrix[2][2])
        # Vertical
        has_won = has_won or self.validate_three(board_matrix[0][0], board_matrix[1][0], board_matrix[2][0])
        has_won = has_won or self.validate_three(board_matrix[0][1], board_matrix[1][1], board_matrix[2][1])
        has_won = has_won or self.validate_three(board_matrix[0][2], board_matrix[1][2], board_matrix[2][2])

        if has_won:
            return 1

         return 0

    def validate_three(self, point1, point2, point3):
        """
        Checks if a player has a winning condition across 3 boxes
        :param point1: Value of first cell
        :param point2: Value of second cell
        :param point3: Value of third cell
        :return: Boolean indicating if all cells match and non-empty)
        """
        if point1 == ' ' or point2 == ' ' or point3 == ' ':
            return False
        elif len(set([point1, point2, point3])) == 1:  # getting unique values for row,
            return True
        else:
            return False

    def is_board_full(self):
        """
        Check if game board is full
        :return: True if all 9 squares are filled
        """
        if len(self.positions) == 0:
            return True
        else:
            return False

    def new_game(self):
        """
        resets game engine to starting values
        :return:
        """
        self.positions = None
        self.game_board = None

        self.positions = list(range(1, 10))
        self.game_board = list(
            [list(self.board_row_template), list(self.board_row_template), list(self.board_row_template)])
        choice = 'a'
        while choice not in ['X', 'O']:
            choice = input('Player 1, Please select your symbol (X or O): ')

        print('Player1 will be {}'.format(choice))
        if choice.upper() == 'X':
            self.settings['Player1'] = 'X'
            self.settings['Player2'] = 'O'
        else:
            self.settings['Player1'] = 'O'
            self.settings['Player2'] = 'X'

    def play_again(self):
        """
        Ask players for another game
        :return:
        """
        choice = ''
        while choice.upper() not in ['Y', 'N']:
            choice = input('Play another game (Y or N)? ')

        return choice.upper() == 'Y'

    def show_game_state(self):
        """
        Prints the current board state to the console
        :return:
        """
        print(' {} | {} | {} '.format(self.game_board[0][0], self.game_board[0][1], self.game_board[0][2]))
        print('---+---+---')
        print(' {} | {} | {} '.format(self.game_board[1][0], self.game_board[1][1], self.game_board[1][2]))
        print('---+---+---')
        print(' {} | {} | {}'.format(self.game_board[2][0], self.game_board[2][1], self.game_board[2][2]))
