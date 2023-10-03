# Required Modules & aliases
import time
from game_data import game_technicals as gt

# Method Aliases
dell_line = gt.delete_last_lines
hangman_art = gt.hangman_ascii
t = time.sleep
text = gt.typewriter_effect
down = gt.lower_cursor
up = gt.raise_cursor



# Defines the Player class, and all actions taken towards individual Player instances.
class Player():
    """
    Represents an individual player in the hangman game.
    
    Attributes:
        name (str): The player's name.
        points (int): The player's current score.

    Methods:
        add_points: Adds a point to the self.points attribute for each letter correctly guessed.
        __str__: Prints the self.name attribute is printed when the player object is printed.
    """
    def __init__(self, name, points=0):
        self.name = name
        self.points = points
    

    # Points are the win condition for the First To 15 gamemode.
    def add_points(self):
        self.points += 1
        return self.points

    
    # Ensures the player's name is printed when addressed.
    def __str__(self):
        return(self.name)









# Defines the Hangman class, which handles all game-related logic.
class Hangman:
    """
    Manages the core logic for a game of Hangman.
    
    Attributes:
        players_left (list): List of players still active in the game.
        difficulty (int): Game difficulty level (1 for Easy, 2 for Medium, 3 for Hard).
        mode (int): Game mode (1 for Last Man Standing, 2 for First To 15 points, 3 for Singleplayer).
    
    Methods:
        _set_player_lives: Sets the number of lives for players based on game difficulty.
        _round_start: Begins a new round by selecting words and initiating turns for each player.
        _round_end: Determines end-of-round procedures based on the chosen game mode.
        _handle_first_to_15: Manages round results for the 'First To 15' game mode.
        _handle_other_modes: Manages round results for 'Last Man Standing' and single-player modes.
        _player_turn: Manages a player's turn where they guess letters for a given word.
        _ask_letter: Prompts the player to guess a letter and ensures valid input.
        _check_letter: Checks guessed letter against the word and directs to appropriate handling.
        _handle_correct_guess: Handles procedures when a player guesses a letter correctly.
        _handle_incorrect_guess: Handles proceedures when a player's letter guess is incorrect.
        _game_repeat: Asks player if they'd like to play another game and restarts if desired.
    """
    def __init__(self, player_list, difficulty, mode):   
        self.players_left = player_list  
        self.difficulty = difficulty
        self.mode = mode


        # Informs the player(s) of the rules and number of lives they get for each round.
        if self.mode == 1:
            text("Last Man Standing: Last player to lose a round wins.", 2, True)
        elif self.mode == 2:
            text("First To 15: First player to correctly guess 15 letters wins", 2, True)

        self._set_player_lives()
        text(f"You have {self.num_lives} lives to correctly guess your word.", 2, True)

        # Starts the rounds
        self._round_start()



    # Sets player lives based  on game difficulty
    def _set_player_lives(self):
    # Easy
        if self.difficulty == 1:
            self.num_lives = 7
    # Medium
        elif self.difficulty == 2:
            self.num_lives = 6
    # Hard
        else:
            self.num_lives = 5



    # Chooses the words, and iteratively initiates the round for each player.
    def _round_start(self):
        words_chosen = gt.selecting_words(len(self.players_left), self.difficulty)
        round_words = list(zip(self.players_left, words_chosen))


        for player, word in round_words:
            # Sets each player's lives and the letters they've already guessed.
            self._set_player_lives()
            self.list_letters = []

            # Plays the round for the current player.
            player_round_results = self._player_turn(player, word)

            # Deletes any ascii art after the round if necessary.
            down(6)
            dell_line(15)

            
        self._round_end()



    # Directs to specific handling method based on game mode.
    def _round_end(self):
        if self.mode == 2:
            self._handle_first_to_15()
        else:
            self._handle_other_modes()


    
    # Handles First To 15 gamemode round results.
    def _handle_first_to_15(self):
        # Finds the player with the highest points
        max_points = max(player.points for player in self.players_left)

        # Congratulates the winner(s) or starts another round.
        if max_points >= 15:
            for player in self.players_left:
                if player.points == max_points:
                    text(f"Congratulations {player}! You won with {player.points} points!", 1, True)
            self._game_repeat()
        else:
            self._round_start()
    


    # Handles Last Man Standing and singleplayer round results.
    def _handle_other_modes(self):
    # Congratulates the winner.
        if len(self.players_left) == 1:
            text(f"Congratulations {self.players_left[0]}, you've won Hangman!", 1, True)
            self._game_repeat()

    # Continues to the next round.
        elif len(self.players_left) > 1:
            for player in self.players_left:
                text(f"{player}, you have passed this round.", 0.6, True)
            self._round_start()
    # Single player    
        else:
            self._game_repeat()



    # Handles the round for the current player.
    def _player_turn(self, player, word):
        """
        Manages a player's turn where they guess letters for a given word.
        
        Args:
            player (Player): The player taking the turn.
            word (str): The target word for the round.
        """
    # Sets the word attributes for the current player's round.
        self.word_guessed = ['_' for i in word]
        self.num_letters = len(set(word))

    # Prints the necessary word information to the player.
        text(f"{player}, your mystery word has {self.num_letters} unique characters:\n")
        text(' '.join(self.word_guessed))
        down()

    # Iteratively obtains the player's letter input.
        while True:
            letter = self._ask_letter()

        # Checks if the letter's already been guessed.
            if letter in self.list_letters:
                dell_line(0)
                text(f"Letter '{letter}' was already tried", 0.6, True)
                continue
            
        # Sends unguessed letters to be processed and ends the loop once the round ends.
            self.list_letters.append(letter)
            if not self._check_letter(player, letter, word):
                break



    # Asks the player to guess a letter until a valid letter is given.
    def _ask_letter(self):
        """
        Prompts the player to guess a letter and ensures valid input.
        
        Returns:
            str: The guessed letter.
        """
        while True:
            text(f"Please enter a letter: ")
            letter = input().lower().strip()
            dell_line(1)

            if len(letter) == 1 and letter.isalpha():
                return letter
            
            text("Please, enter just a single alphabetical character", 1, True)
        
    

    # Processes the player's valid guess by comparing it to the word.
    def _check_letter(self, player, letter, word):
        """
        Checks the guessed letter against the word and directs to appropriate handling.
        
        Args:
            player (Player): The player who made the guess.
            letter (str): The guessed letter.
            word (str): The target word for the round.
        """
        if letter in word:
            return self._handle_correct_guess(player, letter, word)
        else:
            return self._handle_incorrect_guess(player, letter, word)



    # Handles a correct guess.
    def _handle_correct_guess(self, player, letter, word):
        """
        Handles procedures when a player guesses a letter correctly.
        
        Args:
            player (Player): The player who made the guess.
            letter (str): The correctly guessed letter.
            word (str): The target word for the round.
        """
        self.word_guessed = [letter if word[index] == letter else current_char for index, current_char in enumerate(self.word_guessed)]
        self.num_letters -= 1

        dell_line(2)
        text(' '.join(self.word_guessed))
        down()

        if '_' not in self.word_guessed:
            text(f"Congratulations! You've correctly guessed \"{word}\" as the word.", 1, True)
            player.add_points()

            if self.mode == 2:
                text(f"{player} has accumulated {player.points} points.", 1, True)
            return False
        
        else:
            text(f"Good guess! \"{letter}\" is in the word.", 0.7, True)
            player.add_points()
            return True



    # Handles an incorrect guess.
    def _handle_incorrect_guess(self, player, letter, word):
        """
        Handles procedures when a player's letter guess is incorrect.
        
        Args:
            player (Player): The player who made the guess.
            letter (str): The incorrectly guessed letter.
            word (str): The target word for the round.
        """
    # Handling the lives and ascii art.
        self.num_lives -= 1
        down()
        hangman_art(self.num_lives)
        up(10)


    # Checks if the player has run out of lives.
        if self.num_lives == 0:
            text("Unlucky! You've run out of lives.", 1, True)
            
        # Eliminates the player in Last Man Standing.
            if self.mode == 1:
                text(f"{player} has been eliminated!", 1, True)
                self.players_left.remove(player)
            
        # Prints the accumulated points of the player in First To 15.
            elif self.mode == 2:
                text(f"{player} has accumulated {player.points} points.", 1, True)

        # Prevents winning statement if singleplayer.
            else:
                self.players_left.remove(player)

            return False

    # Informs the player that their guess was incorrect if they still have lives.
        text(f"Sorry. \"{letter}\" is not in the word. Try again.", 0.6, True)
        return True
    


    # Asks the user if they wish to play another game
    def _game_repeat(self):
        while True:
            text("Would you like to play another game? (y/n): ")
            repeat_input = input().lower().strip()
            dell_line(1)

            if repeat_input == 'y':
                initiate_game()
                break
            elif repeat_input == 'n':
                text("Thank you for playing!", 1, True)
                break
            else:
                text("Please enter a valid input (y/n)...", 1, True)
                continue











