# Namiha Yasuda, namihay2@usc.edu
# ITP 116, Fall 2021
# Final Project

import random
import operator

def checkYNinput(statement):
    inp = input(statement)
    if (inp == 'y') or (inp == 'n'):
        return inp
    else:
        print("Please answer with y or n.")
        inp = checkYNinput(statement)
        return inp



def start():
    print("Welcome to Tic Tac Toe!")
    question = "Would you like to read from a previously saved scoreboard and update the scores after this game? (y or n): "
    yorn = checkYNinput(question)
    if yorn == 'y':
        filename = input("What's the file name?: ")
        inputFile = open(filename, "r")
        scoreboard = {}
        for line in inputFile:
            line = line.strip('\n')
            linelist = line.split(", ")
            scoreboard.update({ linelist[0]: int(linelist[1]) })
        inputFile.close()
        print("File read!")
        print("------")
        return [scoreboard, filename, True, "player 1", 0, "player 2", 0, 0, [[],[]], 1, False]
    else:
        print("We will create a new scoreboard at the end.")
        scoreboard = {}
        print("------")
        return [scoreboard, 'scoreboard.txt', False, "player 1", 0, "player 2", 0, 0, [[],[]], 1, False]



def checkName(scoreboard, num):
    playerNum = str(num)
    name = input("What's the name of player "+playerNum+"? ")
    if name in scoreboard.keys():
        question = "The name "+name+" already exists on the scoreboard. Are you a returning player? If you're a new player, please answer n and type a different name. (y or n): "
        yorn = checkYNinput(question)
        if yorn == 'y':
            print("Welcome to the game "+name+"!")
            return [scoreboard, name]
        else:
            returnlist = checkName(scoreboard, num)
            return returnlist
    else:
        print("Welcome to the game " + name + "!")
        scoreboard.update({name: 0})
        return [scoreboard, name]



def playerNames(list):
    newlist = checkName(list[0], 1)
    list[3] = newlist[1]
    list[0] = newlist[0]
    newlist = checkName(list[0], 2)
    list[5] = newlist[1]
    list[0] = newlist[0]
    print("------")
    return list



def printTicTacToe(list):
    player1List = list[8][0]
    player2List = list[8][1]
    i = 1
    while i < 10:
        if (i == 3) or (i == 6) or (i == 9):
            if i in player1List:
                print('X')
            elif i in player2List:
                print('O')
            else:
                print(i)
        else:
            if i in player1List:
                print('X', end=" ")
            elif i in player2List:
                print('O', end=" ")
            else:
                print(i, end=" ")
        i += 1
    print("---")



def startGame(list):
    num = random.randint(1,2)
    if num == 1:
        list[7] = 1
        print("Based on a randomized selection, "+list[3]+" will go first for this game.")
        print(list[3]+"'s mark will be 'X' and "+list[5]+"'s mark will be 'O'.")
    else:
        list[7] = 2
        print("Based on a randomized selection, " + list[5] + " will go first for this game.")
        print(list[5] + "'s mark will be 'X' and " + list[3] + "'s mark will be 'O'.")

    print("Start:")
    printTicTacToe(list)
    return list



def menu():
    answered = False
    print("Menu:")
    print("1. Go to next turn")
    print("2. Go back to a certain turn")
    print("3. Start over the entire game")
    print("4. Exit")
    while answered == False:
        inp = input("What would you like to do?: ")
        if inp.isnumeric():
            if int(inp) in [1, 2, 3, 4]:
                return int(inp)
            else:
                print("Please choose a number that's in range.")
        else:
            print("Please type a number.")



def checkNum(list, rangeMax, sta, turn):
    if turn == True:
        answered = False
        while answered == False:
            place = input(sta)
            if place.isnumeric():
                if (int(place) in list[8][0]) or (int(place) in list[8][1]):
                    print("Please choose a number that does not have a mark placed on it.")
                elif (int(place) > rangeMax) or (int(place) < 1):
                    print("Please choose a number that's in range.")
                else:
                    return int(place)
            else:
                print("Please type a number.")
    else:
        answered = False
        while answered == False:
            place = input(sta)
            if place.isnumeric():
                if (int(place) > rangeMax) or (int(place) < 1):
                    print("Please choose a number that's in range.")
                else:
                    return int(place)
            else:
                print("Please type a number.")



def op1(list):
    turnNum = list[9]
    turnNumstr = str(turnNum)
    if list[7] == 1:
        firstPlayer = list[3]
        secondPlayer = list[5]
    else:
        firstPlayer = list[5]
        secondPlayer = list[3]

    print("Turn "+turnNumstr+":")
    if turnNum%2==1: #odd num, player that went first
        statement = firstPlayer + ", in which number would you like to place your mark?: "
        mark = checkNum(list, 9, statement, True)
        list[8][0].append(mark)
    else: #even num, player that went second
        statement = secondPlayer + ", in which number would you like to place your mark?: "
        mark = checkNum(list, 9, statement, True)
        list[8][1].append(mark)
    printTicTacToe(list)
    list[9] = list[9] + 1
    return list



