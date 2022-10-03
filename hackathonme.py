import random
import time
def printLine(line):
    for letter in line:
        print(letter,end='')
        time.sleep(0.01)

dining_dollars = 0
energy_points = 0
key = False
book = False
flagpole = False

def food():
    global dining_dollars
    if dining_dollars>0:
        place = input('Feeling tired? Where do you want to eat now?\n')
        if place == 'C':
            chick_fila()
        if place == 'B':
            blue_donkey()
        if place == 'D':
            halls = ['W','N','B']
            randhall = halls[random.randrange(len(halls))]
            if randhall == 'W':
                willage()
            if randhall == 'N':
                north_ave()
            if randhall == 'B':
                brittain()
        else:
            printLine('Not an option! Read the instructions carefully.')
            food()
    else:
        printLine("Sorry you've run out of money!")
        


def blue_donkey():
    global energy_points
    global dining_dollars
    printLine("You are now at blue donkey, the perfect place for sleep deprived students\nYou think to yourself: hot coffee would be perfect to keep you up!\nThe lady at the desk asks\n")
    printLine('A hot coffee or a muffin?\n')
    coffee = input("")
    if coffee == 'hot coffee':
        energy_points += 1
    else:
        printLine('Caffeine is more efficient when it comes to energy!\n')
        blue_donkey()


def chick_fila():
    global energy_points
    global dining_dollars
    printLine('You arrived to the most famous food truck at Georgia Tech!\nThe line is long but their famous spicy chicken will give you the right amount \nof spice to continue your arduous journey!\n')
    printLine('After your long wait, you aproach the cashier and you order a\n')
    sandwich = input('')
    if sandwich == 'spicy chicken':
        energy_points += 1
        dining_dollars -= 2
    else:
        printLine('Chick-Fil-a has much better things to offer!\n')
        chick_fila()


def north_ave():
    global energy_points
    global dining_dollars
    printLine("Nave won't be your favorite but it does the job\n From the food you can get an icecream,chicken,tofu and salad.\n")
    printLine("Pick wisely, you need a sufficient amount of protein to succeed in your journey.\n")
    choice = input('')
    if choice == 'salad':
        energy_points += 1
        dining_dollars -= 2
    if choice == 'ice cream':
        energy_points += 0.5
        dining_dollars -= 3
    if choice == 'chicken'or choice == 'tofu':
        energy_points += 2
        dining_dollars -= 3
    else:
        printLine("You're at Nave, don't get too creative! Your options are limited.\n")
        north_ave()



def bagelBros():
    global energy_points
    global dining_dollars
    printLine("Everything Bagels is all we're offering today! Enjoy your meal!\n")
    energy_points += 1
    dining_dollars -= 2
    
def smoothieLand():
    global energy_points
    printLine("We all love the the Smoothie clerk!\nShe's sweet and fast\nShe offers you a smoothie for free! It's a Lucky Day!\n")
    energy_points += 0.5
    
def brittain():
    global energy_points
    global dining_dollars
    printLine("Welcome to Brittain! Looks similar to the Harry Potter dining Hall doesn't it?!\nWhat's special about brittain is that they offer a wide range\nof breakfast options at any time of the day!\n")
    printLine('You have two stations: the Smoothie Station and the Bagel Station\nWhere would you rather eat?\n')
    place = input('')
    if place == 'Bagel Station':
        bagelBros()
    if place == 'Smoothie Station':
        smoothieLand()
    else:
        printLine('That place is closed! Sorry!\n')
        brittain()
def willage():
    global energy_points
    global dining_dollars
    printLine('Welcome to Willage! Today is Make your Own Waffle Day!\nYou can Head to the station and make your Waffle!\n')
    energy_points += 1
    dining_dollars -= 2

