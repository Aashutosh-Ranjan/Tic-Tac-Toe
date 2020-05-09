from IPython.display import clear_output
from random import randint
from itertools import permutations
A,B,codes=[],[],[(1,2,3),(4,5,6),(7,8,9),(3,5,7),(1,5,9),(1,4,7),(2,5,8),(3,6,9)]
board=[]
inpboard=[]
first=''
last_chance=''
choiceA,choiceB='',''
regame=''
def randominpt():
    clear_output()
    global last_chance,first,board,inpboard,choiceA,choiceB,regame,A,B
    board=[0]+9*[' ']
    inpboard=['','1','2','3','4','5','6','7','8','9']
    first=''
    last_chance=''
    choiceA,choiceB='',''
    regame=''
    A=[]
    B=[]
    randnum=randint(0,1)
    if(randnum==0):
        first='A'
        last_chance='B'
    else:
        first='B'
        last_chance='A'
        
    return player_choice()
        
def player_choice():
    
    global choiceA,choiceB,first
    if(first=='A'):
        choiceA=input('Player A selected by random, enter a character of your choice as input => ')
        while(len(choiceA)!=1):
            choiceA=input('Enter a single character as input => ')
    
    elif(first=='B'):
        choiceB=input('Player B selected by random, enter a character of your choice as input => ')
        while(len(choiceB)!=1):
            choiceB=input('Enter a single character as input => ')
    
     
    return input_no()
        
def input_no():
    global A,B,choiceA,choiceB,board,inpboard,last_chance,regame
    ticboard()

    if (last_chance=='B'):

        if(choiceA==''):
            choiceA=input(' Player A, Enter your choice of character as input => ')
            while(len(choiceA)!=1 or choiceA.lower()==choiceB.lower()):
                choiceA=input('Player A, Please enter a single character and different input from B => ')
        ip=(int(input('Please enter a number for the board position choice Player A => ')))
        if(board[ip]==' '):
            inpboard[ip]=' '
            board[ip]=choiceA
            A.append(ip)
            last_chance='A'

        else:
            while(board[ip]!=' ' or str(ip) not in inpboard):
                ip=(int(input('Invalid input, Enter again Player A => ')))
            A.append(ip)
            board[ip]=choiceA
            inpboard[ip]=' '
            last_chance='A'

    else:

        if(choiceB==''):
            choiceB=input(' Player B, Enter your choice of character as input => ')
            while(len(choiceB)!=1 or choiceA.lower()==choiceB.lower()):
                choiceB=input('Player B, Please enter a single character and different input from A => ')
            
        ip=(int(input('Please enter a number for the board position choice Player B => ')))
        if(board[ip]==' '):
            board[ip]=choiceB
            inpboard[ip]=' '
            B.append(ip)
            last_chance='B'
        else:
            while(board[ip]!=' ' or str(ip) not in inpboard):
                ip=(int(input('Invalid input, Enter again Player B => ')))
            B.append(ip)
            board[ip]=choiceB
            inpboard[ip]=' '
            last_chance='B'
        
        
        
    
    if(winchk()!='None'):
        
        print(winchk())
        regame=input('Do you want to play again [Y/N] => ')
        while(regame.lower() not in ['y','n']):
            regame=input('Answer only in [Y/N] => ')
        if(regame.lower()=='y'):
            randominpt()
        elif(regame.lower()=='n'):
            print("____ __ _ Thanks for playing _ __ ____")
    else:
        input_no()


def ticboard():
    clear_output()
    global board,inpboard,choiceA,choiceB
    print('   |   |\t\t  |   |')
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+'\t\t'+inpboard[7]+' | '+inpboard[8]+' | '+inpboard[9])
    print(f'-----------            -----------      Choice of A = {choiceA}')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+'\t\t'+inpboard[4]+' | '+inpboard[5]+' | '+inpboard[6])
    print(f'-----------            -----------      Choice of B = {choiceB}')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+'\t\t'+inpboard[1]+' | '+inpboard[2]+' | '+inpboard[3])
    print('   |   |\t\t  |   |')

          
def winchk():
    global codes,A,B,result
    for i in codes:
        if(i in list(permutations(A,3))):
            ticboard()
            return('__Player A won the game__')

        elif(i in list(permutations(B,3))):
            ticboard()
            return('__Player B won the game__')
    if(' ' not in board):
        ticboard()
        return("Game Tied")
    else:
        return('None')

randominpt()