Python_project_Rummikub
=======================

This is a learning project in Python to make my own digital version of Rummikub.

Started learning to code in Python and gave myself a few summer project to work on.
As this project advances, more complicated things arrise and this project will probably continue for a bit longer.

=======================================================================================================================
The Game: Rummikub
This game is played with a sets of numbers ranging from 1 to 13 in four colours (red, blue, black, and yellow). There are two of every tile and two additional jokers, making a total of 106 tiles.  

The game can be played with 1 to 4 players. 
Each player has their own shelf and start out with 14 tiles. 

The goal of the game is to play all the tiles on your shelf, until no tiles are left on your shelf.
The person who finishes first, wins the game.
To determine 2nd, 3rd, and 4th place, add up the value of the remaining tiles on the shelfs.

Moves you can make:
1. make sets
2. add tiles to the sets that have already been played.
3. take a tile

1. Make a set
A set consists of a minimum of 3 tiles and can either be 
  - a range in the same colour (red 1,2,3)
  - the same number with different colours (red 13, blue 13, black 13).

Note:
Range (red 4, black 5, blue 6) or (red 8, red 8, blue 8) are not sets.

2. Add tiles to existing sets
You can add tiles to existing sets. For example: 
Say you have a (black 11), and in the game is a set of (red 11, blue 11, yellow 11) then you can add your tile to this set.
You can also rearrange tiles in order to add your tile, however, in rearranging tiles you may not take tiles back on your shelf and each of the newly rearranged sets have to have a minimum of three tiles per set.

3. Take a tile
If you can't make a set or add a tile in your turn, you ahve to pick a tile from the pile.


Jokers
The game should contain two jokers that allow you to use in place of any tile you may need and will take on the value of the tile it replaces. 
For instance if you have a joker, a (blue 10), and a (blue 12) you can make the set (blue 10, joker, blue 12).
Once the joker haas been played it has to stay in the game, i.e. if the next player adds a tile by replacing the joker with a (blue 11), the player now has to make a new set with the joker, or add the joker to an existing set. 
The joker cannot be put back on the shelf for later use once it's played.

For your first turn, you have to have a set of a minimum of 30 points before you can play.
You can count your points by adding up the tiles in the sets you can make.
For instance, if you can make a set of (red 11, blue 11, yellow 11) you are making a set with 33 point and you can make your first move. However, if you can only make a set of (red 1,2,3) (6 points) then you will have take tiles until you have another set to add up to 30 points. 
After you first move, you are not restricted by a minimum of points to play. 


================================================================================================================

Where I'm at:
  1. I have not figured out a good way to create a set with tiles that have both the atribute colour and the atribute number.
  2. I only have a 2 player game where the computer plays itself.
  3. I'm currently working with a double set ranging 1 to 9 - no colours.
  4. And it works, it prints out a game rapport as the game progresses until there is a winner.

All this is documented in the file Mini_Rummi



