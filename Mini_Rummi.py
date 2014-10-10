# This is a version of Rummikub where a player is playing the computer.
# We're still only using an adjusted set of tiles, making a string rather than multiple sets.
# This version will not use any classes, since I'm not sure it actually adds anything. 
# And I wish to keep my code as clean as possible.
# It's not a complete version though, just an intermediary step, but at least there is some 
# player interaction now. :)

# Here's the rules:
# Each player starts with 5 tiles on their shelf and the first player to use all the tiles
# on their shelf and thereby emptying the shelf, wins.
# In the game there are three options:
# 1. If you can't make a move, you can take a tile
# 2. You can add tiles to the board
# 3. You can make a combination of tiles on your shelf and put them out onto the board.


## Je gebruikt op dit moment Testertje.py om de play-functie aan het werk te krijgen.



import random
from sys import exit
from itertools import groupby
from operator import itemgetter


board = []				# This is the playing field on which the tiles are placed.
to_add = []        		# Global variable for tracking sets to add
add_no = []				# Global variable for tracking tiles to add
turn = ()				# Global variable that tells the play-function which script to follow
move_possible = []		# tracks if a move is possible
set_possible = []		# tracks what type of move is possible
tile_possible = []		# tracks what type of move is possible
move_made = []			# tracks what move has been made
shelf_p1 = []			# shelf of human player	
shelf_cp = []			# shelf of computer
counter = 0				# global variable tracking turns after tiles is empty.
move_counter = 0		# global variable counting the moves of player 1 
						# it's to check he/she doesn't pick a tile when he/she already made a move.	


# *******************************************************************************

# Picking tiles at the start of the game.		
def pick_tiles(tiles, shelf):        #To start the game, 5 tiles need to be picked.
	for i in range(0, len(shelf)):   #for every position(!) on the shelf, add a tile  
		shelf[i] = tiles.pop()
	shelf.sort()

# In order to add tiles to the board, we need to know if we have a set on our shelf.
# A set is a list of 3 or more consecutive numbers.
# How can we check if a set is a set on our shelf?
		
# as adapted from a recommendation on StackOverflow
def check_for_set(shelf):
	global to_add
	
	to_add = []
	for k,g in groupby(enumerate(shelf), lambda (i,x):i-x):
		sub_set = map(itemgetter(1), g)        # map takes the function itemgetter and 
		                                       # applies it to all g
		if len(sub_set) > 2:        #if the length of the set is greater than 2, save it
			to_add = sub_set
		else:
			pass					# Else, nothing

# checks for single tiles from the shelf to add 
def check_for_single_tiles_to_add(shelf):		
	global add_no
	add_no = []

	for i in shelf: 								#for every element on the shelf
		if ((i)+1) in board:
			add_no.append(i)
		elif ((i)-1) in board:
			add_no.append(i)
		else:
			pass	


def move_possible_questionmark(shelf):		# Determines if a move is possible.
	global to_add
	global add_no
	global move_possible
	global set_possible
	global tile_possible

	move_possible = []
	set_possible = 0
	tile_possible = 0
	
	check_for_set(shelf)
	check_for_single_tiles_to_add(shelf)
		
	if to_add or add_no: 
		move_possible = 1
		if to_add and add_no:
			set_possible = 1
			tile_possible = 1		
		elif to_add:
			set_possible = 1
		elif add_no:
			tile_possible = 1
		else:
			pass			
	else:
		move_possible = 0	


def tussenstapje():
	global turn
	global shelf_p1
	global shelf_cp
	global board
	global tiles	
	
	answer = []
	
	print "\nWould you like to continue?"
	answer = raw_input("y/n >")
	if answer == "y":
		if turn == 1:	
			play(shelf_p1, tiles, board)
		elif turn == 2:
			play(shelf_cp, tiles, board)	
		else:
			print "Error, contact administrator."
	else:
		print "You seem unsure. Let's restart the game."
		print " "
		print "Restarting game"
		print "/"
		print "-"
		print "\\"
		print "|"
		print "/" 
		start_game() 	


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
	
	if sum(sets_in_1) > sum(sets_in_2):			# If Player one has a bigger set than computer
		print "Player 1 may begin."
		turn = 1
		#play(s1, tiles, board)
	elif sum(sets_in_1) < sum(sets_in_2): 		# If Computer has a great set than player
		print "Computer may begin."
		turn = 2
		#play(s2, tiles, board)
	else:										# If neither have a set,
		if s1[-1] > s2[-1]:						# the highest tile gets to begin.
			print "Player 1 may begin."
			turn = 1
		#	play(s1, tiles, board)
		else:
			print "Computer may begin."
			turn = 2
		#	play(s2, tiles, board)
	
	tussenstapje()	

