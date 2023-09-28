# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Table Of Contents
1. [Overview](#overview)
2. [User Experience](#user-experience)
- [Difficulty](#difficulty)
- [Modes](#modes)
3. [Player Class](#player-class)
4. [Hangman Class](#hangman-class)
- [round-start()](#round-start)
- [ask-letter()](#ask-letter)
- [check-letter()](#check-letter)
5. [Game Technicals](#game-technicals)
- [WordSelector](#wordselector)
- [Miscellaneous](#miscellaneous)
6. [Critiques](#critiques)


## Overview
This hangman game is designed to be a customisable multiplayer experience where not only the player count can be selected, but the game mode and difficulty. The number of lives is dependant on the difficulty, as well as the word length and (if included) the timer for each player round. The game will be replayable from within the program, though this aspect of the code is unfinished. The modes will specify the win conditions and rules for the game. The code utilises technical functions that keep the output clean and concise, ensuring only the relevant information is outputted to the terminal when needed.

Note that the code is written as a prototype, and was written hastily and as a proof of concept. The specificities of this will be discussed in the critiques section.


## User Experience
Before the game is initialised the program asks the user for several arguments. In order, these are the player count, difficulty and (if applicable) the multiplayer gamemode. It will ask for an input for each player's name. 
(Though the input is stripped, I have noticed a bug where if too much whitespace is entered before entering and inputing the name, the name will stay printed in the terminal when the proceeding code runs.) 

The program collects a word for each player, who are given a set amount of lives to correctly enter all the letters in their respective words. Details are found in the subsections of the User Experience.

Only relevant statements are printed to the terminal when necessary, keeping the user experience concise and manageable for practicality purposes. That said, there is a custom print function found in the 'game_technicals.py' file that writes each statement one character at a time, creating a typewriter effect. This was unnecessary, but a thought that passed my mind and that I thought would be cool to implement.


### Difficulty
The difficulty determines the length of the words given, as well as the lives the player has. I had noticed that 5 lives was sometimes quite difficult depending on the word selected from the lists, so the number of lives are as follow:

- Easy: 8 lives
- Medium: 6 lives
- Hard: 5 lives

The length of the words given are also affected. Though players will each get words of the same length, there is a variation for each difficulty. These are:

- Easy: 4 to 5 letters long
- Medium: 5 to 7 letters long
- Hard: 7 to 10 letters long

The probabilities of getting words of a certain length are not equal and dependant on the quantity of each found in the word lists for each difficulty.

### Modes
The rules of the game including the win conditions are dependant on the game mode.

If the mode is Last Man Standing, then any players who fail a round are eliminated and removed from subsequent rounds. If it is First To 15 (15 letters) then the player who is first to gain 15 letters wins. If multiple players accumulate over 15 letters in the same round, then the player with the highest score wins. If they have the same score, they both win. 

If it is single player, then the game will be one round and (though not implemented) the user will have the option to replay the game.


## Player Class
The Player class is the template for the Player objects created at the beginning of the experience. It includes the name, the points and the strike (whether the player has failed a round in Last Man Standing) for each player. It is a simple class and the interaction between it and the Hangman class, or whether it's even necessary to be seperate, is something I'm unsure of.


## Hangman Class
This class deals with the bulk of the programmatic content. It handles the game flow, the letter verification, the conditions for the game based on difficulty and mode, as well as calling the WordSelector class in the game_technicals.py file to obtain the round's words. The following methods are explained in more detail.

### round-start()
This method sets the number of lives each player has for each round, then for each player calls the ask_letter() method to iteratively ask the current player to guess their word's letters. After the round is over, the method then handles the outcome of the round depending on the mode. Whether this be that a further round is required or the win/lose conditions have been met and the game finishes.

### ask-letter()
This method is called for each player in one round of the game. It starts by printing the number of unique characters and the empty self.word_guessed list of characters. It then asks for an input from the player, and checks if the letter is valid i.e is a single letter and is alphabetical. It then checks if the letter has already been guessed, and if so prompts the user to enter a new character. If valid, the user's input is sent to the check_letter() method.

### check-letter()
This method checks to see if the user input is found within the word. It updates the self.word_guessed attribute if so, and handles the points gained or lives lost as a result of the input. If the gamemode is First To 15, then it prints the accumulated points a player has after the round ends. It then returns the outcome of the round's last input (and thus the outcome of the round) to the ask_letter() method which then returns it to the round_start() method.


## Game Technicals
The game_technicals.py file includes the lists for all the words that can be issued in the game, as well as the WordSelector class and several miscellaneous functions that help with the presentation of the game from the fron end. The details are as follows:

### WordSelector
This class contains one method, the selecting_words() method, though may incorporate the countdown_timer() method (if implemented). This method takes the attributes found withing the WordSelector class, notably the player count and difficulty, and retrieves the relevant amount of words from the relevant word list. 

It ensures the words are all of the same length, doing so by randomly selecting the first word, and selecting the remaining words based on the first word's length. It then returns the words to the round_start() method that zips the words with the list of players.

### Miscellaneous
The game_technicals.py file also includes several other functions aimed at keeping repeated code concise or adding a bit of flare. In brief, these functions consist of:

#### typewriter_effect()
This function is an altered print function that creates a typewriter effect for every output, giving a bit of uniqueness to the game.

#### delete_last_lines()
This function takes the length of the last typewriter_effect() print statement and prints whitespace over it, with an argument for how many lines the cursor moves up to do so.

#### lower_cursor()
A simple function that moves the cursor down by an integer argument (default: 1). I believe it's only been used once so far in the code but I figured it could come in handy.


## Critiques
Because this code was written in one stretch, and with the attitude of "get it all working first", the conciseness and simplicity of it leaves much to be desired. Throughout development I intended to take on a specific approach to annotation but couldn't decide on how I wanted the code structured or annotated so I left it for after the final touches have been finished.

Overall the code is a bit of a mess and needs cleaning but most of the logic is done for the modes and difficulties. It just needs restructuring to adhere better to good coding practices.

### DRY Coding Practices
Despite making use of functions, DRY coding practices are not adhered to as well as they could be. An example of this is at the bottom of the script, which deals with the player input for the game settings. It was written to separate each setting for conceptual simplicity but has not been edited since it was first written. Because of the repetitive nature of the section, it could easily fit into a single function with parameters for the min/max values, the input and the error message.

### Abstraction
The methods found in the Hangman class are long and would be better split into separate methods. They were based off of the default template methods given for the project, which I adhered to for simplicity however after fleshing them out they've become long and complicated and the Hangman class could be much simpler with less nested if/else statements and while loops. The game settings loop at the bottom of the script also fits into needed abstraction.

### General Cleaning
General cleaning is needed on the code This includes: 
- Setting while loops to 'while == True' as opposed to 'while bool_value == True', as they're unneeded. 
- The return variables in the check_letter() method could also likely be fitted/grouped into a single tuple variable for each condition. 
- Global variables such as the first_to_15_list could be encapsulated into the Hangman class. If/else statements could be more procise. 
- The Player class itself might be unnecessary and player properties could be handled within the Hangman Class.
- Redundant else: continue/else: pass statements that were placeholders but no longer needed.
- Restructuring of the dell() (delete_last_lines) function calls so they're more intuitive and easier to track in the program runtime.