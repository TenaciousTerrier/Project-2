# Thomas Hepner
# 10/15/2015
# Intro to Programming Nanodegree
# Project 2: Build a Mad Libs Game

### Project Specification and Criteria Notes ###
# 1. Build Reverse Mad-Libs: read a sentence with blanks in it and then fill in the blanks appropriately.
# 2. Game works
# 3. Code Review
#	- Variables
# 	- Functions
#	- Appropriate use of data
#	- Appropriate use of other coding techniques

### Game Specifications ###
#	- Has 3 or more levels with 4 or more blanks each
#	- immediately after beginning the game; user is prompted to select a difficulty for easy, medium, or hard
#	- once level is selected, game displays a fill-in-the-blank and a prompt to fill in the first blank

# Economics Lesson 1: Money
money_madlib = "Money has four functions. The first function is to serve as a medium of ___1___, to eliminate the inefficiencies of the barter system, and satisfy the Double Coincidence of Wants. The second function is a measure of ___2___; it acts as standard measure and can be used as a common denomination of trade. Money is also a standard of deferred ___3___, meaning it can be used to fulfill obligations of debt in the future. The fourth, and final function of money, is a ___4___ of value, meaning that the value of money must remain stable over time."

# Economics Lesson 2: Supply
supply_madlib = "The law of supply is a principle of economics which states that all else equal, an ___1___ in the price of a good results in an ___2___ of the quantity supplied. In this principle, there is a direct relationship between ___3___ and quantity. In the real world, this means that suppliers and producers of goods are willing to increase production of their goods and services as the prices of them increases in order to maximize their profits. The slope of the supply curve is ___4___ sloping."

# Economics Lesson 3: Demand
demand_madlib = "The law of demand is an economics principle which states that all else equal, an ___1___ in the price of a good results in a ___2___ in the quantity demanded. In this principle, there is a direct relationship between price and ___3___. In practice, the law means that purchases or customers of goods and services are willing to decrease their consumption, or purchases of these goods, as the prices of these goods increases. The slope of the demand curve is ___4___ sloping."

# Mablib Blanks and Answers
money_blanks = ["exchange", "value", "payment", "store"]
supply_blanks = ["increase", "increase", "price", "upward"]
demand_blanks = ["increase", "decrease", "quantity", "downward"]

def game_choice(difficulty):
	if difficulty == "easy":
		return demand_madlib
	if difficulty == "medium":
		return supply_madlib
	if difficulty == "hard":
		return money_madlib
	else:
		return None

def game_answers(difficulty):
	if difficulty == "easy":
		return demand_blanks
	if difficulty == "medium":
		return supply_blanks
	if difficulty == "hard":
		return money_blanks
	else:
		return None

def new_game(): 
	difficulty = raw_input("Do you want to play an easy, medium, or hard game? [Note: Please type 'easy', 'medium', or 'hard']: ")
	print ""
	output = [game_choice(difficulty), difficulty]
	if output[0] != None: 
		return output
	else:
		print "You did not choose an available game."
		print ""
		return new_game()

def fill_blanks(choice, difficulty):	
        print choice
        print ""
        correct_words = game_answers(difficulty)

        i = 0
        while i <= range(len(correct_words)-1):
                if i >= len(correct_words):
                        break
                user_input = raw_input("What is in the blank (___" + str(i + 1) + "___)? ")
                print ""
                if user_input == correct_words[i]:
                        i = i + 1
                        print "That is correct!"
                        print ""
                        choice = choice.replace("___" + str(i) + "___", user_input)
                        print choice
                        print ""
                else:
                        i = i
                        print "Try again!"
                        print ""
        # print choice
        print ""
        print "Congratulations! You have completed this exercise!"
        print ""

def play_game():
        print "Today you will be playing some reverse madlib games to help you study introductory economics concepts."
        print ""
        madlib = new_game()
        fill_blanks(madlib[0], madlib[1])
        user_input = raw_input("Do you want to keep playing (Y/N)? ")
        print ""
        print ""
        if user_input == "Y":
                play_game()
        else:
                print ""

### Play Game
play_game()


