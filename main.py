import os
import random
import time
from socket import setdefaulttimeout

def levelUp():
  global level
  global statPoints

  level = level + 1
  statPoints = statPoints + 5
  print('You are level', level)
def statPointAdd():
  global statPoints
  statPoints = statPoints + 10
  print('You now have', statPoints, 'stat points')
def roomTest():
  if int1 == 1: # This checks for the type of room, also known as seed number. It can be 0 - 9, and each number has its own room type
    print('This is a "Safe" room')
  
  if int1 == 2: # This checks for the type of room, also known as seed number. It can be 0 - 9, and each number has its own room type
    print('This is a "Treasure" room')
  
  if int1 == 3: # This checks for the type of room, also known as seed number. It can be 0 - 9, and each number has its own room type
    print('This is an  "Enemy" room')
  
  if int1 == 4: # This checks for the type of room, also known as seed number. It can be 0 - 9, and each number has its own room type
    print('This is an "Enemy" room')
  
  if int1 == 5: # This checks for the type of room, also known as seed number. It can be 0 - 9, and each number has its own room type
    print('This is a "Healing" room')
  
  if int1 == 6: # This checks for the type of room, also known as seed number. It can be 0 - 9, and each number has its own room type
    print('This is a "Puzzle" room')
  
  if int1 == 7: # This checks for the type of room, also known as seed number. It can be 0 - 9, and each number has its own room type
    print('This is a "Boss" room')
  
  if int1 == 8: # This checks for the type of room, also known as seed number. It can be 0 - 9, and each number has its own room type
    print('This is a "Puzzle" room')
  
  if int1 == 9: # This checks for the type of room, also known as seed number. It can be 0 - 9, and each number has its own room type
    print('This is an "Enemy" room')
  
  if int1 == 0: # This checks for the type of room, also known as seed number. It can be 0 - 9, and each number has its own room type
    print('This is a "Boss" room')
## TODO:
#  Make seed decoder algorithm - DONE
#  Make decoded outputs - DONE
#  Make "game"
#  Document and comment on code so I actualy know what I'm reading lol
def statCall():
  global healthTick
  global name
  global level
  global health
  global strength
  global defence
  global luck
  global statPoints
  statRepeat = 1
  while statRepeat == 1: # Keeps character screen open till finished
    print('\u001b[34m') # Just text
    print(name, '\u001b[32mLvl\u001b[0m:', level) # Just text
    print('===================') # Just text
    print('\u001b[31mHealth\u001b[0m:  ', health) # Just text
    print('\u001b[31mStr\u001b[0m:     ', strength) # Shows Strength Stat
    print('\u001b[36mDef\u001b[0m:     ', defence) # Shows Defence Stat
    print('\u001b[32mLuck\u001b[0m:    ', luck) # shows luck stat
    print('Stat Pts:\u001b[33m', statPoints, '\u001b[0m') # Shows how many stat points you have, and prompts you to use them
    print('===================')
    statChoice = input('\n\u001b[33mstats\u001b[0m>> ') # the "terminal"
  
    if statChoice == 'str': # Checks if the user types "str"
      print('How many points do you want to spend?') # Just text
      statAdd = input('\n\u001b[33mstats\u001b[0m>> ') # the "terminal"
      if int(statAdd) > int(statPoints): # if you have less stat points than you want to spend
        print("You don't have that many points!") # Just text
        time.sleep(0.5) # Waits 0.5 seconds
      elif int(statAdd) <= int(statPoints): # if you have more than or the same amount that you want to spend
        strength = int(strength) + int(statAdd) # Sets strength stat
        statPoints = int(statPoints) - int(statAdd) # removes stat points
      os.system('clear')

    if statChoice == 'def': # Checks if the user types "def"
      print('How many points do you want to spend?') # Just text
      statAdd = input('\n\u001b[33mstats\u001b[0m>> ') # the "terminal"
      if int(statAdd) > int(statPoints): # if you have less stat points than you want to spend
        print("You don't have that many points!") # Just text
        time.sleep(0.5) # Waits 0.5 seconds
      elif int(statAdd) <= int(statPoints): # if you have more than or the same amount that you want to spend
        defence = int(defence) + int(statAdd) # Sets Defence stat
        statPoints = int(statPoints) - int(statAdd) # removes stat points
      os.system('clear')
        
    if statChoice == 'luck': # Checks if the user types "luck"
      print('How many points do you want to spend?') # Just text
      statAdd = input('\n\u001b[33mstats\u001b[0m>> ') # the "terminal"
      if int(statAdd) > int(statPoints): # if you have less stat points than you want to spend
        print("You don't have that many points!") # Just text
        time.sleep(0.5) # Waits 0.5 seconds
      elif int(statAdd) <= int(statPoints): # if you have more than or the same amount that you want to spend
        luck = int(luck) + int(statAdd) # Sets Luck stat
        statPoints = int(statPoints) - int(statAdd)# removes stat points
      os.system('clear')
        
    if statChoice == 'end':
      statRepeat = 0

