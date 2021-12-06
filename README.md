# Janggi-Game
Hello I'd like to play a game ;) Korean Chess game that is. This is a very simple game with a 
several pieces listed below.

# Installation
Please see the following programs used:
* Python3

# Start
* To start the game, please initialize the class JanggiGame.

# Rules
This game is blue vs red. Blue starts first and after each valid move, the turn will switch over to the 
opposing color. The game will end once the enemy general is dead.

## General
Must stay within the nine-point fortress. He moves one point along any printed line in the 
fortress.

## Elephant
This piece has a very unusual move, found only in Korean chess. He starts one point forward, backward, left or right,
and then moves two points outward diagonally, like an extended knight’s move. He can be blocked anywhere along this path
, as he is in the diagram by the green cannon, and by the red rook.

## Guard
Moves exactly the same as the General, and is also confined to the fortress.

## Canon
If you are acquainted with Chinese chess, note that the Korean cannon has some important differences. The cannon moves 
along any straight line, including the lines within the fortress, but must have one piece to jump over. In the diagram 
below, the cannon (H) can move to point A (jumping over the pawn at B); to M (jumping over K); to E (jumping over F); 
and may capture the green piece on D. He may not jump over more than one piece (to point C), and may not move without 
jumping (points G, L and N). Also, he may not leap over another cannon (friend or foe) (can not go over I to J), and may 
never capture another cannon.

## Chariot
Moves as many points as he wishes, in a straight line, along the lines of the board. This is the same move as the 
western rook, but note that the Korean rook can also move along the diagonal lines in the fortress, if he is already 
on one of these points. He can not jump over pieces (such as the red queen in the diagram), and he captures as he moves
 (and so, can capture the green piece at his right).
 
## Horse
One point forward, backward, left or right plus one point outward diagonally, as shown in the diagram at right. 
This is similar to the western knight, but the Korean knight can be blocked. Note that in the diagram (right) the knight
can not move to the red marked points, because he is blocked by the pawn on his right. (He is not blocked by the pawn 
on his left.)

## Soldier
One point, either forward or sideways.

# Example
```
game = JanggiGame()
move_result = game.make_move('c1', 'e3') #should be False because it's not Red's turn
move_result = game.make_move('a7,'b7') #should return True
blue_in_check = game.is_in_check('blue') #should return False
game.make_move('a4', 'a5') #should return True
state = game.get_game_state() #should return UNFINISHED
game.make_move('b7','b6') #should return True
game.make_move('b3','b6') #should return False because it's an invalid move
game.make_move('a1','a4') #should return True
game.make_move('c7','d7') #should return True
game.make_move('a4','a4') #this will pass the Red's turn and return True
```
