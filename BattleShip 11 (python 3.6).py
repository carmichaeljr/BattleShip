from random import randint
from time import sleep

board=[]
WORD="\t\t~~BATTLESHIP~~"

for letter in WORD:
   print(letter,end="")
   sleep(0.3)
print("\n\t_____________________________")
#print "Let's play Battleship!\n"
#sleep(0.5)
print("  You will be playing against the computer!",)
sleep(0.5)
print(\
"""
   __0__1__2__3__4_|~|_5__6__7__8__9_
   0|:_::_::_:_0_:_| |_::_::_::_::_:
   1|:_:_: -H-:_::_| |_:_0_:_:*S1:_:
   2|:_::_::_:_0_:_| |_:_0_:_:*S1:_:
   3|~S~~S~:_::_::_| -H-*S2:_::_::_:
   4|:_::_::_::_::_| |_::_::_::_:_0_
   '''----[Computer}~{Player]----'''
""",)

sleep(0.5)
input("\n\t  Press enter to play!")

loop12=True
while loop12:
   print(\
"""
________________How to play_________________
~First place your ships on your ocean grid.
~Your ships cannot be diagonal.
~Your ships are two units long, and you have 
   two of them
~Your ships cannot be on top of one another. 

______________________________________________
[```Type in "ESC" to skip the instructions```]
""")
   sleep(0.3)
   user_input=input("\tPress enter to continue.").upper()
   if  user_input=="ESC":
       loop12=False
       continue

   print(\
"""
________________How to play_________________
~You and your opponent will take turns, 
   calling out one shot per turn, trying to 
   hit each others ships.
~Once all of the coordinates on the ship have
   been hit, the ship is sunk.
~Your goal is to sink the computers ships
   before the computer sinks yours.
______________________________________________
[```Type in "ESC" to skip the instructions```]
""")
   sleep(0.3)
   user_input=input("\tPress enter to continue.").upper()
   if  user_input=="ESC":
       loop12=False
       continue
   
   print(\
"""
____________________Key_____________________
"-H-" =Hit              __0__1__2__3__4_
"~S~" =Sunk            0|:_::_::_:_0_:_|  
"_0_" =Miss            1|_0_:_:-H-:_::_|  
"{@}" & "[@]" =        2|:_::_::_:_0_:_|
 Where the ships were  3|~S~~S~:_::_::_|   
"*S1" & "*S2" =        4|:_::_::_::_::_| 
 Where your ships are      
____________________________________________
[+=+=+=+=```Press enter to play```=+=+=+=+=]
""")
   sleep(0.3)
   input("\tPress enter to play.")
   loop12=False

#defines functions that eilol be used latter on
def is_user_ship_col(x):
   user_input=True
   while user_input:
       if x=="5" or x=="6" or x=="7" or x=="8" or x=="9":
           user_input=False
           return int(x)
       else:
           print_board(board)
           if x=="":
               sleep(0.5)
               print("You did not enter anything. Please enter col again:")
               x=input("-->")
           else:
               sleep(0.5)
               print("Invalid input.Make sure your ship is on your baord. Please enter col again:")
               x=input("-->")
           
def is_user_ship_row(y):
   user_input=True
   while user_input:
       if y=="0" or y=="1" or y=="2" or y=="3" or y=="4":
           user_input=False
           return int(y)
       else:
           print_board(board)
           if y=="":
               sleep(0.5)
               print("You did not enter anything. Please enter row again.")
               y=input("-->")
           else:
               sleep(0.5)
               print("Invalid input.Make sure your ship is on your baord. Please enter row again:")
               y=input("-->")

def greater_than_4(z, col_or_row):
   user_input=True
   while user_input:
       if z=="0" or z=="1" or z=="2" or z=="3" or z=="4":
           return int(z)
           user_input=False
       else:
           print_board(board)
           if z=="":
               sleep(0.5)
               print("You did not enter anything. Please enter ",col_or_row,"again.")
               z=raw_input("-->")
           else:
               sleep(0.5)
               print("Invalid input.Make sure you are guessing on the computers board.\n Please enter",col_or_row,"again.")
               z=input("-->")
       

