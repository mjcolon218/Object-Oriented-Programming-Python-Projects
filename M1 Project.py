#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Maurice J Colon
#Milestone Project 1 
#6/30/19
import random
from IPython.display import clear_output # Using the Module from Ipython fir clearoutput Method

def display_Board(board):# Creating the Function Display Board to set up the display for the game //Using indexing for slots
    clear_output()
    print ('  ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print ('----------')
    print ('  ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print ('----------')
    print ('  ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    


# In[2]:


test_Board = ['#','','','','','','','','','']#Creating Testboard to see if Im making progress!
#display_Board(test_Board)Testing my Board


# In[3]:


def player_Choose():#Creating function to decide if player 1 wants to be X or O 
    marker = ''# marker is set to Empty string
    while not (marker =='X'or marker == 'O'):#Gonna keep prompting until you enter X or O
        marker = (input("X or O?:Pick Wisely...")).upper()#Prompting user for input while using upper method
    if marker == 'X':# little bit of Logic to keep things organized 
        return('X','O')
    else:
        return('O','X')
    
#player_Choose()Testing Function 


# In[4]:


def place_marker(board,marker,position):#making function to add a marker on a position according to index by passing variables 
    board[position] = marker  #.....Through the paramaters.
    
#place_marker(test_Board,'X',3)#Placing markers to check if the function is working. 
#place_marker(test_Board,'X',2)
#place_marker(test_Board,'X',1)
def win_Check(board,mark):# Returning Boolean to check if someone Won Vertical, Horizontal, or Diagonal.
    return((board[1] == mark and board[2] == mark and board[3] == mark)or # Across Row 1
           (board[4] == mark and board[5] == mark and board[6] == mark)or # Across Row 2
            (board[7] == mark and board[8] == mark and board[9] == mark)or # Across Row 3
           (board[1] == mark and board[4] == mark and board[7] == mark)or # Down Column 1 
           (board[2] == mark and board[5] == mark and board[8] == mark)or # Down Column 2 
           (board[3] == mark and board[6] == mark and board[9] == mark)or # Down Column 3
           (board[7] == mark and board[5] == mark and board[3] == mark))  # Diagonally Cross


def choose_First():#Created function and used random module to get random integers to decide whos goes first SHoot ur DICE!
    if random.randint(0,1)==0:#if the random number is equivalent to 0 then print statements triggers with return 'String'
        print(""""""'Player 2 Goes First!'"""""")
        print('Your Turn.....')
        return 'Player 2'
    
    else:#More logic almost like an inverse function one would say just the opposite
        print(""""""'Player 1 Goes First!'"""""")
        print('Your Turn.....')
        return 'Player 1'
    
def empty_check(board,position):# Creating a function that returns bool according to if the index[p]  has empty string 
    return board[position] == ''# Returns True bool if the board[position] is empty or equal to a empty String

 #empty_check(test_Board,7) Checking if function is working 

def check_Fullboard(board):# creating function using for loops in range of 10 while using emptyCheck function to determine if
    for i in range(1,10): # Board is full , the range 1-10 reps 1-9 on the board indexs that where using the empty_check on 
        if empty_check(board,i):
            return False
    return True
#check_Fullboard(test_Board)Testing Function as always    

def player_Choice(board):#Creating function for playerChoice
    # setting variable to integer 0 to keep track 
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not empty_check(board,position):#while 0 is not in the list[1-9]or
        #the board is filled in that position
        position = int(input('Whats your next MOVE:1-9'))
    
    return position # returning position because if I dont I wont be able to pass it through another function
#player_Choice(test_Board)Testing Function also


def replay():#Simple function prompting for an input then using methods to make sure it meets certain criteria
    return input ('would you like to play again ?:Yes or No').lower().startswith('y')

#replay()running tests on my functions making sure work 
 


# In[5]:


#choose_First() Just me testing my code out along the way 


# In[6]:


#display_Board(test_Board)More tests


# In[7]:


#win_Check(test_Board,'X')More tests


# In[8]:


print ('*****WELCOME TO TIC TAC TOE*****')

while True:#While we playing this game the board starts out 3x3 with empty strings in the 9 indices positions
    theBoard = ['']*10
    
    player_1marker,player_2marker = player_Choose()#setting 2 variables to the function playerchoose that returns list w 2 characters
    #for each variable ...player_1marker and player_2marker
    turn = choose_First()#more variable setting to functions 
    play_game = input('are you ready to play now : Enter Yes or NO').lower()# Prompting user this time for input 
    
    if play_game.lower()== 'y':#some Logic with that variable to set Game on to a BOOL True or False
        game_on = True
    else:
        game_on = False
        
    while game_on:#While game on is true or player types in yes or YES and its player 1 turn
        if turn == 'Player 1':
            display_Board(theBoard)#Display the board
            print('players 1 go')#Prints whos turn it is 
            position = player_Choice(theBoard)#setting the position the player chooses to move to and return it 
            place_marker(theBoard,player_1marker,position)#placeing the marker from player on the board according to position
            
            if win_Check(theBoard,player_1marker):#Were checking if player1 markers are returnong true up down or diagonally
                display_Board(theBoard)#display board
                print('Congrulations You have Won the Game !')#printing you won if wincheck returns True
                game_on = False # after the print statement the game_on Bool is set to false to end the game 
            else:#If win_check is false we move to this else statement to check if the board is full and if so its a draw
                if check_Fullboard(theBoard):
                    display_Board(theBoard)#Display board
                    print('Sorry the Game is a DRAW')#prints the game is a draw then breaks to end game 
                    break
                else:# if win_check and check_fullboard both returns False meaning u aint win and it aint a draw then
                    # we prints player 2 your turn then turn changes to Player 2 and we Execute the out most else statement
                    #which is essentially the same functions and methods that players 1 used to determing whether he won or 
                    # is it  a draw if neither then its the other players turn 
                    print('Player 2 Your Turn')
                    turn = 'Player 2'
                    
        else:#When those above inner else statements are not true for player one then its players 2 turns which is the most 
            #outter else statement that is executed ... thats why indentation counts for python!
            display_Board(theBoard)
            print('player 2 go')
            position = player_Choice(theBoard)
            place_marker(theBoard,player_2marker,position)
            
            if win_Check(theBoard,player_2marker,):
                display_Board(theBoard)
                
                print('Congratulation You have Won the Game !')
                game_on = False
            else:
                if check_Fullboard(theBoard):
                    display_Board(theBoard)
                    print('Sorry the Game is a Draw')
                    break
                else:

                    turn = 'Player 1'
    if not replay():#if we not replaying the game the continuous bool true is or game running is broken so it python wont keep 
        #executing the same code over and over 
        break
        


# In[ ]:





# In[ ]:




