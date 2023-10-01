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
    - [set-player-lives()](#set-player-lives)
    - [round-start()](#round-start)
    - [round-end()](#round-end)
    - [handle-first-to-15()](#handle-first-to-15)
    - [handle-other-modes()](#handle-other-modes)
    - [player-turn()](#player-turn)
    - [ask-letter()](#ask-letter)
    - [check-letter()](#check-letter)
    - [handle-correct-guess()](#handle-correct-guess)
    - [handle-incorrect-guess()](#handle-incorrect-guess)
    - [game-repeat()](#game-repeat)
5. [Game Technicals](#game-technicals)
    - [selecting-words()](#selecting-words)
    - [delete-last-lines()](#delete-last-lines)
    - [typewriter-effect()](#typewriter-effect)
    - [lower-cursor()](#lower-cursor)
    - [raise-cursor()](#raise-cursor)
    - [hangman-ascii()](#hangman-ascii)


## Overview
This hangman game is designed to be a customisable multiplayer experience where not only the player count can be selected, but the game mode and difficulty. The number of lives is dependant on the difficulty, as well as the word length for each player round. The rules for each game mode are specified before each game, and the program utilises a custom module to keep technical functions seperate. The game is replayable from within the program.


## User Experience
Before the game is initialised the program asks the user for several arguments. In order, these are the player count, difficulty and (if applicable) the multiplayer gamemode. It will ask for an input for each player's name.

This is managed by the **initiate_game()** function, and the **get_game_settings** function, of which the former iteratively calls the latter with the relevant prompt arguments.

The program collects a word for each player, who are given a set amount of lives to correctly enter all the letters in their respective words. Details are found in the subsections of the User Experience.

Only relevant statements are printed to the terminal when necessary, and deleted afterwards. This keeps the user experience concise and manageable for practicality purposes. That said, there is a custom print function found in the **'game_technicals.py'** file that writes each statement one character at a time, creating a typewriter effect. This was unnecessary, but something that I thought would be cool to implement. It might bring more attention to what's being printed however, so could benefit the user experience for some.


### Difficulty
The difficulty determines the length of the words given, as well as the lives the player has. The number of lives are as follows:

- Easy: 7 lives
- Medium: 6 lives
- Hard: 5 lives

The length of the words given are also affected. Though players will each get words of the same length, there is a variation for each difficulty. These are:

- Easy: 4 to 5 letters long
- Medium: 5 to 7 letters long
- Hard: 7 to 10 letters long

Each difficulty is split into 3 dictionaries, with the character lengths of the words being the keys and the respective lists of words that length as the values. The probabilities for each length evenly split within each difficulty dictionary, though there are more words of certain lengths than others.

### Modes
The rules of the game, including the win conditions are dependant on the game mode.

If the mode is Last Man Standing, then any players who fail a round are eliminated and removed from subsequent rounds. If it is First To 15 (15 letters) then the player who is first to gain 15 letters wins. If multiple players accumulate over 15 letters in the same round, then the player with the highest score wins. If they have the same score, they both win. 

If it is single player, then the game will be one round and the user will have the option to play another game.


## Player Class
The Player class is the template for the Player objects created at the beginning of the experience. It includes the name and the points for each player. It has a limited use though its points attribute makes it easy to keep track of player scores in First To 15.


## Hangman Class
This class deals with the bulk of the programmatic content. It handles the game flow, the letter verification, the conditions for the game based on difficulty and mode, as well as calling the **selecting_words()** and **hangman_ascii()** functions from the **game_technicals.py** file. The following methods are explained in more detail:

### set-player-lives()
This sets the number of lives for each player based on the difficulty, and is called in the **round_start()** method to be reset for each player.

### round-start()
Begins a new round and initiates the turn for each player.

### round-end()
Handles the end-of-round procedures and calls the relevant method based on the gamemode.

### handle-first-to-15()
Handles the round's outcome for the First To 15 gamemode.

### handle-other-modes()
Handles the round's outcome for the Last Man Standing and singleplayer gamemodes.

### player-turn()
Initiates of manages the turn for the current player, printing the empty word to be guessed, as well as stating the number of unique characters in the word. It also calls the **ask_letter()** and **check_letter()** methods.

### ask-letter()
Prompts the player to enter a letter and checks if the input is valid. I.e if it is a single, alphabetical letter.

### check-letter()
Checks the guessed letter against the player's word and directs to the appropriate handling depending on the guess' success.

### handle-correct-guess()
Handles the procedure when the player has guessed correctly, and manages the outcome when a player has guessed all the letters correctly.

### handle-incorrect-guess()
Handles the procedures when the player has guessed incorrectly, and manages the outcome (depending on the gamemode) when a player has run out of lives.

### game-repeat()
Prompts the player to state whether they wish to play another game. If the player says yes ('y') then the **initiate_game()** function will be called and a new game's setting's will be obtained.


## Game Technicals
The **game_technicals.py** file includes the dictionaries containing all the words that can be issued in the game, as well as several functions that help with both game mechanics and the presentation of the game from the fron end. These functions are as follows:

### selecting-words()
This method takes the length of the players_left attribute in Hangman and the difficulty, and retrieves the relevant amount of words from the appropriate word dictionary. 

It ensures the words are all of the same length. It does this by randomely selecting a key (word length) in one of the word dictionaries, and then randomely selecting the necessary amount of words from the value of said key.

### delete-last-lines()
This function uses escape codes to delete the last lines, of a user-defined quantity.

### typewriter-effect()
This function is an altered print function that creates a typewriter effect for every output, as well as having built-in delay and auto-delete parameters.

### lower-cursor()
A function that moves the cursor down by an integer argument (default: 1).

### raise-cursor()
A function that uses an escape code to raise the cursor by an integer argument (default=1).

### hangman-ascii()
A function that stores a list containing the hangman ascii art in order. When called it will reverse index this list using the number of lives the player has remaining, making it compatible with all difficulties.