name = '[null]'
terminalRepeat = 1 # The repeat variable
statRepeat = 1 # The repeat variable
level = 0
health = 60
strength = 0 # Base Strength Stat
defence = 0 # Base Defence Stat
luck = 0 # Base Luck Stat
statPoints = 20 # Base Stat Points
x = 0
seedChoose = 0 # a boolian statment asking if the user wants to choose their seed (This is just for initalization)
seedBit = 0 # amount of time the decoder will repeat (This is just for initalization)
roomBreakDown = list()
roomList = list() # the encoded room data

maxRoom = 1500 # Max amount of rooms you can choose to spawn
minRoom = 1  # Min amount of rooms you can choose to spawn

roomBitCount = 0 # (This is just for initalization)
roomRoll = random.randint(1,3) # The roll chance for room type (This is just for initalization)
seedChooseTest = input('Do you want to use a custom seed? y or n: ')
if seedChooseTest == 'y': # Checks if the user typed 'y'
  seedChoose = 1 # Sets seedChoose to 1

elif seedChooseTest == 'n': # Checks if the user typed 'n'
  seedChoose = 0 # Sets seedChoose to 0
else:
  print('\u001b[31m\n**That was not yes or no!**\n\u001b[0mAuto setting to random seed.\n')

if seedChoose == 0: # Checks if user wants to pick a seed
  seedBit = int(input('How many rooms? ')) # How large the seed is

  if seedBit > maxRoom: # If the number of rooms you choose is higher than the max, it sets it to the max

    print(seedBit, 'is bigger than the maximum rooms') # Tells the user that the number it too big
    seedBit = maxRoom # sets the number of rooms to the max room numeber
    time.sleep(1)

  if seedBit < minRoom: # If the number of rooms you choose is lower than the min, it sets it to the min
    print(seedBit, 'is less than minimum rooms') # Tells the user that the number it too small
    seedBit = minRoom # sets the number of rooms to the min room number

## TODO:
#  Make seed decoder algorithem
#  Make decoded outputs
#  Make "game"
#  Document and comment on code so I actualy know what im reading lol
if seedChoose ==1: # Checks if user wants to pick a seed
  seedOutput = list(str(input('Enter Seed: ')))
  
  for items in list(seedOutput): # Repeats for every item in the custom seed, AKA every number
    seedBit = seedBit + 1 # Adds one point to the bit (for the decoder)
  

if seedChoose == 0: # Checks if user wants to pick a seed
  seedOutput = list(str(1)) # Start of list, list always has '1' as starting item
  print('\u001b[33m**Creating Seed**\n')
  for bit in range(seedBit): # how the 5-bit seed is generated
    
    seed = random.randint(0,9) # Generates a random int that is 0 - 9
    seedOutput.append(str(seed)) # Adds the random int that we previusly made into the seed-list
print(str(seedOutput))
print('\u001b[32m**Decoding seed**')

## THIS IS THE SEED DECODER
for bit in range(seedBit): # Repeats for every "bit" in the seed (every item)
  
  seedNum = int(seedOutput[0]) # sets variable seedNum to the first item in the list 

  if seedNum == 1: # rolles for room type when a number in seed is 1
    roomRoll = random.randint(1,3)

  if seedNum == 2: # rolles for room type when a number in seed is 2
    roomRoll = random.randint(1,3)

  if seedNum == 3: # rolles for room type when a number in seed is 3
    roomRoll = random.randint(1,3)

  if seedNum == 4: # rolles for room type when a number in seed is 4
    roomRoll = random.randint(1,3)

  if seedNum == 5: # rolles for room type when a number in seed is 5
    roomRoll = random.randint(1,3)

  if seedNum == 6: # rolles for room type when a number in seed is 6
    roomRoll = random.randint(1,3)

  if seedNum == 7: # rolles for room type when a number in seed is 7
    roomRoll = random.randint(1,3)

  if seedNum == 8: # rolles for room type when a number in seed is 8
    roomRoll = random.randint(1,3)

  if seedNum == 9: # rolles for room type when a number in seed is 9
    roomRoll = random.randint(1,3)

  if seedNum == 0: # rolles for room type when a number in seed is 0
    roomRoll = random.randint(1,3)

  seedOutput.pop(0) # Removes the first item in the seedOutput list
  if roomBitCount > 8:
    roomBitCount = 0
  roomBitCount = roomBitCount + 1 # Each iteration adds one to bit count