def print_results(user_ship_status, comp_ship_status, user_guess, comp_guess):
   print_user_guess=[]
   print_comp_guess=[]
   print_user_guess.append(user_guess[1])
   print_user_guess.append(user_guess[0])
   print_comp_guess.append(comp_guess[1])
   print_comp_guess.append(comp_guess[0])
   
   print("__________|_Guessed:___|____Status:___")
   print("You;      |",print_user_guess,"    |",comp_ship_status)
   print("Computer; |",print_comp_guess,"    |",user_ship_status)

for x in range(5):
   board.append(["{_}",] * 10)
   for row in board:
       row[0]="[_-"
       row[1]="-_-"
       row[2]="-_-"
       row[3]="-_-"
       row[4]="-_]"
       row[5]="[_}"
       row[9]="{_]"
   
def print_board(board):
   counter=0
   print(" _0___1___2___3___4_|_5___6___7___8___9_")
   for row in board:
       print(counter,end="")
       print(" ".join(row))
       counter+=1
   sleep(0.2)
   print("'''------[Computer}~{Player]--------'''")

#print_board(board)

#defines the first ships first coordinate
comp_ship1_coordinate1_row=randint(0,4)
comp_ship1_coordinate1_col=randint(0,4)
comp_ship1_coordinate1=[comp_ship1_coordinate1_row, comp_ship1_coordinate1_col]

#defines the first ships second coordinate
loop1=True
while loop1:
   pick_direction=randint(0,3)
   if pick_direction==0:
       comp_ship1_coordinate2_row=comp_ship1_coordinate1_row+1
       comp_ship1_coordinate2_col=comp_ship1_coordinate1_col
   elif pick_direction==1:
       comp_ship1_coordinate2_row=comp_ship1_coordinate1_row-1
       comp_ship1_coordinate2_col=comp_ship1_coordinate1_col
   elif pick_direction==2:
       comp_ship1_coordinate2_row=comp_ship1_coordinate1_row
       comp_ship1_coordinate2_col=comp_ship1_coordinate1_col+1
   else:
       comp_ship1_coordinate2_row=comp_ship1_coordinate1_row
       comp_ship1_coordinate2_col=comp_ship1_coordinate1_col-1
   
   if (comp_ship1_coordinate2_row>4 or comp_ship1_coordinate2_row<0) or\
   (comp_ship1_coordinate2_col>4 or comp_ship1_coordinate2_col<0):
       loop1=True
   else:
       comp_ship1_coordinate2=[comp_ship1_coordinate2_row,comp_ship1_coordinate2_col]
       loop1=False
       

#defines the second ships first coordinate
loop2=True
while loop2:
   comp_ship2_coordinate1_row=randint(0,4)
   comp_ship2_coordinate1_col=randint(0,4)
   comp_ship2_coordinate1=[comp_ship2_coordinate1_row, comp_ship2_coordinate1_col]
   if (comp_ship2_coordinate1==comp_ship1_coordinate1) or \
   (comp_ship2_coordinate1==comp_ship1_coordinate2):
       loop2=True
   else:
       loop2=False
       
#defines the second ships second coordinate
loop3=True
while loop3:
   pick_direction=randint(0,3)
   if pick_direction==0:
       comp_ship2_coordinate2_row=comp_ship2_coordinate1_row+1
       comp_ship2_coordinate2_col=comp_ship2_coordinate1_col
   elif pick_direction==1:
       comp_ship2_coordinate2_row=comp_ship2_coordinate1_row-1
       comp_ship2_coordinate2_col=comp_ship2_coordinate1_col
   elif pick_direction==2:
       comp_ship2_coordinate2_row=comp_ship2_coordinate1_row
       comp_ship2_coordinate2_col=comp_ship2_coordinate1_col+1
   else:
       comp_ship2_coordinate2_row=comp_ship2_coordinate1_row-1
       comp_ship2_coordinate2_col=comp_ship2_coordinate1_col
   if (comp_ship2_coordinate2_row>4 or comp_ship2_coordinate2_row <0) or (comp_ship2_coordinate2_col>4 or comp_ship2_coordinate2_col <0):
       loop3=True
   else:
       comp_ship2_coordinate2=[comp_ship2_coordinate2_row,comp_ship2_coordinate2_col]
       if (comp_ship2_coordinate2==comp_ship1_coordinate1) or (comp_ship2_coordinate2==comp_ship1_coordinate2):
           loop3=True
       else:
           loop3=False

     
