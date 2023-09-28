# Importing the necessary modules and 

import functools
import time
import random
t = time.sleep


easy_words = [
            # 30 4-letter words
    "bark", "lone", "mild", "glow", "jazz", 
    "pint", "knee", "bold", "sing", "clay",
    "wolf", "dusk", "muse", "bind", "wisp",
    "plum", "grip", "flaw", "fawn", "veer",
    "wave", "rift", "link", "brag", "limp",
    "torn", "clog", "slid", "gale", "shun",

            # 70 5-letter words
    "swipe", "crisp", "taste", "flint", "quill", 
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
    "blend", "whisk", "charm", "sleet", "cloak"
] # / 100


medium_words = [
            # 20 5-letter words
    "swipe", "crisp", "taste", "flint", "quill", 
    "blush", "flock", "shine", "frost", "pride", 
    "swoop", "track", "plead", "sleek", "blaze", 
    "snarl", "plumb", "grunt", "skate", "climb", 
            
            # 70 6-letter words
    "thwart", "stripe", "crunch", "glinty", "muzzle",
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
    "flocks", "ignite", "broods", "starch", "wrongs",

            # 40 7-letter words
    "frosted", "swindle", "blanket", "crawled", "glisten",
    "shrivel", "trickle", "brushed", "spindle", "throttle",
    "spliced", "drizzle", "frantic", "flounce", "scuttle",
    "splotch", "spanner", "scrawny", "trashed", "bristle",
    "squared", "dwindle", "spruced", "flutter", "shimmer",
    "twisted", "scraped", "crackle", "prickle", "strayed",
    "grunted", "streaky", "flanked", "trapped", "drapers",
    "wriggle", "bricked", "twirled", "frowned", "clashed"
] # / 130


hard_words = [
            # 40 7-letter words
    "frosted", "swindle", "blanket", "crawled", "glisten",
    "shrivel", "trickle", "brushed", "spindle", "throttle",
    "spliced", "drizzle", "frantic", "flounce", "scuttle",
    "splotch", "spanner", "scrawny", "trashed", "bristle",
    "squared", "dwindle", "spruced", "flutter", "shimmer",
    "twisted", "scraped", "crackle", "prickle", "strayed",
    "grunted", "streaky", "flanked", "trapped", "drapers",
    "wriggle", "bricked", "twirled", "frowned", "clashed",

            # 60 8-letter words
    "absorbed", "buttered", "clashing", "driveway", "elevator",
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
    "grinding", "hitching", "invoking", "jostling", "kindling",
            
            # 20 9-letter words
    "adversity", "bellowing", "construed", "deploring", "entrusted",
    "fluctuate", "hastening", "insulated", "jubilance", "knuckling",
    "lamenting", "mavericks", "navigated", "oscillate", "perplexed",
    "quandary", "reverence", "splotches", "truncated", "undermine",

            # 20 10-letter words
    "absolutely", "bitterness", "conflation", "deplorable", "exasperate",
    "fluctuated", "graciously", "holograph", "innovative", "judicature",
    "kaleidoscope", "languished", "monochrome", "nurturance", "perfection",
    "quicksilver", "resonating", "stipulated", "turmoil", "underlying"
] # / 140






class WordSelector():  
    def __init__(self, player_count, difficulty):
        
        
    # Setting the class's attribute
        self.player_count = player_count
        self.difficulty = difficulty


    def selecting_words(self):
        if self.difficulty == 1:
            word_list = easy_words 
        elif self.difficulty == 2:
            word_list = medium_words
        else:
            word_list = hard_words


        first_word = random.choice(word_list)
        target_length = len(first_word)


        filtered_words = [word for word in word_list if len(word) == target_length]


        words_chosen = [first_word]
        for _ in range(1, self.player_count):
            words_chosen.append(random.choice(filtered_words))
        
        return words_chosen






def coundown_timer(difficulty):
        

    if difficulty == 1:
        time = 120
        
    elif difficulty == 2:
        time = 80
        
    else:
        time = 60


    for sec in range(time, 0, -1):
        print(f'\r Countdown: {sec}', end='', flush=True)





last_text_length = 0

def typewriter_effect(text):
    global last_text_length
    for char in text:
        print(char, end='', flush=True)
        t(0.01)
    last_text_length = len(text)





def delete_last_lines(lines=0):
    global last_text_length
    # Use the escape code to move the cursor up
    print("\033[A" * lines, end='') 
    # Erase the line
    print("\r" + "  " * last_text_length +  "\r", end='', flush=True)




def lower_cursor(lines=1):
    for line in range(lines):
        print("\n", flush=True)