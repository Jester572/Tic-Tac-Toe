# Jesse Earley
#W02 Prove: Developer - Solo Code Submission

def main():
    print('Welcome to Tic-Tac-Toe!')
    print('First player will be Xs and Second player will be Os.')
    print('The first player to get 3 in a row wins.')
    print('Pick a spot that has not been taken by typing the number')
    
    complete = False
    spot1 = '1'
    spot2 = '2'
    spot3 = '3'
    spot4 = '4'
    spot5 = '5'
    spot6 = '6'
    spot7 = '7'
    spot8 = '8'
    spot9 = '9'
    turn = 'X'
    while complete == False:        
        gameboard(spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9)
        print()
        print()
        spot = str(input(f'It is {turn}s turn'))
        if spot == "X" or spot == "O":
            print('This spot has already been taken. Chose a different spot.')
        elif spot == spot1:
            spot1 = turn
            turn = change_turn(turn)
        elif spot == spot2:
            spot2 = turn
            turn = change_turn(turn)
        elif spot == spot3:
            spot3 = turn
            turn = change_turn(turn)
        elif spot == spot4:
            spot4 = turn
            turn = change_turn(turn)
        elif spot == spot5:
            spot5 = turn
            turn = change_turn(turn)
        elif spot == spot6:
            spot6 = turn
            turn = change_turn(turn)
        elif spot == spot7:
            spot7 = turn
            turn = change_turn(turn)
        elif spot == spot8:
            spot8 = turn
            turn = change_turn(turn)
        elif spot == spot9:
            spot9 = turn
            turn = change_turn(turn)
        else: print('Please chose a number between 1 and 9')
        complete = check(spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9)
        if complete == 'draw':
            gameboard(spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9)
            print('The game ends in a draw. There is no winner. Try again.')
        elif complete == True:
            gameboard(spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9)
            print(f'Congradulations {turn}s wins')

def change_turn(turn):
    if turn == "X":
        turn = "O"
    else: turn = "X"
    return turn
    
    
def gameboard(spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9):
    print(f'   {spot1} | {spot2} | {spot3} ')
    print(f'  ---+---+---')
    print(f'   {spot4} | {spot5} | {spot6} ')
    print(f'  ---+---+---')
    print(f'   {spot7} | {spot8} | {spot9} ')
    
    
def check(spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9):
    if spot1 == spot1 and spot2 == spot1 and spot3 == spot1:
        return True
    elif spot4 == spot4 and spot5 == spot4 and spot6 == spot4:
        return True
    elif spot7 == spot7 and spot8 == spot7 and spot9 == spot7:
        return True
    elif spot1 == spot7 and spot4 == spot7 and spot7 == spot7:
        return True
    elif spot2 == spot2 and spot5 == spot2 and spot8 == spot2:
        return True
    elif spot3 == spot3 and spot6 == spot3 and spot9 == spot3:
        return True
    elif spot1 == spot1 and spot5 == spot1 and spot9 == spot1:
        return True
    elif spot3 == spot3 and spot5 == spot3 and spot7 == spot3:
        return True
    elif (spot1 == "O" or spot1 == "X") and (spot2 == "O" or spot2 == "X") and (spot3 == "O" or spot3 == "X") and (spot4 == "O" or spot4 == "X") and (spot5 == "O" or spot5 == "X") and (spot6 == "O" or spot6 == "X") and (spot7 == "O" or spot7 == "X") and (spot8 == "O" or spot8 == "X") and (spot9 == "O" or spot9 == "X"):
        return 'draw'
    else: return False
    
    
if __name__ == "__main__":
    main()