#board[comp_ship1_coordinate1_row][comp_ship1_coordinate1_col]="*s1"
#board[comp_ship1_coordinate2_row][comp_ship1_coordinate2_col]="*s1"
#board[comp_ship2_coordinate1_row][comp_ship2_coordinate1_col]="*s2"
#board[comp_ship2_coordinate2_row][comp_ship2_coordinate2_col]="*s2"
print_board(board)

#defines the first ships first coordinate
print("Lets play!")
print("Enter your first ships first coordinate.")
sleep(1)
user_ship1_coordinate1_col=is_user_ship_col(input("Enter Col->"))
user_ship1_coordinate1_row=is_user_ship_row(input("Enter Row->"))

user_ship1_coordinate1=[user_ship1_coordinate1_row,user_ship1_coordinate1_col]
board[user_ship1_coordinate1_row][user_ship1_coordinate1_col]="*s1"


#defines the first ships second coordinate
loop4=True
on_board=False
while loop4:
   if on_board==True:
       print_board(board)
       sleep(0.5)
       print("Invalid input. Make sure your ship is on your board.")
   else:
       print_board(board)
       print("Now pick your ships direction.\n Up,Down,Left,or Right")
       sleep(1)
   user_pick_direction=input("R,L,U,D->").upper()

   if user_pick_direction=="U" or user_pick_direction=="UP":
       user_ship1_coordinate2_row=user_ship1_coordinate1_row-1
       user_ship1_coordinate2_col=user_ship1_coordinate1_col
   elif user_pick_direction=="D" or user_pick_direction=="DOWN":
       user_ship1_coordinate2_row=user_ship1_coordinate1_row+1
       user_ship1_coordinate2_col=user_ship1_coordinate1_col
   elif user_pick_direction=="R" or user_pick_direction=="RIGHT":
       user_ship1_coordinate2_row=user_ship1_coordinate1_row
       user_ship1_coordinate2_col=user_ship1_coordinate1_col+1
   elif user_pick_direction=="L" or user_pick_direction=="LEFT":
       user_ship1_coordinate2_row=user_ship1_coordinate1_row
       user_ship1_coordinate2_col=user_ship1_coordinate1_col-1
   else:
       on_board=True
       continue
   if (user_ship1_coordinate2_row>4 or user_ship1_coordinate2_row<0) or (user_ship1_coordinate2_col>9 or user_ship1_coordinate2_col<5):
       on_board=True
       continue
   else:
       loop4=False
       user_ship1_coordinate2=[user_ship1_coordinate2_row,user_ship1_coordinate2_col]
       board[user_ship1_coordinate2_row][user_ship1_coordinate2_col]="*s1"
   loop4=False

#print_board(board)

#defines  the second ships first coordinate
loop5=True
on_board=False
while loop5:
   print_board(board)
   if on_board==True:
       sleep(0.5)
       print("Invalid input. Make sure your ship is on your board. \nYour ships cannot be on top of one another.")
   else:
       print("Now pick your second ships first coordinate.")
       sleep(1)
   sleep(0.5)
   user_ship2_coordinate1_col=is_user_ship_col(input("Enter Col->"))
   user_ship2_coordinate1_row=is_user_ship_row(input("Enter Row->"))
   user_ship2_coordinate1=[user_ship2_coordinate1_row, user_ship2_coordinate1_col]
   if user_ship2_coordinate1==user_ship1_coordinate1 or user_ship2_coordinate1==user_ship1_coordinate2:
       print_board(board)
       on_board=True
   else:
       board[user_ship2_coordinate1_row][user_ship2_coordinate1_col]="*s2"
       loop5=False
   