## THIS IS THE ROOM ENCODER
  roomData = str(seedNum) + str(roomRoll) + str(roomBitCount) # Encodes the room data into a 3 digit code
  roomList.append(str(roomData)) # Adds the room data to a list


print('\u001b[0mThe encoded room data is:')
for items in list(roomList):
  print(str(x + 1) + ':', roomList[x])
  x = x + 1

  time.sleep(0.01) # For florish, lol
x = 0
for num in list(roomList): # This whole block is for development
  num = int(roomList[x]) #!
  
  int1 = (num % 1000) // 100#!
  int2 = (num % 100) // 10#!
  int3 = (num % 10)#!
  print('\n')#!
  print(int1, int2, int3)#!
  print('Room Type', int1,'\nRoom Variant', int2, '\nRoom Number', int3)#!
  x = x + 1#!

os.system('clear')
  ## START OF GAME STUFF!
print('Game Start!') # This is all temporary, untill I get a buddy to do some story design!



while statRepeat == 1: # Keeps character screen open till finished
  print('\u001b[34m') # Just text
  print('Make your character') # Just text
  print('===================') # Just text
  print('\u001b[0m') # Just text
  print('\u001b[31mStr\u001b[0m:', strength) # Shows Strength Stat
  print('\u001b[36mDef\u001b[0m:', defence) # Shows Defence Stat
  print('\u001b[32mLuck\u001b[0m:', luck) # Shows Luck Stat
  print('You have\u001b[33m', statPoints, '\u001b[0mStat Points to spend\nPlease select the stat you want to increase.') # Shows how many stat points you have, and prompts you to use them
  statChoice = input('>> ') # the "terminal"

  if statChoice == 'str': # Checks if the user types "str"
    print('How many points do you want to spend?') # Just text
    statAdd = input('>> ') # the "terminal"
    if int(statAdd) > int(statPoints): # if you have less stat points than you want to spend
      print("You don't have that many points!") # Just text
      time.sleep(0.5) # Waits 0.5 seconds
    elif int(statAdd) <= int(statPoints): # if you have more than or the same amount that you want to spend
      strength = int(strength) + int(statAdd) # Sets strength stat
      statPoints = int(statPoints) - int(statAdd) # removes stat points
    os.system('clear')

  if statChoice == 'def': # Checks if the user types "def"
    print('How many points do you want to spend?') # Just text
    statAdd = input('>> ') # the "terminal"
    if int(statAdd) > int(statPoints): # if you have less stat points than you want to spend
      print("You don't have that many points!") # Just text
      time.sleep(0.5) # Waits 0.5 seconds
    elif int(statAdd) <= int(statPoints): # if you have more than or the same amount that you want to spend
      defence = int(defence) + int(statAdd) # Sets Defence stat
      statPoints = int(statPoints) - int(statAdd) # removes stat points
    os.system('clear')
      
  if statChoice == 'luck': # Checks if the user types "luck"
    print('How many points do you want to spend?') # Just text
    statAdd = input('>> ') # the "terminal"
    if int(statAdd) > int(statPoints): # if you have less stat points than you want to spend
      print("You don't have that many points!") # Just text
      time.sleep(0.5) # Waits 0.5 seconds
    elif int(statAdd) <= int(statPoints): # if you have more than or the same amount that you want to spend
      luck = int(luck) + int(statAdd) # Sets Luck stat
      statPoints = int(statPoints) - int(statAdd)# removes stat points
    os.system('clear')

  if statPoints <= 0: # Checks if you are out of stat points
    print('Enter name') # Asks for character name
    name = input('>> ') # Terminal
    print('**Character Created, Starting Story**') # Just text
    statRepeat = 0 # Ends loop
    time.sleep(1) # Waits 1 second
    os.system('clear')

## FIRST ROOM
print('This is where the first room will begin') # Filler text

## ROOM DECODER - First Room
num = int(roomList[0])

int1 = (num % 1000) // 100
int2 = (num % 100) // 10
int3 = (num % 10)

