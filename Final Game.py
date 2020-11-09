''' I am Salamata Bah '''
import Category #imports the file that has the functions for every category
def start ():
    player_input= input("Type in START if you are ready!\n")
    if player_input == 'START':
        print("Welcome to GuessMe!\nThis is a game that will test your general Knoweldge.\n You will have 5 categories: Math, French, Geography, Rap, and Trivia.\nChoose between one of these categories and we shall begin.\n")
    else:
        print("You can only enter START!")
        start()
start() # this function makes sure that you only can type in START
def user_answer():
    while True:
        played= ["math", "geography", "french",  "rap", "trivia" ] #a list with the possible categories
        player_input = input ("Choose a category. Make sure it is all lowercase!!\n") # asks player to choose a category
        print("")
        if player_input == "geography": # checks if it matches geography
            Category.geography()
        elif player_input == 'math': # checks if it matches math
            Category.math()
        elif player_input == "french": # checks if it matches french
            Category.french()
        elif player_input == "rap" : # checks if it matches rap
            Category.rap()
        elif player_input == 'trivia': # checks if it matches trivia
            Category.trivia()
        else: # otherwise you can't play that category
            print("That was not an option! Choose between the 5 categories!") # and you will be reminded this 
            user_answer() # and given an option to type in the category name correctly
        print("Would you like to continue playing the Game?") # after playing the category, ask player if they want to continue
        player_input = input("Type yes or no!\n") # by typing yes or no
        if player_input == 'yes': # if yes
            user_answer() # recall the function
        elif player_input == 'no' : # if no 
            print ("BYE!! Thank you for playing!") # print this 
            break # end the while loop
        elif player_input != "no": #user type anything other than yes or no 
            print("Make sure you type yes or no") # print this to remind them
        elif player_input != "yes": #user type anything other than yes or no 
            print("Make sure you type yes or no") # print this to remind them
            
user_answer() # call the function


        
 