#defines the second ships second coordinate
loop6=True
on_board=False
while loop6:
   if on_board==True:
       print_board(board)
       sleep(0.5)
       print("Invalid input. Make sure your ship is on your board. Your ships cannot be on top of one another.")
   else:
       print_board(board)
       print("Now pick your ships direction.\n Up,Down,Left,or Right")
       sleep(1)
   user_pick_direction=input("R,L,U,D->").upper()

   if user_pick_direction=="U" or user_pick_direction=="UP":
       user_ship2_coordinate2_row=user_ship2_coordinate1_row-1
       user_ship2_coordinate2_col=user_ship2_coordinate1_col
   elif user_pick_direction=="D" or user_pick_direction=="DOWN":
       user_ship2_coordinate2_row=user_ship2_coordinate1_row+1
       user_ship2_coordinate2_col=user_ship2_coordinate1_col
   elif user_pick_direction=="R" or user_pick_direction=="RIGHT":
       user_ship2_coordinate2_row=user_ship2_coordinate1_row
       user_ship2_coordinate2_col=user_ship2_coordinate1_col+1
   elif user_pick_direction=="L" or user_pick_direction=="LEFT":
       user_ship2_coordinate2_row=user_ship2_coordinate1_row
       user_ship2_coordinate2_col=user_ship2_coordinate1_col-1
   else:
       on_board=True
       continue
   if (user_ship2_coordinate2_row>4 or user_ship2_coordinate2_row<0) or (user_ship2_coordinate2_col>9 or user_ship2_coordinate2_col<5):
       on_board=True
       continue
   else:
       user_ship2_coordinate2=[user_ship2_coordinate2_row,user_ship2_coordinate2_col]
       if (user_ship2_coordinate2==user_ship1_coordinate1) or (user_ship2_coordinate2==user_ship1_coordinate2):
           on_board=True
           continue
       else:
           loop6=False
           board[user_ship2_coordinate2_row][user_ship2_coordinate2_col]="*s2"


#print_board(board)
print( \
"""
```````````````````````````````````````````````
       _
 _____| |___          Sploosh!!! 
 \ 0   0  0/          _\/_
~~\_______/~~\```\~~~~/ |\~~~~~~~
                    \~~~~\  MISS! (Hah hah...)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
""")
#finds out if the user wants to go first
loop7=True
sleep(0.5)
start_turn=input("\nDo you want to go first(If you dare...)y/n->").upper()
while loop7:
   if start_turn=="Y" or start_turn=="YES":
       sleep(0.5)
       print("Alrighty then....have it your way!")
       person_start=True
       loop7=False
   elif start_turn=="N" or start_turn=="NO":
       sleep(0.5)
       print("Well then...have fun!")
       loop7=False
   else:
       sleep(0.5)
       start_turn=input("What was that? y/n:").upper()
#print_board(board)


#the big turn loop
comp_ship1_coordinate1_hit=False
comp_ship1_coordinate2_hit=False
comp_ship2_coordinate1_hit=False
comp_ship2_coordinate2_hit=False
comp_ship1_sunk=False
comp_ship2_sunk=False
first_turn=True
user_ship1_coordinate1_hit=False
user_ship1_coordinate2_hit=False
user_ship2_coordinate1_hit=False
user_ship2_coordinate2_hit=False
user_ship1_sunk=False
user_ship2_sunk=False
comp_miss=0
user_miss=0
comp_ship_status="--"
user_ship_status="--"
comp_guess=[0,0]
user_guess=[0,0]

