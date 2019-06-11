#This program is used to make a TicTacToe game for two players.
#Player  1 has X symbol and Player 2 has O symbol


board = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
player = 1
Win = 1
Draw = -1
Running = 0
Stop = 1
Game = Running
symbol = 'X'


# This Function Draws THe Game Board
def Board():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")


# Checks position is empty or not
def Available(x):
    if (board[x] != 'X'  and board[x] != 'O'):
        return True
    else:
        print("That place is already taken!!")
        return False

def CheckWin():
    global Game
    if (board[1] == board[2] and board[2] == board[3] and board[1] != '1'): 
        Game = Win
    elif (board[4] == board[5] and board[5] == board[6] and board[4] != '4'):
        Game = Win
    elif (board[7] == board[8] and board[8] == board[9] and board[7] != '7'):
        Game = Win
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != '1'):
        Game = Win
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != '2'):
        Game = Win
    elif (board[3] == board[6] and board[6] == board[9] and board[3] != '3'):
        Game = Win
    elif (board[1] == board[5] and board[5] == board[9] and board[5] != '5'):
        Game = Win
    elif (board[3] == board[5] and board[5] == board[7] and board[5] != '5'):
        Game = Win
        
     #Draw Condition
    elif (board[1] != '1' and board[2] != '2' and board[3] != '3' and board[4] != '4' and board[5] != '5' and board[
        6] != '6' and board[7] != '7' and board[8] != '8' and board[9] != '9'):
        Game = Draw
    else:
        Game = Running


print("XOXOXO  TIC TAC TOE  XOXOXO")
print("Player 1 [X] --- Player 2 [O]\n")
print()
print()
while (Game == Running):
    Board()
    if (player % 2 != 0):
        print("Player 1's Move")
        symbol = 'X'
    else:
        print("Player 2's Move")
        symbol = 'O'
    choice = int(input("Enter the position on the board : "))
    if (Available(choice)):
        board[choice] = symbol
        player += 1
        CheckWin()

Board()
if (Game == Draw):
    print("Game Draw")
elif (Game == Win):
    if (player % 2 != 0):
        print("Player 1 Won")
    else:
        print("Player 2 Won")