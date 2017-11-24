#!/bin/python3

from random import randint

while 1:
  player = input('rock(r), paper(p), scisson(s)?')
  
  if player == 'E':
    print('Breaking program')
    break
  
  elif player != 'r' and player != 'p' and player != 's':
    print('Invalid Entry')
    print("")
    #break
    
   
  
  else:
    
    print(player, 'vs', end=' ')
    
    #computers turn
    
    chosen = randint(1,3)
    #print(chosen)
    
    if chosen == 1:
      computer = 'r'
    
    elif chosen == 2:
      computer = 'p'
      
    else:
      computer = 's'
      
    print(computer)
    
    if player == computer:
      print('*****DRAW*****')
      print("")
      
    elif player == 'r' and computer == 'p':
      print('*****You lose :\'(')
      print("")
      
    elif player == 'r' and computer == 's':
      print('*****You Win*****')
      print("")
    
    elif player == 'p' and computer == 'r':
      print('*****You Win*****')
      print("")
      
    elif player == 'p' and computer == 's':
      print('*****You lose :\'(')
      print("")
      
    elif player == 's' and computer == 'r':
      print('*****You lose :\'(')
      print("")
      
    elif player == 's' and computer == 'p':
      print('*****You Win*****')
      print("")