# Obtaining game settings
def get_game_settings(prompt, min_val, max_val, error_message):
    """
    Function to obtain game settings based on user input.
    
    Args:
        prompt (str): The message asking the user for input.
        min_val (int): The minimum allowed value for the setting.
        max_val (int): The maximum allowed value for the setting.
        error_message (str): The message displayed for invalid input.
        
    Returns:
        int: The valid input provided by the user.
    """

    while True:
        text(prompt)

    # Checks for a valid input to return
        try:
            user_input = int(input().strip())
            #dell_line(1)
            if min_val <= user_input <= max_val:
                dell_line(1)
                return user_input
            else:
                raise ValueError
            
    # Prints error statement.
        except ValueError:
            dell_line(1)
            text(error_message, 1, True)





if __name__ == '__main__':
    text("Welcome to Hangman!", 1, True)


    # Initiates selection of game settings and game.
    def initiate_game():
        # Calling the get_user_input function with specified arguments
        player_count = get_game_settings(
            "Enter your player count (max: 4): ", 1, 4, 
            "Please enter a number between 1 and 4..."
        )


        difficulty = get_game_settings(
            "Select the difficulty (Easy -> 1, Medium -> 2, Hard -> 3): ", 1, 3, 
            "Please enter a number between 1 and 3..."
        )

        # Asks for multiplayer-specific gamemode, or defaults to singleplayer.
        if player_count > 1:
            mode = get_game_settings(
                "Choose the gamemode (Last Man Standing -> 1, First To 15 points -> 2): ", 1, 2,
                "Please enter a number between 1 and 2..."
            )
        else:
            mode = 3


        # Creates the list of players.
        player_list = []

        # Getting names for each player.
        for player in range(player_count):
            dell_line(0)
            text(f"Player {player + 1} Name: ")
            player_name = input().strip()
            player_list.append(Player(player_name))
            dell_line(1)

        # Starting the game.
        t(1)
        game = Hangman(player_list, difficulty, mode)
    
# Initial program startup.
    initiate_game()