# *******************************************************************************
# types of plays in the game:

# adding a set to the board:
def add_set(board, shelf):
	global move_made
	global to_add
		
	to_add = []	
	check_for_set(shelf)								# controleert of er een setje op de plank staat,				
														# returns a value to to_add.	
	if not to_add:
		move_made = []
	else:
		first_index_no = shelf.index(to_add[0])        # Gives us the index no of the first value in to_add on our shelf
		length_set = len(to_add)
		
		while length_set != 0:							# While not all of the elements in to_add are added
			board.append(shelf.pop(first_index_no))		
			length_set -= 1
			# And this works, because index no. x get's popped everytime, so then the next element gets that index no.				
		move_made = 1
	    
	board.sort()
	shelf.sort()


# Adding one or more items to the board.
def add_one(board, shelf):
	global move_made
	global add_no
		
	add_no = []
	check_for_single_tiles_to_add(shelf)		
			
	if add_no:
		for i in add_no:        # I had to append to the board separately since the code wasn't running properly otherwise.
			dex_no = shelf.index(i)
			board.append(shelf.pop(dex_no))	
		move_made = 1
	else:
		pass
	
	board.sort()
	shelf.sort()
				
	
# Taking one from the pile, since there is no other move possible.
def take_one(tiles, shelf):
	new_tile = tiles.pop(0)
	shelf.append(new_tile)        # Pops the first tile of Tiles and appends it to shelf
	shelf.sort()
	
# *******************************************************************************

