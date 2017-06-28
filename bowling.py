'''
Created on Jun 28, 2017

@author: Matt
uses Python 3.6
expects user to enter a valid string representing
a game of bowling and returns total score
'''
#from pip._vendor.distlib.compat import raw_input

def calc_score(rounds):
    total_score = 0
    num_of_rounds = 0 
    
    #user_input = raw_input("Input a valid sequence of rolls for one line of American Ten-Pin Bowling.")
    #user_input = user_input.strip()

    #rows = list(user_input)
    rows = list(rounds.strip())
    for i in range(len(rows)):
        if str(rows[i]) == "-":
            rows[i] = 0
        if str(rows[i]).lower() == "x":
            rows[i] = 10
        if str(rows[i]) == "/":
            continue 

    for i in range(len(rows)):
        if i+2 < len(rows) and rows[i] == 10:
            num_of_rounds += 2
            if i+2 < len(rows) and rows[i+2] == "/":
                total_score += 10 + 10
            else:
                total_score += 10 + int(rows[i+1]) + int(rows[i+2])
        elif rows[i] =="/":
            num_of_rounds += 1
            total_score += int(rows[i+1])
        elif 0 <= int(rows[i]) <= 9:
            num_of_rounds += 1
            if i+1 < len(rows) and rows[i+1] == "/":
                total_score += 10
            else:
                total_score += int(rows[i])
        if num_of_rounds == 20:
            break
        
        
    return ("The total score for this game: " + str(total_score))