# This is a mini version of Rummikub just to see if I can make it work.
# This is the version using the class player.
#
# Here's the rules:
# The computer is playing itself. 
# Each player starts with 8 tiles on their shelf and the first player to use all the tiles
# on their shelf and thereby emptying the shelf, wins.
# In the game there are three options:
# 1. If you can't make a move, you can take a tile
# 2. You can add tiles to the board
# 3. You can make a combination of tile on your shelf and put them out onto the board.

import random
from sys import exit
from itertools import groupby
from operator import itemgetter

class Player(object):
 	def __init__(self, name):
 		self.name = name 	
 	shelf = []	


player_1 = Player("player_1")
computer = Player("computer")

	

tiles = range(1,30)		# Creates a set of 18 tiles ranging from 1 to 18, including 18.
board = []				# This is the playing field on which the tiles are placed.
to_add = []        		# Has to be a global variable.
turn = ()				# also has to be a global variable
move_made = []

random.shuffle(tiles)	# This shuffles up the tiles so we can begin playing.	
print "\nWelcome to this automated version of a MiniRummi!"
print "This is a spectator version, so watch and learn."
print "There are two players, both played by the computer."
print "There are 18 tiles in the game, ranging from 1 to 18."
print "In a moment the tiles will be shuffled and we can begin the game."
print "/"
print "-"
print "\\"
print "|"
print "/" 

print "Tiles have been shuffled."
print "Number of tiles in the game:\n", len(tiles)
print "Let's start this game! \n\n"

# *******************************************************************************


# Picking tiles at the start of the game.		
def pick_tiles(tiles, shelf):        #To start the game, 4 tiles need to be picked.
	for i in range(0,4):        #for every position on the shelf, add a tile  
		shelf[i] = tiles.pop(0)
	shelf.sort()
	print shelf, "\n"


# In order to add tiles to the board, we need to know if we have a set on our shelf.
# A set is a list of 3 or more consecutive numbers.
# How can we check if a set is a set on our shelf?
		
# as adapted from a recommended on StackOverflow
def check_for_set(list):
	global to_add
	
	for k,g in groupby(enumerate(list), lambda (i,x):i-x):
		sub_set = map(itemgetter(1), g)        # map takes the function itemgetter and 
		                                       # applies it to all g
		if len(sub_set) > 2:        #if the length of the set is greater than 3, save it
			to_add = sub_set
		else:
			pass					# Else, nothing


# types of plays in the game:

# adding a set to the board:
def add_set(board, shelf):
	global move_made
	global to_add
		
	check_for_set(shelf)
	
	if not to_add:
		print "Nothing to add"        # If to_add is empty
		move_made = []
	else:
		first_index_no = shelf.index(to_add[0])        # Gives us the index no of the first value in to_add on our shelf
		length_set = len(to_add)
		
		while length_set != 0:							# While not all of the elements in to_add are added
			board.append(shelf.pop(first_index_no))		
			length_set -= 1
			# And this works, because index no. x get's popped everytime, so then the next element gets that index no.				
		to_add = []
		move_made = 1
	    
	board.sort()
	shelf.sort()


# Adding one or more items to the board.
def add_one(board, shelf):
	global move_made
	
	add_no = []
	for i in shelf: 	#for every element on the shelf
		if ((i)+1) in board:
			add_no.append(i)
		elif ((i)-1) in board:
			add_no.append(i)
		else:
			pass
	
	if add_no:
		for i in add_no:        # I had to append to the board separately since the code wasn't running properly otherwise.
			dex_no = shelf.index(i)
			board.append(shelf.pop(dex_no))	
		move_made = 1
	else:
		print "Nothing to add."
		pass
			
	board.sort()
	shelf.sort()
				
	
# Taking one from the pile, since there is no other move possible.
def take_one(tiles, shelf):
	new_tile = tiles.pop(0)
	print "New tile:", new_tile
	shelf.append(new_tile)        # Pops the first tile of Tiles and appends it to shelf
	shelf.sort()
	print "Tiles on the shelf: %s" % shelf

	
# ************************************************************************************

