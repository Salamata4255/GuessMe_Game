import random 

class Game: # I created a class to keep the same structure in every function 
    def __init__(self, question, correctAnswer, wrongAnswers):
        self.question = question
        self.correct_answ = correctAnswer
        self.wrong_answ = wrongAnswers

def geography():
    ques_List = [Game("Which of the following is not on Earth?", "Sea of Tranquility", ["North Sea", "Mediterranean Sea","Baltic Sea"]),
    Game("What is the capital of Australia?", "Canberra", ["Sydney", "Melbourne", "Newcastle"]),
    Game("Where is Minsk?", "Belarus", ["Russia", "France", "Germany"]),
    Game("What is the capital of Guinea?", "Conakry", ["Dakar", "Lagos", "Kampala"]),
    Game("Which of the following is not an African country?", "Malaysia", ["Madagascar", "Djibouti", "South Africa", "Zimbabwe"])]
    # the above list consists of the question, a correct answer, and a list of incorrect answers. It follows the structure of the class GAME
    count = 0 # to keep the score updated by counting the number of correct answers
    random.shuffle(ques_List) # to shuffle the questions and the wrong answers
    for i in ques_List: # to check and go over everything in the list named ques_List
        # after it checks it prints the questions out
        print("Your options are:\n" + i.question) # followed by this line
        possibilities = i.wrong_answ + [i.correct_answ] # to store correct answers in a list followed by wrong answers
        random.shuffle(possibilities) # and print them along with the wrong answers in a random order
        index = 0 #where the list starts
        while index < len(possibilities): # make sure that the index number is less than the length of the list 
            print(str(index+1) + ": " + possibilities[index]) #transforms index into a string and prints all options at the speciifc index in order 
            index += 1 #increments the index number
        player_input = input("Please enter the number next to your answer:\n")# ask the player to input the index number
        while not player_input.isdigit(): # check if the player inputed a digit
            print("That was not a number. Please enter a number.") # if not print this
            player_input = input("Please enter the number next to your answer:\n") # and ask the player to input again
        player_input = int(player_input) # convert player input to an integer
        while not (player_input > 0 and player_input <= len(possibilities)): #check if the player inputed a number that is not negative and matches the possibilities
            print("That number doesn't correspond to any answer.") # if not a number within that scope prints
            player_input = input("Please enter the number next to your answer:\n") # ask them again
        if possibilities[player_input-1] == i.correct_answ: # if the input matches the correct answer, -1 because the list starts at index 0
            print("Your answer was correct.\n") # print this
            count += 1 # increment the score
        else:
            print("Your answer was wrong.\n") # if not print this
    #print(("You answered {} out of {} questions correctly").format(str(count), len(ques_List)))
    print("You answered " + str(count) + " out of " + str(len(ques_List)) + " questions correctly.") # this tells how many they answered correctly
    if count < 5: # if score less than 5
        print("Sorry! You lost at Geography!\n") # you loose
    elif count == 5: # if score = 5
        print ("Congrats! You won!\n") # you win
# all the following functions are built based on the first one! they have the same structure just different answers

def math():
    ques_List = [Game("Which of these numbers can be divided exactly by 8?", "560", ["514", "483","596"]),
    Game("Who wrote the first textbook in Differential Calculus?", "Guillaume de l’Hôpital ", ["Pythagore", "Hooke", "Socrates"]),
    Game("Y = 34x – 160, what are the values of y when x = 2, 3, 4?", "-92, -58, -24", ["340,140,98", "-168, -34, -120", "92,58,24"]),
    Game("What is the ratio of the rate at which the volume of a spherical bubble of radius r increases to the rate its radius increases?", "4πr^2:1", ["πr^2:1", "4/3π:1", "2π:1"]),
    Game("What is the GCD of 36 and 42?", "6",["4","8", "2", "7"])]
    count = 0
    random.shuffle(ques_List)
    for i in ques_List:
        print("Your options are:\n" + i.question)
        possibilities = i.wrong_answ + [i.correct_answ] 
        random.shuffle(possibilities)
        index = 0
        while index < len(possibilities):
            print(str(index+1) + ": " + possibilities[index])
            index += 1
        player_input = input("Please enter the number next to your answer:\n")
        while not player_input.isdigit():
            print("That was not a number. Please enter a number.")
            player_input = input("Please enter the number next to your answer:\n")
        player_input = int(player_input)
        while not (player_input > 0 and player_input <= len(possibilities)):
            print("That number doesn't correspond to any answer. Please enter the number next to your answer:\n")
            player_input = input()
        if possibilities[player_input-1] == i.correct_answ:
            print("Your answer was correct.\n")
            count += 1
        else:
            print("Your answer was wrong.\n")
    print("You answered " + str(count) + " out of " + str(len(ques_List)) + " questions correctly.")
    if count < 5:
        print("Sorry! You lost at math!\n")
    elif count == 5:
        print ("Congrats! You won!\n")
    
    
