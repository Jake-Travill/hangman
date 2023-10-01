# Importing the necessary modules
import time
import random
t = time.sleep


EASY_WORDS = {
            # 30 4-letter words
    4: ["bark", "lone", "mild", "glow", "jazz", 
        "pint", "knee", "bold", "sing", "clay",
        "wolf", "dusk", "muse", "bind", "wisp",
        "plum", "grip", "flaw", "fawn", "veer",
        "wave", "rift", "link", "brag", "limp",
        "torn", "clog", "slid", "gale", "shun"]
,
            # 70 5-letter words
    5: ["swipe", "crisp", "taste", "flint", "quill", 
        "blush", "flock", "shine", "frost", "pride", 
        "swoop", "track", "plead", "sleek", "blaze", 
        "snarl", "plumb", "grunt", "skate", "climb", 
        "drift", "dance", "laugh", "scare", "crush", 
        "spear", "flame", "douse", "prize", "creek", 
        "gleam", "proud", "drown", "twist", "slope", 
        "brace", "scour", "whale", "chill", "pluck",
        "graze", "spire", "mirth", "bloat", "thorn", 
        "draft", "clean", "swell", "stale", "smoke", 
        "blitz", "flare", "brood", "trick", "haste",
        "shred", "snack", "slink", "plush", "crank",
        "creep", "freak", "gloom", "scoot", "flank",
        "blend", "whisk", "charm", "sleet", "cloak"]
} # / 100


MEDIUM_WORDS = {
            # 20 5-letter words
    5: ["swipe", "crisp", "taste", "flint", "quill", 
        "blush", "flock", "shine", "frost", "pride", 
        "swoop", "track", "plead", "sleek", "blaze", 
        "snarl", "plumb", "grunt", "skate", "climb"] 
,
            # 70 6-letter words
    4: ["thwart", "stripe", "crunch", "glinty", "muzzle",
        "bricks", "trance", "plight", "driven", "whinny",
        "strobe", "flinch", "sprint", "glisten", "scrawl",
        "thrice", "prance", "gravel", "shrink", "fumble",
        "thongs", "drapes", "graced", "spritz", "frugal",
        "screed", "flight", "browse", "strand", "sleuth",
        "cradle", "grouse", "thieve", "chance", "sickle",
        "spiral", "scrub", "bleach", "dwindle", "fringe",
        "sprout", "glance", "smudge", "thrust", "sliced",
        "breeze", "quiver", "lather", "drills", "plunge",
        "mingle", "rights", "drones", "clench", "slouch",
        "blurbs", "flares", "sprung", "gleams", "twitch",
        "squire", "gloved", "craves", "strode", "plucks",
        "flocks", "ignite", "broods", "starch", "wrongs"]
,
            # 40 7-letter words
    7: ["frosted", "swindle", "blanket", "crawled", "glisten",
        "shrivel", "trickle", "brushed", "spindle", "throttle",
        "spliced", "drizzle", "frantic", "flounce", "scuttle",
        "splotch", "spanner", "scrawny", "trashed", "bristle",
        "squared", "dwindle", "spruced", "flutter", "shimmer",
        "twisted", "scraped", "crackle", "prickle", "strayed",
        "grunted", "streaky", "flanked", "trapped", "drapers",
        "wriggle", "bricked", "twirled", "frowned", "clashed"]
} # / 130


HARD_WORDS = {
            # 40 7-letter words
    7: ["frosted", "swindle", "blanket", "crawled", "glisten",
        "shrivel", "trickle", "brushed", "spindle", "throttle",
        "spliced", "drizzle", "frantic", "flounce", "scuttle",
        "splotch", "spanner", "scrawny", "trashed", "bristle",
        "squared", "dwindle", "spruced", "flutter", "shimmer",
        "twisted", "scraped", "crackle", "prickle", "strayed",
        "grunted", "streaky", "flanked", "trapped", "drapers",
        "wriggle", "bricked", "twirled", "frowned", "clashed"]
,
            # 60 8-letter words
    8: ["absorbed", "buttered", "clashing", "driveway", "elevator",
        "flapping", "gradient", "hormonal", "imprison", "juxtapose",
        "knocking", "lurking", "muttered", "nurtured", "obstruct",
        "pervaded", "quivered", "ravished", "stapling", "thriving",
        "umbrella", "vanished", "wrinkled", "xeroxing", "yearning",
        "zippered", "abrasive", "blotting", "creeping", "drenched",
        "enriched", "fumbling", "gritting", "hovering", "injected",
        "jumbling", "kneading", "lighting", "mumbling", "nuzzling",
        "outlined", "plucking", "quacking", "ruffling", "screamed",
        "twisting", "uplifted", "vaulting", "whirling", "yowling",
        "zingy", "bleached", "crumpled", "doodling", "flinching",
        "grinding", "hitching", "invoking", "jostling", "kindling"]
,            
            # 20 9-letter words
    9: ["adversity", "bellowing", "construed", "deploring", "entrusted",
        "fluctuate", "hastening", "insulated", "jubilance", "knuckling",
        "lamenting", "mavericks", "navigated", "oscillate", "perplexed",
        "quandary", "reverence", "splotches", "truncated", "undermine"]
,
            # 20 10-letter words
    10: ["absolutely", "bitterness", "conflation", "deplorable", "exasperate",
        "fluctuated", "graciously", "holograph", "innovative", "judicature",
        "kaleidoscope", "languished", "monochrome", "nurturance", "perfection",
        "quicksilver", "resonating", "stipulated", "turmoil", "underlying"]
} # / 140



def selecting_words(player_count, difficulty):
    """
    Selects a list of words based on the player count and difficulty.

    Args:
        player_count (int): Number of players in the game.
        difficulty (int): Difficulty level (1 for easy, 2 for medium, 3 for hard).

    Returns:
        list: A list of words for the game.
    """

    # Selecting the dictionary to choose from based on difficulty.
    if difficulty == 1:
        word_dict = EASY_WORDS 
    elif difficulty == 2:
        word_dict = MEDIUM_WORDS
    else:
        word_dict = HARD_WORDS

    # Ensuring all words chosen are the same length.
    word_lengths = list(word_dict.keys())
    chosen_length = random.choice(word_lengths)

    # Choosing the correct quantity of equally-lengthed words.
    words_chosen = random.sample(word_dict[chosen_length], player_count)
       
    return words_chosen



# Deletes last lines in the range of the current line to/including the argument.
def delete_last_lines(lines=0):
    for _ in range(lines + 1): 
        print("\r\033[K", end='', flush=True)
        if _ < lines:
            print("\033[A", end='', flush=True)



# Custom print function that displays text like a typewriter and has auto-delete functionality.
def typewriter_effect(text, delay=None, auto_delete=False):
    # Adding a short delay for each character of a text
    for char in text:
        print(char, end='', flush=True)
        t(0.008)
    
    # Introducing delay before automatic deletion.
    if delay:
        t(delay)
    if auto_delete:
        delete_last_lines(0)



# Moves cursor down by specified lines.
def lower_cursor(lines=1):
    # Moves the cursor down by the specified amount
    for line in range(lines):
        print("\n", flush=True)



# Moves cursor up by specified lines
def raise_cursor(lines=1):
    print(f"\x1b[{lines}A", end="", flush=True)



# Stores and prints the Hangman ASCII art.
def hangman_ascii(num_lives):
    HANGMAN_ASCII_ART = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    # Indexes the ascii art list based on the number of lives.
    print(HANGMAN_ASCII_ART[-num_lives-1])