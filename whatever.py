# Import Section

import re  # not used. Package is for RegEx (Regular Expressions)
import inquirer  # used for the main menu
import ast  # used to convert string array into an actual dictionary that python uses
# uses pip3 install numpy to install this package. Used to process arrays
import numpy as np




# Global Variables

file = ""  # global variable so we can reference it anywhere in the code
# global variable so we can access individual lines of the file anywhere in the code
fileArr = np.array([])
choice = ""
menu_options = [
    inquirer.List('menu', message="What would you like to do?",
                  choices=['Add a coin', 'Delete a coin', 'Calculator','List coins', 'List portfolio', 'Exit'])
]



# Function Section

def load_file():
    global file  # reference the global variable from above inside of a function
    global fileArr  # same as above
    # open a file named answers.txt as read only
    file = open('answers.txt', 'r')
    # read all the lines in the file and save to fileArr variable
    fileArr = file.readlines()
    arrLen = len(fileArr)  # grab the length of the array from above
    for x in range(arrLen):  # loop through each item in the array/list
        # convert and assign the current value from string to dictionary to the same index in the list/array
        fileArr[x] = ast.literal_eval(fileArr[x])
    file.close()

def add_coins():
    # created variable with questions to ask. This one is for adding coins
    init_questions = [inquirer.Text('amount', message="How many coins?")]
    repeat_questions = [
        inquirer.Text('name', message="What's the coin?"),
        inquirer.Text('apy', message="What's the APY?"),
        inquirer.Text('initial', message="What's your initial investment?")
    ]  # created variable with questions to ask. This one is used for looping and filling in the information for each coin
    amount = inquirer.prompt(init_questions)  # ask user init_question
    # for x = 0 until the range of the length of the array is met
    for x in range(int(amount['amount'])):
        # ask the repeat_questions and store in variable
        answers = inquirer.prompt(repeat_questions)
        file = open("answers.txt", "a+")  # open the file with append
        # convert answers, which is in dictionary form, into a string to store into file
        file.write(str(answers))
        # add a newline at the end to ensure next coin is under
        file.write("\n")
        file.close()  # close to finalize the writes to file
    loop_menu()

def read_file(whatever):
    file = open(whatever, "r")
    print(file.read())
    file.close()

def list_portfolio():
    for x in range(len(fileArr)):  # going through the array of imported information
        string_builder = "Ticker: {} || APY: {} || Investment: {}".format(
            fileArr[x]['name'], fileArr[x]['apy'], fileArr[x]['initial'])
        # this is the format of the portfolio. the {} curly braces represent areas that need filling. we use format and give it 3 arguments. the coin, apy and initial investment to fill in the braces respectively.
        print(string_builder)
    loop_menu()

def list_coins():
    for x in range(len(fileArr)):  # going through the array of imported information
        string_builder = "Coin: {}".format(
            fileArr[x]['name'])
    # this is the format of the coins. the {} curly braces represent areas that need filling. we use format and give it 1 argument. the coin name and the braces get filled.
        print(string_builder)
    loop_menu()

def delete_coin():
    print(fileArr)
    nameArr = []
    for x in range(len(fileArr)):
        nameArr.append(fileArr[x]['name'])
    coin_options = [inquirer.List(
        'coins', message="Which coin would you like to delete?", choices=nameArr)]
    choice = inquirer.prompt(coin_options)
    index = nameArr.index(choice['coins'])
    fileArr.pop(index)
    print('new fileArr')
    print(str(fileArr))
    file = open("answers.txt", "w")  # open the file with write
    for x in range(len(fileArr)):
        file.write(str(fileArr[x]))
        file.write("\n")
    file.close()
    loop_menu()
    
def loop_menu():
    global choice
    global menu_options
    choice = ""
    choice = inquirer.prompt(menu_options)

def die():
    print("Good bye!")

def read_arr(index):
    print("You wish to read the loaded array..")
    print(fileArr[index])

def std_calculation(ansArr):
    apy = int(ansArr['apy'])
    initial = int(ansArr['initial'])
    years = int(ansArr['years'])
    return_val = initial
    print("Current return val: {}".format(return_val))
    for x in range(years):
        print('In Loop')
        return_val = ((apy/100) * return_val) + return_val 
        print("return val: {}".format(return_val))
    print("Final return val: {}".format(return_val))


    return return_val

def calculator():
    print('inside of calculator')
    std_questions = [ inquirer.Text('apy', message="What is the APY?"), inquirer.Text('initial', message="How much do you have to invest?"), inquirer.Text('years', message="How many years?") ]
    goal_questions = [ inquirer.Text('goal', message="How much money do you want to make?"), inquirer.Text('initial', message="How much do you have to invest?"), inquirer.Text('years', message="How many years do you wish to wait?") ]
    calc_options = [ inquirer.List('calc', message="Choose calculator type:", choices=['Standard Calculator', 'Goal Calculator']) ]
    calc_choice = inquirer.prompt(calc_options)
    if calc_choice['calc'] == "Standard Calculator":
        print('chose standard calculator')
        std_answers = inquirer.prompt(std_questions)
        str_builder = "For initial investment of ${} and an APY of {}% for {} year(s) you would expect to receive ${}".format(std_answers['initial'], std_answers['apy'], std_answers['years'], std_calculation(std_answers))
        print(str_builder)
    if calc_choice['calc'] == "Goal Calculator":
        print('chose goal calculator')
        goal_answers = inquirer.prompt(goal_questions)
        str_builder = "For your goal of ${} and initial invest of ${} and a waiting period of {}, you would require an APY of {}% to achieve this goal.".format()




# Start Program == Anything above isn't run besides the importing and declaration of global variables ==


load_file()  # load the file and its content for use in the menu

read_arr(0) # read the first entry in the array. This should be what you were asking about to Andrea
print(type(fileArr[0])) # what is the object stored in this array/list ? type will tell you
# the above should be a dictionary or dict for short. In normal programming this looks identical to JSON
# you can call individual words or 'keys' as they should be called. JSON and most likely dictionary, don't quote
# me since I'm no python guy, store information as key-value pairs.
# Example
# {
#    'key': 'value',
#    'name': 'Bob'
# }
# you can then call the key as follows fileArr[0] <= this returns the first dictionary in the array
# fileArr[0]['name'] should spit out the first name of the coin stored in answers
print(fileArr[0]['name']) # this is how you access the information so you can do calculations
# something like int(fileArr[0]['apy']) * int(fileArr[0]['initial']) * years => something  
loop_menu()



# Based of choise, call a function

if choice['menu'] == "Add a coin":
    print('chose add a coin')
    add_coins()
if choice['menu'] == "Delete a coin":
    print('chose delete a coin')
    delete_coin()
if choice['menu'] == "Calculator":
    print('chose calculator')
    calculator()
if choice['menu'] == "List coins":
    print('chose list coins')
    list_coins()
if choice['menu'] == "List portfolio":
    print('chose portfolio')
    list_portfolio()
if choice['menu'] == "Exit":
    print('chose exit')
    die()