def play(shelf, tiles, board):
	global turn
	global move_made
	global move_possible
	global shelf_p1
	global shelf_cp
	global counter
	global set_possible
	global tile_possible
	global move_counter
	global add_no
	global to_add

	# Variables for first player input
	answer = []
	move_counter = 0
	
	while turn == 1:					# player_1's turn - later afmaken
		
		print "\nTiles on your shelf:", shelf
		print "Tiles left:", len(tiles)
		print "Tiles on the board:", board
		
		move_possible_questionmark(shelf)	# checks whether any move is possible at all.
				
		print "\nWhat would you like to do?"
		print "Add a Tile (t), Add a Set (s), Pick a Tile (p), Pass (pass)?"
		answer = raw_input("t/s/p/pass >")
		
		if answer == "t":
			if tile_possible == 0:
				print "You don't seem to have tiles to add to the board."
			else:
				add_one(board, shelf_p1)
				print "This was added to the board: ", add_no
				move_counter += 1
				
			if not shelf:					# if these moves empty then shelf, then
				print "This is on the board: ", board
				print "Game Over!"
				print "Player 1 wins!"
				exit()
			else:
				pass				
		elif answer == "s":
			if set_possible == 0:
				print "You don't seem to have a set to add to the board."
			elif set_possible == 1:
				add_set(board, shelf_p1)	 	
				print "This was added to the board: ", to_add
				move_counter += 1

			if not shelf:					# if these moves empty then shelf, then
				print "This is on the board: ", board
				print "Game Over!"
				print "Player 1 wins!"
				exit()
			else:
				pass				
			
		elif answer == "p":
			if move_counter > 0:
				print "You've already made a move and can't take a tile."
				print "You just forfeited the game. Computer wins."
				exit()
			else: 	
				if tiles:						# if there are tiles left, grab a tile
					print "Player 1 takes a tile."
					take_one(tiles, shelf_p1)
					print "Tiles on your shelf:", shelf
					print "End turn Player 1."
					turn = 2
					play(shelf_cp, tiles, board)					
				else: 							# if there are no tiles left
					print "No more tiles left."
					if counter < 2:				# if the turn counter is less than 2, then
						counter += 1
						print "End turn Player 1."
						turn = 2
						play(shelf_cp, tiles, board)
					else:						# if the turn counter has not been increased, then just carry on		
						print "This is on the board: ", board
						print "Game Over!"
						if not board:				# als er geen stenen zijn uitgelegd: "tie"
							print "It's a tie!"
							exit()
						elif sum(shelf_p1) < sum(shelf_cp):		# als er wel stenen zijn uitgelegd, dan wint de laagste some van shelf			
							print "Player_1 has %r left" %shelf_p1
							print "Computer has %r left" %shelf_cp
							print "Player 1 wins!"
							exit()
						elif sum(shelf_p1) == sum(shelf_cp):		
							print "Player_1 has %r left" %shelf_p1
							print "Computer has %r left" %shelf_cp
							print "It's a tie!"
							exit()
						elif sum(shelf_p1) > sum(shelf_cp):		
							print "Player_1 has %r left" %shelf_p1
							print "Computer has %r left" %shelf_cp
							print "Computer wins!"
							exit()
						else:	
							pass
				
		elif answer == "pass":
			print "End turn player 1."
			turn = 2
			play(shelf_cp, tiles, board)
		else:
			print "%r is not a valid option." %answer
				
			
	while turn == 2:					# Computer's turn
		print "\nComputer starts turn:"
		print "Tiles left:", len(tiles)
		
		move_possible_questionmark(shelf)	# checks whether any move is possible at all.
		
		if move_possible == 1:				# if there is an action the player can take, then...
			move_made = []					# make the move
			add_set(board, shelf_cp)
			add_one(board, shelf_cp)
			add_one(board, shelf_cp)        # You have to check if there are sets of 2 on your shelf that could both be added.
			print "Tiles on the board:", board
			if not shelf:					# if these moves empty then shelf, then
				print "Game Over!"
				print "Computer wins!"
				exit()
			else:
				print "End turn Computer."
				turn = 1
				play(shelf_p1, tiles, board)
		
		elif move_possible == 0:			# if there are no actions the player can take, then...
			if tiles:						# if there are tiles left, grab a tile
				print "Computer can't make a move. Takes a tile."
				take_one(tiles, shelf_cp)
				print "End turn Computer."
				turn = 1
				play(shelf_p1, tiles, board)					
			else: 							# if there are no tiles left
				print "No more tiles left."
				if counter < 2:				# if the turn counter is less than 2, then
					counter += 1
					print "End turn Computer."
					turn = 1
					play(shelf_p1, tiles, board)
				else:						# if the turn counter has not been increased, then just carry on		
					print "Game Over!"
					if not board:				# als er geen stenen zijn uitgelegd: "tie"
						print "It's a tie!"
						exit()
					elif sum(shelf_p1) < sum(shelf_cp):		# als er wel stenen zijn uitgelegd, dan wint de laagste some van shelf			
						print "Player_1 has %r left" %shelf_p1
						print "Computer has %r left" %shelf_cp
						print "Player 1 wins!"
						exit()
					elif sum(shelf_p1) == sum(shelf_cp):		
						print "Player_1 has %r left" %shelf_p1
						print "Computer has %r left" %shelf_cp
						print "It's a tie!"
						exit()
					elif sum(shelf_p1) > sum(shelf_cp):		
						print "Player_1 has %r left" %shelf_p1
						print "Computer has %r left" %shelf_cp
						print "Computer wins!"
						exit()
					else:	
						pass
							
		else: 
			print "Error, consult administrator."	
			exit()
		
		

def start_game():
	global turn 
	global tiles
	global shelf_p1
	global shelf_cp
	
	tiles = range(1,31)		# Creates a set of 30 tiles ranging from 1 to 30
	random.shuffle(tiles)	# This shuffles up the tiles so we can begin playing.	
	print "\nWelcome to this automated version of a MiniRummi!"
	print "This is a player-version and you will be playing the computer."
	print "There are 30 tiles in the game, ranging from 1 to 30."
	print "In a moment the tiles will be shuffled and we can begin the game."
	print "/"
	print "-"
	print "\\"
	print "|"
	print "/" 

	print "Tiles have been shuffled."
	print "Number of tiles in the game:\n", len(tiles)
	print "Let's start this game! \n\n"

	shelf_p1 = [0] * 5        #Let's us start with 5 starting positions.
	shelf_cp = [0] * 5
		
	
	print "\nPlayer 1 picks tiles:"
	pick_tiles(tiles, shelf_p1) 
	print shelf_p1
	
	print "\nComputer picks tiles:"
	pick_tiles(tiles, shelf_cp)
	
	first_to_play(shelf_p1, shelf_cp, tiles, board)
	
	
start_game()