int2 = 1 ## TEMP ##
if int2 == 1:
  print('A few day ago in a bar you \nheard about a strange cave out\nin the woods. With the promise\nof loot, you head out in \nsearch of the cave.\n\n"Hey %s, come over here!\nI think I found it!' % name) # 30 characters
  print('Type "start" to begin the game.')


  while terminalRepeat == 1: # Terminal Repeat
    terminalInput = input('>> ') # Terminal
    if terminalInput == 'stats': # When you enter stats it will open the stats menu
      statCall() # opens stats
      os.system('clear')
      print('**Exited Stats**\n') # Just text
      print('A few day ago in a bar you \nheard about a strange cave out\nin the woods. With the promise\nof loot, you head out in \nsearch of the cave.\n\n"Hey %s, come over here!\nI think I found it!' % name) # 30 characters
      print('Type "start" to begin the game.')
      time.sleep(0.5)
      os.system('clear')
      print('A few day ago in a bar you \nheard about a strange cave out\nin the woods. With the promise\nof loot, you head out in \nsearch of the cave.\n\n"Hey %s, come over here!\nI think I found it!' % name) # 30 characters
      print('Type "start" to begin the game.')
    elif terminalInput == 'roomTest':
      roomTest()
    elif terminalInput == 'FreeTen':
      statPointAdd()
  
    elif terminalInput == 'levelUp':
      levelUp()

    elif terminalInput == 'start':
      terminalRepeat = 0
      os.system('clear')
      print('As you walk down the hill to where you heard you friend, Mark.\nIn front of Mark there is an anchint looking temple\n"This is the place!" Mark says\nDo you enter? ("y" or "n")')
      terminalRepeat = 1
      while terminalRepeat == 1: # Terminal Repeat
        terminalInput = input('>> ') # Terminal
        if terminalInput == 'stats': # When you enter stats it will open the stats menu
            statCall() # opens stats
            os.system('clear')
            print('**Exited Stats**\n') # Just text
            print('As you walk down the hill to where you heard you friend, Mark.\nIn front of Mark there is an anchint looking temple\n"This is the place!" Mark says\nDo you enter? ("y" or "n")') # 30 characters
            time.sleep(0.5)
            os.system('clear')
            print('As you walk down the hill to where you heard you friend, Mark.\nIn front of Mark there is an anchint looking temple\n"This is the place!" Mark says\nDo you enter? ("y" or "n")') # 30 characters
            
        elif terminalInput == 'FreeTen':
            statPointAdd()
        
        elif terminalInput == 'levelUp':
            levelUp()
        elif terminalInput == 'roomTest':
          roomTest()
        elif terminalInput == 'y':
          terminalRepeat = 0
          os.system('clear')
          print('This is the yes answer')

        elif terminalInput == 'n':
          terminalRepeat = 0
          os.system('clear')
          print('This is the no answer')
        elif terminalInput == 'end':
          print('**Bye**')
          terminalRepeat = 0
        else:
          os.system('clear')
          print('As you walk down the hill to where you heard you friend, Mark.\nIn front of Mark there is an anchint looking temple\n"This is the place!" Mark says\nDo you enter? ("y" or "n")')
      
    elif terminalInput == 'end':
      print('**Bye**')
      terminalRepeat = 0
    else:
      os.system('clear')
      print('A few day ago in a bar you \nheard about a strange cave out\nin the woods. With the promise\nof loot, you head out in \nsearch of the cave.\n\n"Hey %s, come over here!\nI think I found it!' % name) # 30 characters
      print('Type "start" to begin the game.')
      
if int2 == 2:
  print('This is the second variation')
  print('Room 1, Seed 1, Variant 2')
  while terminalRepeat == 1: # Terminal Repeat
    terminalInput = input('>> ') # Terminal
    if terminalInput == 'stats': # When you enter stats it will open the stats menu
      statCall() # opens stats
      os.system('clear')
      print('**Exited Stats**\n') # Just text
      print("This is the second variation") # Just text
      time.sleep(0.5)
      os.system('clear')
      print("This is the second variation") # Just text
  
    elif terminalInput == 'FreeTen':
      statPointAdd()
  
    elif terminalInput == 'levelUp':
      levelUp()

    elif terminalInput == 'start':
      os.system('clear')
      print('This is where the game will start')
      terminalRepeat = 0
  
    elif terminalInput == 'end':
      print('**Bye**')
      terminalRepeat = 0
    else:
      os.system('clear')

if int2 == 3:
  print('This is the third variation')
  print('Room 1, Seed 1, Variant 3')
  while terminalRepeat == 1: # Terminal Repeat
    terminalInput = input('>> ') # Terminal
    if terminalInput == 'stats': # When you enter stats it will open the stats menu
      statCall() # opens stats
      os.system('clear')
      print('**Exited Stats**\n') # Just text
      print("This is the third variation") # Just text
      time.sleep(0.5)
      os.system('clear')
      print("This is the third variation") # Just text
  
    elif terminalInput == 'FreeTen':
      statPointAdd()
  
    elif terminalInput == 'levelUp':
      levelUp()

    elif terminalInput == 'start':
      os.system('clear')
      print('This is where the game will start')
      terminalRepeat = 0
    
    elif terminalInput == 'end':
      print('**Bye**')
      terminalRepeat = 0
    
    else:
      os.system('clear')