### To decide who get's to play first, we run first_to_play
# Either the person who has a set on its shelf or the person who has the highest number
def first_to_play(s1, s2, tiles, board):
	global to_add
	global turn 
	
	check_for_set(s1)
	sets_in_1 = to_add
	to_add = []
	
	check_for_set(s2)
	sets_in_2 = to_add
	to_add = []
	
	if sum(sets_in_1) > sum(sets_in_2):
		print "Player 1 may begin."
		turn = 1
		play(s1, tiles, board)
	elif sum(sets_in_1) < sum(sets_in_2): 
		print "Computer may begin."
		turn = 2
		play(s2, tiles, board)
	else:
		if s1[-1] > s2[-1]:
			print "Player 1 may begin."
			turn = 1
			play(s1, tiles, board)
		else:
			print "Computer may begin."
			turn = 2
			play(s2, tiles, board)
	
		
def play(shelf, tiles, board):
	global turn
	global move_made
	global shelf_2
	counter = 0

	while shelf and turn == 1:	
		print "\nPlayer 1 makes a move:"
		print "Tiles left:", len(tiles)
		print "Tiles on the board:", board
		print "Tiles on the shelf", shelf
		move_made = []
		add_set(board, player_1.shelf)
		add_one(board, player_1.shelf)
		add_one(board, player_1.shelf)        # You have to check if there are sets of 2 on your shelf that could both be added.
		
		if not move_made and tiles:
			print "Player 1 can't make a move. Takes a tile."
			take_one(tiles, player_1.shelf)
		else:
			print "Tiles on the board:", board
			print "Tiles left on the shelf", shelf
			pass	
		print "End turn player 1."
		
		if not shelf:
			print "Game Over!" 
			print "Player 1 wins!"
			exit()
		elif len(shelf) == 9 and not tiles and not board:
			print "Game over!"
			print "It's a tie!"
			exit()
		elif not tiles and counter>2:
			print "Game over!"
			print "No more tiles available."	
			if sum(player_1.shelf) < sum(computer.shelf):
				print "Player 1 wins!"
				exit()
			elif sum(player_1.shelf) == sum(computer.shelf):
				print "It's a tie!"
				exit()
			else:
				print "Computer wins!"
				exit()		
		else:
			turn = 2
			play(computer.shelf, tiles, board)
			
	while shelf and turn == 2:
		print "\nComputer makes a move:"
		print "Tiles left:", len(tiles)
		print "Tiles on the board:", board
		print "Tiles on the shelf", shelf
		move_made = []
		add_set(board, computer.shelf)
		add_one(board, computer.shelf)
		add_one(board, computer.shelf)        # You have to check if there are sets of 2 on your shelf that could both be added.
		
		if not move_made and tiles:
			print "Computer can't make a move. Takes a tile."
			take_one(tiles, computer.shelf)
		else:
			print "Tiles on the board:", board
			print "Tiles left on the shelf", shelf
			pass	
		print "End turn computer."
		
		if not shelf:
			print "Game over!"
			print "Computer wins!"
			exit()
		elif len(shelf) == 9 and not tiles and not board:
			print "Game over!"
			print "It's a tie!"
			exit()
		elif not tiles and counter>2:			
			print "Game over!"
			print "No more tiles available."	
			if sum(player_1.shelf) < sum(computer.shelf):
				print "Player 1 wins!"
				exit()
			elif sum(player_1.shelf) == sum(computer.shelf):
				print "It's a tie!"
				exit()
			else:
				print "Computer wins!"
				exit()		
		else:
			turn = 1
			play(player_1.shelf, tiles, board)
 	
 		

def start_game():
	global turn 
	
	player_1.shelf = [0] * 8        #Let's us start with 4 starting positions.
	computer.shelf = [0] * 8
	
	print "Player 1 picks tiles:"
	pick_tiles(tiles, player_1.shelf) 
	
	print "Computer picks tiles:"
	pick_tiles(tiles, computer.shelf)
	
	first_to_play(player_1.shelf, computer.shelf, tiles, board)
	
	
start_game()
	


		