def towers():
    wrong_answer = 0
    global energy_points
    global key
    printLine('You remember that your friend Isabelle works at the registration office at Tech Tower.\nShe must have the key!\nYou decide to visit her at her dorm in towers\nYou knock...No answer.\nYou knock again..."WHAT?!"\n')
    printLine("Isabelle is not very nice today and she decides to put you to the test!\nShe proceeds to ask:\'Feed me anything and I'll grow but give me water and I'll die.\'\nWho am I?\n")
    printLine('Beware, you only get three tries before you start losing points!\n')
    answer = input('')
    while wrong_answer<2:
        if answer.lower() == 'fire':
            printLine('WOW!You guessed it! Isabelle gives you the key, grunts and slams the door!At least you got the key!')
            key = True
            break
        else:
            printLine('No, Try again!\n')
            wrong_answer += 1
            answer = input('')
            continue
    if wrong_answer == 2:
        energy_points -= 1
        towers()

def culc():
    location = 'Culc'
    global book
    global energy_points
    gtid = 903123633
    printLine("You get to the most famous place on campus! The CULC. However, it's 7pm and you need your buzzcard to get in! Bummer! You don't have it on you!\nYou approach a security guard and express your concern\n")
    printLine('"I can help you!" She says, "I just need your GTID #:"\n')
    printLine('You forgot your number so you try to guess it. Luckily you remember some of it! GTID# starts with 9031236! you just have to guess the last two digits\n')
    def guess():
        printLine('What is your full GTID #?\n')
        global energy_points
        global book
        try:
            trial = int(input(''))
            energy_points -= 0.1
            while trial != gtid:
                if trial< 903123600:
                    printLine('Your GTID consists of 9 digits!\n')
                elif trial>gtid:
                    printLine("Your Number is Lower than that!\n")
                elif trial<gtid:
                    printLine('Your Number is Higher than that!\n')
                printLine('What is your full GTID#\n')
                trial = int(input(''))
                if trial == gtid:
                    printLine("Cool! That's a Valid GTID! Welcome to the CULC!\nYou enter the building, retrieve the book you need and run out without anyone noticing you...\n")
                    book = True
                    break
        except:
            printLine('Not Valid!\n')
            guess()
    guess()


def brazil():
    global energy_points
    brazil = input('')
    while brazil.lower() != 'brazil':
        printLine("That is disappointing!Try again!\n")
        energy_points -= 1
        brazil = input('')
    if brazil.lower() == 'brazil':
        printLine('Bom Trabalho!\n')
def canada():
    global energy_points
    printLine("Next Flag:\nThis flag is red and white and contains a red maple leaf in the center!\n")
    canada = input('')
    while canada.lower() != 'canada':
        printLine("Mmhmm, Not quite! Guess again!\n")
        energy_points -= 1
        canada = input('')
    if canada.lower() == 'canada':
        printLine('Good Job!\n')
def france():
    global energy_points
    printLine("Last Flag:\nThis flag has 3 vertical stripes: Blue, White and Red!\n")
    france = input('')
    while france.lower() != 'france':
        printLine("Incorrect! What else?\n")
        energy_points -= 1
        france = input('')
    if france.lower() == 'france':
        printLine('Bravo!\n')

def flagBuilding():
    location = "Flag Building"
    points = 0
    global energy_points
    printLine('Welcome to the famous Flag Building!\nDid you know that Georgia Tech hangs a flag for the home countries of every student!\nIn order to access the valuable item you need,\nyou must make the international community proud!\n')
    printLine('I will describe a flag and you will have to guess the country it relates to!\nGood Luck!\n')
    printLine("First flag:\nThis flag has a green background, a yellow diamond in the middle containing a blue circle!\n")
    brazil()
    canada()
    france()
    printLine("You're a true georgraphy expert!\nYou run into the building.\nAfter looking at all the diverse flags hung up on the ceiling,\nyou pickup a flag pole and go on to your next stop...")
    flagpole = True

flagBuilding()

    
              
    
        
    



        
        
        
        
        
    
        
    
    
    
    
    
    





