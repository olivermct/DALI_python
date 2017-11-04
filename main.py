# Oliver McTammany
# AI to play the game Master Mind
# Colors are green=1, blue=2, yellow=3, red=4, white=5, and orange=6

from random import *

TURN_MAX = 10
global player_score
player_score = 0
global computer_score
computer_score = 0


# computer presents user with a possible solution and gets back a score to be analyzed
def turn(possible_solutions, spots, turn_num):
    print possible_solutions
    print "\nTurn " + str(turn_num+1)
    print "I guess " + make_string(spots[0]) + ", " + make_string(spots[1]) + ", " + make_string(spots[2]) + ", " + make_string(spots[3])
    result = raw_input().strip().split()
    num_red = 0
    num_white = 0
    for peg in result:
        if peg == "r":
            num_red += 1
        elif peg == "w":
            num_white += 1

    analyze(possible_solutions, spots, turn_num, num_red, num_white)


# translate the integer guess into human-readable string
def make_string(num):
    if num == 1:
        return "g"
    elif num ==2:
        return"b"
    elif num==3:
        return "Y"
    elif num ==4:
        return "r"
    elif num == 4:
        return "w"
    else:
        return "o"


# computer analyzes feedback from the user and ends the game or formulates another guess
def analyze(possible_solutions, spots, turn_num, num_red, num_white):
    global player_score
    global computer_score

    if turn_num >= TURN_MAX:
        computer_score += turn_num + 1
        print "You win! Congratulations!"
        print "Current score is you: " + str(player_score) + ", me: " + str(computer_score)
        print "To play again, type b to break the code or m to make it."
        main()

    elif num_red == 4:
        player_score += turn_num + 1
        print "I win! Thanks for playing!"
        print "Current score is you: " + str(player_score) + ", me: " + str(computer_score)
        print "To play again, type b to break the code or m to make it."
        main()

    guess = ""                                                      # create a 4 number string of the previous guess
    for spot in spots:
        guess += str(spot)

    n = 0                                                           # has to be while loop because deleting from list
    while n < len(possible_solutions):
        num = possible_solutions[n]
        if str(num) == guess and len(possible_solutions) > 1:       # previous guess didn't trigger end, so delete it
            del possible_solutions[n]
        else:
            theoretical_red = 0                                     # loop through all remaining possibilities and make
            theoretical_white = 0                                   # theoretical score for them. If it matches score
            checks = [False, False, False, False]                   # given by user, then is it still a possibility,
            string = str(num)                                       # otherwise delete
            for i in range(0, 4):
                if string[i] == guess[i]:                           # if matches, score as red
                    theoretical_red += 1
                    checks[i] = True
                else:                                               # scoring for a white peg
                    for j in range(0, 4):
                        if checks[j] == False and string[j] != guess[j] and guess[i] == string[j]:
                            checks[j] = True
                            theoretical_white += 1
                            break
            if theoretical_red != num_red or theoretical_white != num_white:      # score doesn't match user given score
                del possible_solutions[n]
            else:
                n += 1

    guess = str(possible_solutions[randint(0, len(possible_solutions) - 1)])      # get random guess from remaining
    for k in range (0, 4):
        spots[k] = int(guess[k])

    turn_num += 1
    turn(possible_solutions, spots, turn_num)                       # request user feedback on new guess


# give the computer what it needs to break code
def initialize(turn_num, spots):
    possible_solutions = []                             # create list of all possible solutions in game
    i = 1111
    while i <= 6666:
        string = str(i)
        check = 0
        for num in string:
            if int(num) > 0 and int(num) < 7:           # only allow numbers 1-6 because there are 6 colors
                check += 1
        if check > 3:
            possible_solutions.append(i)
        i += 1

    turn(possible_solutions, spots, turn_num)           # go to the first computer turn


# randomly create a code for the user to break
def randomize(turn_num):
    code = str(randint(1, 6)) + str(randint(1, 6)) + str(randint(1, 6)) + str(randint(1, 6))
    # print code
    print "\nOkay, what do you guess?"
    score(code, turn_num)


# retrieve user guess and score it against generated code
def score(code, turn_num):
    global player_score
    global computer_score

    user_guess = raw_input().strip().split()
    guess = ""
    for elem in user_guess:
        if elem == "g":
            guess += "1"
        elif elem == "b":
            guess += "2"
        elif elem == "y":
            guess += "3"
        elif elem == "r":
            guess += "4"
        elif elem == "w":
            guess += "5"
        else:
            guess += "6"

    if code == guess:
        computer_score += turn_num + 1
        print "You win! Congratulations!"
        print "Current score is you: " + str(player_score) + ", me: " + str(computer_score)
        print "To play again, type b to break the code or m to make it."
        main()

    else:
        turn_num += 1
        if turn_num >= TURN_MAX:
            player_score += turn_num + 1
            print "I win! Better luck next time."
            print "Current score is you: " + str(player_score) + ", me: " + str(computer_score)
            print "To play again, type b to break the code or m to make it."
            main()

        output = ""
        red_pegs = 0                                            # same scoring procedure as above
        white_pegs = 0
        checks = [False, False, False, False]
        for i in range(0, 4):
            if code[i] == guess[i]:
                red_pegs += 1
                checks[i] = True
            else:
                for j in range(0, 4):
                    if checks[j] == False and code[j] != guess[j] and guess[i] == code[j]:
                        checks[j] = True
                        white_pegs += 1
                        break

        for i in range(0, red_pegs):
            output += "r "

        for i in range(0, white_pegs):
            output += "w "

        print output                                        # give user the score
        print "\nTurn " + str(turn_num + 1)                 # request next guess
        score(code, turn_num)


# player decides if they will try to break code themselves or have comptuer break the code they make
def main():
    turn_num = 0
    spots = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]    # initialize spots to a random guess
    if raw_input() == "m":
        initialize(turn_num, spots)
    else:
        randomize(turn_num)


print "Hello! Type b to break the code or m to make the code!"
main()