turn_loop=True
while turn_loop:
   if first_turn==True:
       print_board(board)
       first_turn=False
   #the users guessing system
   if start_turn=="Y" or start_turn=="YES":
       start_turn="N"
       print("Enter your guess.")
       user_guess_col=greater_than_4(input("Enter Col->"),"Col")
       user_guess_row=greater_than_4(input("Enter Row->"),"Row")
       user_guess=[user_guess_row, user_guess_col]
       
       loop8=True
       while loop8:
           if board[user_guess_row][user_guess_col]=="_0_" or board[user_guess_row][user_guess_col]=="-H-" or board[user_guess_row][user_guess_col]=="~S~":
               print_board(board)
               print("Oops, you already guessed there.")
               user_guess_col=is_user_ship_row(input("Enter Col->"))
               user_guess_row=is_user_ship_row(input("Enter Row->"))
               user_guess=[user_guess_row, user_guess_col]
           else:
               loop8=False
               
       if user_guess==comp_ship1_coordinate1:
           board[user_guess_row][user_guess_col]="-H-"
           comp_ship_status="HIT!"
           comp_ship1_coordinate1_hit=True
       elif user_guess==comp_ship1_coordinate2:
           board[user_guess_row][user_guess_col]="-H-"
           comp_ship_status="HIT!"
           comp_ship1_coordinate2_hit=True
       elif user_guess==comp_ship2_coordinate1:
           board[user_guess_row][user_guess_col]="-H-"
           comp_ship_status="HIT!"
           comp_ship2_coordinate1_hit=True
       elif user_guess==comp_ship2_coordinate2:
           board[user_guess_row][user_guess_col]="-H-"
           comp_ship_status="HIT!"
           comp_ship2_coordinate2_hit=True
       else:
           board[user_guess_row][user_guess_col]="_0_"
           comp_ship_status="Missed!"
           user_miss+=1
           
       if comp_ship1_coordinate1_hit==True and comp_ship1_coordinate2_hit==True:
           board[comp_ship1_coordinate1_row][comp_ship1_coordinate1_col]="~S~"
           board[comp_ship1_coordinate2_row][comp_ship1_coordinate2_col]="~S~"
           comp_ship_status="SUNK!"
           comp_ship1_coordinate1_hit=False
           comp_ship1_coordinate2_hit=False
           comp_ship1_sunk=True
       elif comp_ship2_coordinate1_hit==True and comp_ship2_coordinate2_hit==True:
           board[comp_ship2_coordinate1_row][comp_ship2_coordinate1_col]="~S~"
           board[comp_ship2_coordinate2_row][comp_ship2_coordinate2_col]="~S~"
           comp_ship_status="SUNK!"
           comp_ship2_coordinate1_hit=False
           comp_ship2_coordinate2_hit=False
           comp_ship2_sunk=True
           
       print_board(board)
           
       if comp_ship1_sunk==True and comp_ship2_sunk==True:
           print(\
"""
 __    ___   ________    ___   ___
 \ \  /  /  /  ____  \  |   | |   |
  \ \/ /   |  /    \  | |   | |   |
   |  |    |  \____/  | |   |~|   |
   |__|     \________/  \_________/
__    __   _______   __    __     !
|  |__|  | |___  __| |  \  |  !   !
|        |     ||    |   \ |  !   o
|   /\   |  ___||__  |    \|  !  O O
|__/  \__| |_______| |__|\____!   O       
""")
           comp_user_won=True
           turn_loop=False
       
   else:
       #the computers guessing system
       start_turn="Y"
       guess_around_hit=randint(0,3)
       
       
       #Picks the coordinate that it will guess 
       #if ship one is hit, guess around it
       if (user_ship1_coordinate1_hit==True or user_ship1_coordinate2_hit==True) and user_ship1_sunk!=True:
           loop9=True
           while loop9:
               if guess_around_hit==0:
                   comp_guess_row=comp_old_guess_row+1
                   comp_guess_col=comp_old_guess_col
                   guess_around_hit=1
               elif guess_around_hit==1:
                   comp_guess_row=comp_old_guess_row-1
                   comp_guess_col=comp_old_guess_col
                   guess_around_hit=2
               elif guess_around_hit==2:
                   comp_guess_row=comp_old_guess_row
                   comp_guess_col=comp_old_guess_col+1
                   guess_around_hit=3
               elif guess_around_hit==3:
                   comp_guess_row=comp_old_guess_row
                   comp_guess_col=comp_old_guess_col-1
                   guess_around_hit=0
               if ((comp_guess_row<0 or comp_guess_row>4) or (comp_guess_col<5 or comp_guess_col>9)) or ( board[comp_guess_row][comp_guess_col]=="_0_" or  board[comp_guess_row][comp_guess_col]=="-H-" or board[comp_guess_row][comp_guess_col]=="~S~"):
                   loop9=True
               else:
                   comp_guess=[comp_guess_row, comp_guess_col]
                   loop9=False
       
       
       #if ship 2 is hit, guess around it 
       elif (user_ship2_coordinate1_hit==True or user_ship2_coordinate2_hit==True) and user_ship2_sunk!=True:
           loop11=True
           while loop11:
               if guess_around_hit==0:
                   comp_guess_row=comp_old_guess_row+1
                   comp_guess_col=comp_old_guess_col
                   guess_around_hit=1
               elif guess_around_hit==1:
                   comp_guess_row=comp_old_guess_row-1
                   comp_guess_col=comp_old_guess_col
                   guess_around_hit=2
               elif guess_around_hit==2:
                   comp_guess_row=comp_old_guess_row
                   comp_guess_col=comp_old_guess_col+1
                   guess_around_hit=3
               elif guess_around_hit==3:
                   comp_guess_row=comp_old_guess_row
                   comp_guess_col=comp_old_guess_col-1
                   guess_around_hit=0
               if ((comp_guess_row<0 or comp_guess_row>4) or (comp_guess_col<5 or comp_guess_col>9)) or ( board[comp_guess_row][comp_guess_col]=="_0_" or  board[comp_guess_row][comp_guess_col]=="-H-" or board[comp_guess_row][comp_guess_col]=="~S~"):
                   loop11=True
               else:
                   comp_guess=[comp_guess_row, comp_guess_col]
                   loop11=False
                   
                   
       #if no ship is hit guess randomly         
       else:
           loop10=True
           while loop10:
               comp_guess_row=randint(0,4)
               comp_guess_col=randint(5,9)
               comp_guess=[comp_guess_row, comp_guess_col]
               if board[comp_guess_row][comp_guess_col]=="_0_" or  board[comp_guess_row][comp_guess_col]=="-H-" or board[comp_guess_row][comp_guess_col]=="~S~":
                   loop10=True
               else:
                   loop10=False
                   
                   
                   
                   
       #checks to see if the computer hit a ship and such
       
       if comp_guess==user_ship1_coordinate1:
           user_ship1_coordinate1_hit=True
           comp_old_guess_row=comp_guess_row
           comp_old_guess_col=comp_guess_col
           if comp_guess_col==5:
               board[user_ship1_coordinate1_row][user_ship1_coordinate1_col]="[H-"
           else:
               board[user_ship1_coordinate1_row][user_ship1_coordinate1_col]="-H-"
           print_board(board)
           user_ship_status="HIT!"
       elif comp_guess==user_ship1_coordinate2:
           user_ship1_coordinate2_hit=True
           comp_old_guess_row=comp_guess_row
           comp_old_guess_col=comp_guess_col
           board[user_ship1_coordinate2_row][user_ship1_coordinate2_col]="-H-"
           print_board(board)
           user_ship_status="HIT!"
       elif comp_guess==user_ship2_coordinate1:
           user_ship2_coordinate1_hit=True
           comp_old_guess_row=comp_guess_row
           comp_old_guess_col=comp_guess_col
           board[user_ship2_coordinate1_row][user_ship2_coordinate1_col]="-H-"
           print_board(board)
           user_ship_status="HIT!"
       elif comp_guess==user_ship2_coordinate2:
           user_ship2_coordinate2_hit=True
           comp_old_guess_row=comp_guess_row
           comp_old_guess_col=comp_guess_col
           board[user_ship2_coordinate2_row][user_ship2_coordinate2_col]="-H-"
           print_board(board)
           user_ship_status="HIT!"
       else:
           board[comp_guess_row][comp_guess_col]="_0_"
           print_board(board)
           user_ship_status="Missed!"
           comp_miss+=1
       if user_ship1_coordinate1_hit==True and user_ship1_coordinate2_hit==True:
           user_ship1_coordinate1_hit=False
           user_ship1_coordinate2_hit=False
           user_ship1_sunk=True
           board[user_ship1_coordinate1_row][user_ship1_coordinate1_col]="~S~"
           board[user_ship1_coordinate2_row][user_ship1_coordinate2_col]="~S~"
           print_board(board)
           user_ship_status="SUNK!"
       elif user_ship2_coordinate1_hit==True and user_ship2_coordinate2_hit==True:
           user_ship2_coordinate1_hit=False
           user_ship2_coordinate2_hit=False
           user_ship2_sunk=True
           board[user_ship2_coordinate1_row][user_ship2_coordinate1_col]="~S~"
           board[user_ship2_coordinate2_row][user_ship2_coordinate2_col]="~S~"
           print_board(board)
           user_ship_status="SUNK!"
            
           
       if user_ship1_sunk==True and user_ship2_sunk==True:
           print(\
"""
   ________   ____      _____   ____      _____
  / ______/  /    |    /     | /    |    /  ___/
 / /        /  ]  |   /  /|  |/  /| |   /  /__
/ /    ___ /  /|  |  /  / |  /  / | |  /   __/
/ /___/  //  / |  | /  /  |____/  | | /   /_
\_______//__/  |__|/__/           |_|/_____/
 ________   ___    __  _____  _____   ?-?
/  ____  \  \  \/  /  | |__  |  O  |    \?
|  /    \ |  \    /   |  __| |    /    ?/
|  \____/ |   \  /    | |__  |  |  \   |
\________/     \/     |____| |__|__|   o
""")
           comp_user_won=False
           turn_loop=False
           continue
           
           
   #Prints the results of the last round in a table

       print_results(user_ship_status, comp_ship_status, user_guess, comp_guess)       
       


