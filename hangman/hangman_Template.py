# Required Modules & aliases
#import random
import time
from game_data import game_technicals as gt

# Method Aliases
t = time.sleep
timer = gt.coundown_timer
textz = gt.typewriter_effect
dell = gt.delete_last_lines
down = gt.lower_cursor


## TODO             1) Clean up the code


## TODO (AFTERNOON)
##                  1) Research:
##                      - Look into a Generator for the Hangman images.
##                  2) COMPLETE THE RELEVANT DOCSTRINGS AND README.
##                  3) (COMPLETE A SAFE, SINGLE PLAYER VERSION)
##                  3) UPLOAD TO GITHUB


class Player():
    def __init__(self, name, points=0, strike=0):
        self.name = name
        self.points = points
        self.strike = strike
    


    def add_points(self):
        self.points += 1
        return self.points

    
    def add_strike(self):
        self.strike += 1
        return self.strike
    
    def __str__(self):
        return(self.name)












class Hangman:


    def __init__(self, player_list, difficulty, mode):   
        self.players_left = player_list  
        self.difficulty = difficulty
        self.mode = mode
        self.word_obtaining = gt.WordSelector(len(self.players_left), self.difficulty)

        

        self.round_start()


    def round_start(self):
        words_chosen = self.word_obtaining.selecting_words()

        round_words = list(zip(self.players_left, words_chosen))

        ## TESTING
        print(round_words)
        t(3)



        for player, word in round_words:


            if self.difficulty == 1:
                self.num_lives = 8
            elif self.difficulty == 2:
                self.num_lives = 6
            else:
                self.num_lives = 5


            self.list_letters = []
            player_round_results = self.ask_letter(player, word)

            dell(2)
            dell(1)




                
        if self.mode == 2:
            if first_to_15_list:
                max_points = max(player.points for player in first_to_15_list)

                for player in self.players_left:
                    if player.points == max_points:
                        textz(f"{player} has won with {player.points} points. Congratulations!")
                        t(1)
                        dell(0)
                    else:
                        continue
            else:
                self.round_start()
                

        else:
            if len(self.players_left) == 1:
                textz(f"Congratulations {self.players_left[0]}, you've won Hangman!")
                t(1)

                ## Game Repeat.


            elif len(self.players_left) > 1:
                for player in self.players_left:
                    textz(f"{player}, you have passed this round.")
                    t(0.6)
                    dell(0)

                self.round_start()
            
            else:
                pass
                ## Game Repeat




    def ask_letter(self, player, word): 
        self.word_guessed = ['_' for i in word]
        self.num_letters = len(set(word))
        textz(f"{player}, your mystery word has {self.num_letters} unique characters:\n")
        textz(' '.join(self.word_guessed))
        down()


        player_round = True
        while player_round == True:
            
            textz("Please enter a letter: ")
            letter = input("").lower()



            if len(letter) == 1 and letter.isalpha():



                if letter in self.list_letters:
                    dell(1)
                    textz(f"Letter '{letter}' was already tried")
                    t(0.6)
                    dell(0)
                

                
                
                else:
                    dell(1)
                    self.list_letters.append(letter)
                    round_results = self.check_letter(player, letter, word)


                    if round_results[0] == True:
                        continue
                    else:
                        player_round = False
                        return round_results
                        
            

            else:
                dell(1)
                textz("Please, enter just a single alphabetical character")
                t(1)
                dell(0)







    def check_letter(self, player, letter, word) -> None:


        if letter in word:

            self.word_guessed = [letter if word[index] == letter else current_char for index, current_char in enumerate(self.word_guessed)]
            self.num_letters -= 1


            dell(2)
            textz(' '.join(self.word_guessed))
            down()

            if '_' not in self.word_guessed:
                textz(f"Congratulations! You've correctly guessed \"{word}\" as the word.")
                player.add_points()
                t(1)
                dell(0)
                if self.mode == 2:
                    textz(f"{player} has accumulated {player.points} points.")
                    t(1)
                    dell(0)
                    if player.points >= 15:
                        first_to_15_list.append(player)
                    else:
                        pass
                else:
                    pass
                return False, player.points, player.strike
                
                

            else:
                textz(f"Good guess! \"{letter}\" is in the word.")
                player.add_points()
                t(0.7)
                dell()
                return True, None, None
                


        else:
            self.num_lives -= 1
            
            
            if self.num_lives == 0:
                dell(0)
                textz("Unlucky! You've ran out of lives.")
                t(1)
                dell(0)

                if self.mode == 1:
                    player.add_strike()
                    textz(f"{player} has been eliminated!")
                    t(1)
                    dell(0)
                    self.players_left.remove(player)
                    #return False, None, player.strike

                elif self.mode == 2:
                    textz(f"{player} has accumulated {player.points} points.")
                    #return False, player.points, None
                    t(1)

                else:
                    player.add_strike()
                return False, player.points, player.strike
            

            else:
                dell(0)
                textz(f"Sorry, \"{letter}\" is not in the word. Try again.")
                t(0.8)
                dell()
                return True, None, None
                
















#               ## PLAYER EXPERIENCE


if __name__ == '__main__':
    textz("Welcome to Hangman!")
    t(1)

    game_running = True
    while game_running == True:




        player_list = []

        first_to_15_list = []







        players_setting = True
        while players_setting == True:
            
            dell(0)
            textz("Enter your player count (max: 4): ")
            player_input = input()
            



            try:
                player_count = int(player_input)
                if not 1 <= player_count <= 4:
                    raise ValueError
                
                else:
                    dell(1)
                    break

        


            except ValueError:
                dell(1)
                textz("Please enter a singe number between 1 and 4...")
                t(1)
                continue










        difficulty_settings = True
        while difficulty_settings == True:
            
            dell(0)
            textz("Select the difficulty (Easy -> 1, Medium -> 2, Hard -> 3): ")
            player_input = input()
            



            try:
                difficulty = int(player_input)
                if not 1 <= difficulty <= 3:
                    raise ValueError
                
                else:
                    dell(1)
                    break

        


            except ValueError:
                dell(1)
                textz("\rPlease enter a singe number between 1 and 3...")
                t(1)
                continue






        if player_count > 1:
            game_mode = True
            while game_mode == True:

                dell(0)
                textz("Choose the gamemode (Last Man Standing -> 1, First To 15 points -> 2): ")
                player_input = input()
                dell(1)
                



                try:
                    mode = int(player_input)
                    if not 1 <= mode <= 2:
                        raise ValueError
                    
                    else:
                        break

            


                except ValueError:
                    dell(1)
                    textz("\rPlease enter a singe number between 1 and 3...")
                    t(1)
                    continue
        else:
            dell(0)
            mode = 3
            
    




        for player in range(player_count):
            dell(0)
            textz(f"Player {player + 1} Name: ")
            player_name = input().strip()
            player_list.append(Player(player_name))
            dell(1)
        
        
    

        game = Hangman(player_list, difficulty, mode)

'''
        repeat = game.game_repeat()
        if repeat == True:
            continue
        else:
            textz("Thank you for playing!")
            t(1)
            break
'''