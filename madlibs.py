# simple madlibs program by Priyanka. 

def madlibs():
    print("Welcome to Madlibs! Let's get started!")
    noun = input("Please enter a noun: ")
    place = input("Please enter a place: ")
    adverb = input("Please enter an adverb: ")
    adjective = input("Please enter an adjective: ")
    noun_two = input("Please enter a noun: ")
    adjective_two = input("Please enter an adjective: ")

    print("-----------------------------------------")
    print("There once was a ", noun, " who lived in a large castle.")
    print("During the summer they would visit ", place, " and throw ", adjective, " parties.")
    print("All the townsfolk, ", adverb, " attended but they never brought any ", noun_two, ".")
    print("The ", noun, " got upset and decided not to invite the ", adjective_two, " townspeople to the parties anymore.")
    print("Now the ", noun, " was lonely but it was better than hanging out with those freeloaders.")

    return

madlibs() # function call 

print("Would you like to play again? (y/n): ")
answer = input("y/n: ")

if answer == "y":
    madlibs() # runs madlibs function from the beginning
else:
    exit() # exits program 