#At the end of the game, it will print the number of hits, misses and such

input("Press enter to see the results.")
if user_ship1_sunk!=True:
   board[user_ship1_coordinate1_row][user_ship1_coordinate1_col]="{@}"
   board[user_ship1_coordinate2_row][user_ship1_coordinate2_col]="{@}"
if user_ship2_sunk!=True:
   board[user_ship2_coordinate1_row][user_ship2_coordinate1_col]="{@}"
   board[user_ship2_coordinate2_row][user_ship2_coordinate2_col]="{@}"

if comp_ship1_sunk!=True:        
   board[comp_ship1_coordinate1_row][comp_ship1_coordinate1_col]="[@]"
   board[comp_ship1_coordinate2_row][comp_ship1_coordinate2_col]="[@]"
if comp_ship2_sunk!=True:
   board[comp_ship2_coordinate1_row][comp_ship2_coordinate1_col]="[@]"
   board[comp_ship2_coordinate2_row][comp_ship2_coordinate2_col]="[@]"
   

user_sunk_ships=0
comp_sunk_ships=0
user_hit_ships=0
comp_hit_ships=0

   
#checks for sunk ships
if comp_ship1_sunk==True:
   user_sunk_ships+=1
   user_hit_ships+=2
if comp_ship2_sunk==True:
   user_sunk_ships+=1
   user_hit_ships+=2