def turnBack(list, turnNum):
    # turn num is 2, we have to restore turn 1
    currentTurn = list[9] # which would be 8 in this case, but only up to 7 is in the list
    diff = currentTurn - turnNum # which would be 8 - 2, 6
    if diff%2 == 0:
        if len(list[8][0]) > len(list[8][1]):
            i = 0
            while i < (diff//2):
                list[8][0].pop()
                list[8][1].pop()
                i += 1
        else:
            i = 0
            while i < (diff//2):
                list[8][1].pop()
                list[8][0].pop()
                i += 1
    else:
        if len(list[8][0]) > len(list[8][1]):
            i = 0
            list[8][0].pop()
            while i < (diff//2):
                list[8][1].pop()
                list[8][0].pop()
                i += 1
        else:
            i = 0
            list[8][1].pop()
            while i < (diff//2):
                list[8][0].pop()
                list[8][1].pop()
                i += 1

    turnNumstr = str(turnNum)
    print("Before Turn " + turnNumstr + ":")
    printTicTacToe(list)
    list[9] = turnNum
    newlist = op1(list)
    return newlist



def op2(list):
    maxTurnNum = list[9] - 1
    statement = "Which turn would you like to go back to?: "
    turn = checkNum(list, maxTurnNum, statement, False)
    newlist = turnBack(list, turn)
    return newlist



def checkWinner(list): # check winner function
    # winning situation
    # list- [scoreboard, filename, True, "player 1", 0, "player 2", 0, 0, [[],[]], 1]
    wonBool = False

    win = []
    win.append([1, 2, 3])
    win.append([4, 5, 6])
    win.append([7, 8, 9])
    win.append([1, 4, 7])
    win.append([2, 5, 8])
    win.append([3, 6, 9])
    win.append([1, 5, 9])
    win.append([3, 5, 7])

    for x in win:
        if all(elem in list[8][0] for elem in x):
            if list[7] == 1:
                print(list[3] + " won! Congratulations!")
                list[4] = 1 + list[4]
            else:
                print(list[5] + " won! Congratulations!")
                list[6] = 1 + list[6]
            wonBool = True
            break
        elif all(elem in list[8][1] for elem in x):
            if list[7] == 2:
                print(list[3] + " won! Congratulations!")
                list[4] = 1 + list[4]
            else:
                print(list[5] + " won! Congratulations!")
                list[6] = 1 + list[6]
            wonBool = True
            break

    if wonBool:
        list[8] = [[], []]
        list[9] = 1

        question = "Would you like to play again? (y or n): "
        yorn = checkYNinput(question)
        print("------")
        if yorn == 'y':
            newlist = startGame(list)
            newlist = op1(newlist)
            return newlist
        else:
            list[10] = True
            return list
    else:
        return list



def op3(list):
    print("------")
    list[9] = 1
    list[8] = [[],[]]
    list[7] = 0
    newlist = startGame(list)
    newlist = op1(newlist)
    return newlist



def endGame(list):
    # print scores
    list4str = str(list[4])
    list6str = str(list[6])
    print(list[3] + ": " + list4str + ", " + list[5] + ": " + list6str)

    # update portfolio with new scores
    d = list[0]
    newscore1 = d[list[3]] + list[4]
    d.update({list[3]: newscore1})
    newscore2 = d[list[5]] + list[6]
    d.update({list[5]: newscore2})
    sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))

    # print them out in a file
    outputFile = open(list[1], "w")
    for key in sorted_d:
        print(key + ", " + str(sorted_d[key]), file=outputFile)
    outputFile.close()

    if list[2] == True:
        print("Your scoreboard (" + list[1] + ") has been updated!")
    else:
        print("A new scoreboard (" + list[1] + ") has been created!")
    print("Thank you for playing!")



def main():
    # starting game first time
    gamelist = start()
    gamelist = playerNames(gamelist)
    gamelist = startGame(gamelist)
    gamelist = op1(gamelist)

    while True:
        menuNum = menu()
        if menuNum == 4:
            endGame(gamelist)
            break
        elif menuNum == 1:
            gamelist = op1(gamelist)
        elif menuNum == 2:
            gamelist = op2(gamelist)
        else: # menuNum == 3
            gamelist = op3(gamelist)


        gamelist = checkWinner(gamelist)
        if gamelist[10]:
            endGame(gamelist)
            break

main()