def french():
    ques_List = [Game("what does Bonjour mean in English?", "Good Morning", ["Good Afternon", "Good bye","Good Evening"]),
    Game("Which of the following is the verb EAT?", "Manger ", ["Aller", "Dormir", "Courir"]),
    Game("How do we say BED in french?", "lit", ["chambre", "salon", "valise"]),
    Game("Which of the following means Tired?", "Fatigue", ["Abattie", "Enjaille", "Heureux"]),
    Game("What is the pronoun SHE in French", "Elle",["Elles","Nous", "Ils", "Vous"])]
    count = 0
    random.shuffle(ques_List)
    for i in ques_List:
        print("Your options are:\n" + i.question)
        possibilities = i.wrong_answ + [i.correct_answ] 
        random.shuffle(possibilities)
        index = 0 
        while index < len(possibilities):
            print(str(index+1) + ": " + possibilities[index])
            index += 1
        player_input = input("Please enter the number next to your answer:\n")
        while not player_input.isdigit():
            print("That was not a number. Please enter a number.")
            player_input = input("Please enter the number next to your answer:\n")
        player_input = int(player_input)
        while not (player_input > 0 and player_input <= len(possibilities)):
            print("That number doesn't correspond to any answer. Please enter the number next to your answer:\n")
            player_input = input()
        if possibilities[player_input-1] == i.correct_answ:
            print("Your answer was correct.\n")
            count += 1
        else:
            print("Your answer was wrong.\n")
           
    print("You answered " + str(count) + " out of " + str(len(ques_List)) + " questions correctly.")
    if count < 5:
        print("Sorry! You lost at french!\n")
    elif count == 5:
        print ("Congrats! You won!\n")

def rap():
    ques_List = [Game("Which rapper was  featured on the song Psycho of Post Malone?", "Ty Dolla $ign", ["Quavo", "Offset"," Young Thug"]),
    Game("Which rapper has a song named Money?", "Cardi B",["Nicki Minaj", "Iggy Azelia", "Rihanna"]),
    Game("What is the real name of Nicki Minaj ?", "Onika Tanya Maraj", ["Kimberly Denis", "Melissa Elliot", "Aaliyah Keef"]),
    Game("What is the stage name of the rapper named Marshall Bruce Mathers III?", "Eminem", ["Kanye", "21 Savage", "Drake"]),
    Game("Choose the rapper who sang these lyrics: <I'm the highest in the room.Hope I make it outta here> ?", "Travis Scott", ["Lil Wayne", "Lil pump", "Dr. Dre ", "Jay-Z"])]
    count = 0
    random.shuffle(ques_List)
    for i in ques_List:
        print("Your options are:\n" + i.question)
        possibilities = i.wrong_answ + [i.correct_answ] 
        random.shuffle(possibilities)
        index = 0 
        while index < len(possibilities):
            print(str(index+1) + ": " + possibilities[index])
            index += 1
        player_input = input("Please enter the number next to your answer:\n")
        while not player_input.isdigit():
            print("That was not a number. Please enter a number.")
            player_input = input("Please enter the number next to your answer:\n")
        player_input = int(player_input)
        while not (player_input > 0 and player_input <= len(possibilities)):
            print("That number doesn't correspond to any answer. Please enter the number next to your answer:\n")
            player_input = input()
        if possibilities[player_input-1] == i.correct_answ:
            print("Your answer was correct.\n")
            count += 1
        else:
            print("Your answer was wrong.\n")
    print("You answered " + str(count) + " out of " + str(len(ques_List)) + " questions correctly.")
    if count < 5:
        print("Sorry! You lost at rap!\n")
    elif count == 5:
        print ("Congrats! You won!\n")


def trivia():
    ques_List = [Game("What is the 2020 pandemic?", "Coronavirus", ["Ebola", "HIV","flu"]),
    Game("What is the world largest mammal?", "Blue mammal", ["human", "elephant", "lion"]),
    Game("Bees are found on every continent expect?", "Antarctica", ["Africa", "America", "Europe"]),
    Game("What is the heaviest element in nature?", "Uranium", ["Zinc", "Copper", "Iron"]),
    Game("What is a group of lions known as?", "pride", ["murder", "squad", "sprat"])]
    count = 0
    random.shuffle(ques_List)
    for i in ques_List:
        print("Your options are:\n" + i.question)
        possibilities = i.wrong_answ + [i.correct_answ] 
        random.shuffle(possibilities)
        index = 0 
        while index < len(possibilities):
            print(str(index+1) + ": " + possibilities[index])
            index += 1
        player_input = input("Please enter the number next to your answer:\n")
        while not player_input.isdigit():
            print("That was not a number. Please enter a number.")
            player_input = input("Please enter the number next to your answer:\n")
        player_input = int(player_input)
        while not (player_input > 0 and player_input <= len(possibilities)):
            print("That number doesn't correspond to any answer. Please enter the number next to your answer:\n")
            player_input = input()
        if possibilities[player_input-1] == i.correct_answ:
            print("Your answer was correct.\n")
            count += 1
        else:
            print("Your answer was wrong.\n")
    print("You answered " + str(count) + " out of " + str(len(ques_List)) + " questions correctly.")
    if count < 5:
        print("Sorry! You lost at trivia!\n")
    elif count == 5:
        print ("Congrats! You won!\n")