if user_ship1_sunk==True:
   comp_sunk_ships+=1
   comp_hit_ships+=2
if user_ship2_sunk==True:
   comp_sunk_ships+=1
   comp_hit_ships+=2

#checks for hit ships
if comp_ship1_coordinate1_hit==True and comp_ship1_sunk!=True:
   user_hit_ships+=1
if comp_ship1_coordinate2_hit==True and comp_ship1_sunk!=True:
   user_hit_ships+=1
if comp_ship2_coordinate1_hit==True and comp_ship1_sunk!=True:
   user_hit_ships+=1
if comp_ship2_coordinate2_hit==True and comp_ship1_sunk!=True:
   user_hit_ships+=1
if user_ship1_coordinate1_hit==True and user_ship1_sunk!=True:
   comp_hit_ships+=1
if user_ship1_coordinate2_hit==True and user_ship1_sunk!=True:
   comp_hit_ships+=1
if user_ship2_coordinate1_hit==True and user_ship1_sunk!=True:
   comp_hit_ships+=1
if user_ship2_coordinate2_hit==True and user_ship1_sunk!=True:
   comp_hit_ships+=1
   
if comp_user_won==True:
   user_won="WON!"
   comp_won="Lost."
else:
   user_won="Lost."
   comp_won="WON!"
   

print_board(board)
print("______________________Results______________________")
print("You      || Sunk:",user_sunk_ships,"|Hit: ",user_hit_ships,"|Missed: ",user_miss,"|Overall: ",user_won)
print("-------------------------------------------")
print("Computer || Sunk:",comp_sunk_ships,"|Hit: ",comp_hit_ships, "|Missed: ",comp_miss,"|Overall: ",comp_won)


