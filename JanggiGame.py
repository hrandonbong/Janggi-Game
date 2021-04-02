#Author: Brandon Hong
#Date: 3/7/21
#Description: Janggi Game is a korean game similar to western chess. This is a class game that will create
# a chess board 10x9 (rows x column).
#General - (King) must be within the fortress, can make 1 move
#Guards - Moves within fortress any direction
#Horses - (Knight) moves 1 frwrd/side and 1 diag. Can be blocked by a piece infront of it
#Elephants - moves 1 frwrd/side and 2 diag. Can be blocked by a piece infront of it
#Chariots - (Rook) can go diag in the fortress too
#Cannons - Moves like rook, but jumps a single piece in btwn it and it's target. Cannot jump cannons
#Soliders - (pawns) move forward 1 or side 1

class JanggiGame:
    """
    A eastern like chess game that has 7 types of pieces:
    (2) Chariots - moves like a rook, can move any number of spaces horiz or vert
    (2) Elephants – moves 3 vert/horiz then 2 sideways motion. Can be blocked if a piece is in between it and its target location
    (2) Horses – moves 2 vert/horiz then 1 sideways motion. Can be blocked if a piece is in between it and its target location
    (2) Guards – has to stay within palace, can move 1 space
    (1) General – has to stay within palace, can move 1 space
    (2) Cannons – has to jump any piece to move to target location
    (5) Soldiers – can move 1 space

    """
    def __init__(self):
        self._board = [['a1' , 'b1' , 'c1' , 'd1' , 'e1' , 'f1' , 'g1' , 'h1' , 'i1'],
                       ['a2' , 'b2' , 'c2' , 'd2' , 'e2' , 'f2' , 'g2' , 'h2' , 'i2'],
                       ['a3' , 'b3' , 'c3' , 'd3' , 'e3' , 'f3' , 'g3' , 'h3' , 'i3'],
                       ['a4' , 'b4' , 'c4' , 'd4' , 'e4' , 'f4' , 'g4' , 'h4' , 'i4'],
                       ['a5' , 'b5' , 'c5' , 'd5' , 'e5' , 'f5' , 'g5' , 'h5' , 'i5'],
                       ['a6' , 'b6' , 'c6' , 'd6' , 'e6' , 'f6' , 'g6' , 'h6' , 'i6'],
                       ['a7' , 'b7' , 'c7' , 'd7' , 'e7' , 'f7' , 'g7' , 'h7' , 'i7'],
                       ['a8' , 'b8' , 'c8' , 'd8' , 'e8' , 'f8' , 'g8' , 'h8' , 'i8'],
                       ['a9' , 'b9' , 'c9' , 'd9' , 'e9' , 'f9' , 'g9' , 'h9' , 'i9'],
                       ['a10', 'b10', 'c10', 'd10', 'e10', 'f10', 'g10', 'h10', 'i10']]

        self._set = [['RC', 'RE' , 'RH' , 'RG', 'e1' , 'RG', 'RE', 'RH' , 'RC'],
                       ['a2' , 'b2' , 'c2' , 'd2', 'RGe', 'f2', 'g2', 'h2' , 'i2'],
                       ['a3' , 'RCa', 'c3' , 'd3', 'e3' , 'f3', 'g3', 'RCa', 'i3'],
                       ['RS' , 'b4' , 'RS' , 'd4', 'RS' , 'f4', 'RS', 'h4' , 'RS'],
                       ['a5' , 'b5' , 'c5' , 'd5', 'e5' , 'f5', 'g5', 'h5' , 'i5'],
                       ['a6' , 'b6' , 'c6' , 'd6', 'e6' , 'f6', 'g6', 'h6' , 'i6'],
                       ['BS' , 'b7' , 'BS' , 'd7', 'BS' , 'f7', 'BS', 'h7' , 'BS'],
                       ['a8' , 'BCa', 'c8' , 'd8', 'e8' , 'f8', 'g8', 'BCa', 'i8'],
                       ['a9' , 'b9' , 'c9' , 'd9', 'BGe', 'f9', 'g9', 'h9' , 'i9'],
                       ['BC' , 'BE' , 'BH' , 'BG', 'e10', 'BG', 'BE', 'BH' , 'BC']]

        self.red_diagonal = ['d1','f1','e2','d3','f3']
        self.blue_diagonal = ['d8', 'f8','e9','d10','f10']

        self._red_palace = ['d1' , 'e1' , 'f1', 'd2' , 'e2', 'f2' ,'d3' , 'e3' , 'f3']
        self._blue_palace = ['d8' , 'e8' , 'f8', 'd9' , 'e9', 'f9' ,'d10' , 'e10' , 'f10']

        self._red_pieces = ['RC','RE','RH','RG','RGe','RS','RCa']
        self._blue_pieces = ['BC','BE','BH','BG','BGe','BS','BCa']
        self._dead = []

        self._game_status = 'UNFINISHED'
        self._turn = 'blue'
        self._tracker = 0 #Even = Blue and Odd = Red

    def get_game_state(self):
        """Returns one of these values, depending on the game state:
            'UNFINISHED' or 'RED_WON' or 'BLUE_WON"""
        return self._game_status

    def is_in_check(self,color):
        """Parameter of color in string, returns true if color is in check"""

        #Functions use turn to determine moves, saving turn and will change it later
        if self._turn == 'blue':
            temp_status = 'blue'
        else:
            temp_status = 'red'

        #Creates a temporary board save so we can return back to the board before check is invoked
        temp_board = [[],[],[],[],[],[],[],[],[],[]]
        for n in range(0,10):
            for o in range(0,9):
                temp_board[n].append(self._set[n][o])

        #Saving the dead list to copy back in later
        temp_dead = []
        for n in range(0,len(self._dead)):
            temp_dead.append(self._dead[n])

        #Used to change what pieces we will be moving based on red or blue check
        if color == 'red':
            general = 'RGe'
            self._turn = 'blue'
            chariot = 'BC'
            horse = 'BH'
            elephant = 'BE'
            cannon = 'BCa'
            soldier = 'BS'
        else:
            general = 'BGe'
            self._turn = 'red'
            chariot = 'RC'
            horse = 'RH'
            elephant = 'RE'
            cannon = 'RCa'
            soldier = 'RS'

        # Finding General Location for next
        for k in range(0, 10):
            for l in range(0, 9):
                if self._set[k][l] == general:
                    next = self._board[k][l]

                    # Chariot Check
                    for i in range(0, 10):
                        for j in range(0, 9):
                            if self._set[i][j] == chariot:
                                current = self._board[i][j]
                                self.move_chariot(current, next, i, j)
                                if general in self._dead:
                                    print(color,"is in check.",color,"make a move.")
                                    self._set = temp_board
                                    self._dead = temp_dead
                                    self._turn = color
                                    return True

                    # Check Horse
                    for i in range(0, 10):
                        for j in range(0, 9):
                            if self._set[i][j] == horse:
                                current = self._board[i][j]
                                self.move_horse(current, next, i, j)
                                if general in self._dead:
                                    print(color, "is in check.", color, "make a move.")
                                    self._set = temp_board
                                    self._dead = temp_dead
                                    self._turn = color
                                    return True

                    # Check Elephant
                    for i in range(0, 10):
                        for j in range(0, 9):
                            if self._set[i][j] == elephant:
                                current = self._board[i][j]
                                self.move_elephant(current, next, i, j)
                                if general in self._dead:
                                    print(color, "is in check.", color, "make a move.")
                                    self._set = temp_board
                                    self._dead = temp_dead
                                    self._turn = color
                                    return True

                    # Check Soldier
                    for i in range(0, 10):
                        for j in range(0, 9):
                            if self._set[i][j] == soldier:
                                current = self._board[i][j]
                                self.move_soldier(current, next, i, j)
                                if general in self._dead:
                                    print(color, "is in check.", color, "make a move.")
                                    self._set = temp_board
                                    self._dead = temp_dead
                                    self._turn = color
                                    return True

                    #Check Cannon
                    for i in range(0, 10):
                        for j in range(0, 9):
                            if self._set[i][j] == cannon:
                                current = self._board[i][j]
                                self.move_cannon(current, next, i, j)
                                if general in self._dead:
                                    print(color, "is in check.", color, "make a move.")
                                    self._set = temp_board
                                    self._dead = temp_dead
                                    self._turn = color
                                    return True

                    #nothing is in check
                    self._set = temp_board
                    self._dead = temp_dead
                    self._turn = temp_status
                    return False

        #Added in case somehow it breaks out of loop
        self._set = temp_board
        self._dead = temp_dead
        self._turn = temp_status
        return False


    def general_valid(self,current):
        """Makes sure the generals do not face each other. Takes current location being moved
        and checks if there are any other pieces in that column, if not returns false and cannot
        move current piece."""
        #if piece between generals tries to move
        for i in range(0,4):
            for j in range(3,6):
                if self._set[i][j] == 'RGe':
                    for k in range(7,10):
                        if self._set[k][j] == 'BGe':
                            for l in range(i,k):
                                if self._board[l][j] == current:
                                    for m in range(i+1,10):
                                        if (self._set[m][j] in self._red_pieces \
                                           or self._set[m][j] in self._blue_pieces) \
                                            and (self._set[m][j] != 'BGe' and \
                                                self._set[m][j] != 'RGe') and (m != l):
                                            return True
                                    return False



    def make_move(self,current,next):
        """Takes current location, and next location as parameters. Will update the board or return
        false for invalid moves."""
        # print("Attempting: ",current, "->", next) #Used to check gradescope
        if self._game_status != 'UNFINISHED':
            return False

        #skipping turn
        if current == next:
            self.change_turn()
            return True

        #Making sure general's do not face each other
        valid = self.general_valid(current)
        if valid == False:
            return False

        #Moving pieces depending on what they are and finding it's coordinates
        for i in range(0,10):
            for j in range(0,9):
                if self._board[i][j] == current:
                    #Chariot
                    if (self._set[i][j] == 'RC' and self._turn == 'red') or\
                            (self._set[i][j] == 'BC'and self._turn == 'blue'):
                        result = self.move_chariot(current, next,i,j)
                        if result == False:
                            return False
                        self.change_turn()
                        self.is_general_dead()
                        return True
                    #Elephant
                    elif (self._set[i][j] == 'RE' and self._turn == 'red') or\
                            (self._set[i][j] == 'BE'and self._turn == 'blue'):
                        result = self.move_elephant(current, next,i,j)
                        if result == False:
                            return False
                        self.change_turn()
                        self.is_general_dead()
                        return True
                    #Horse
                    elif (self._set[i][j] == 'RH' and self._turn == 'red') or \
                            (self._set[i][j] == 'BH' and self._turn == 'blue'):
                        result = self.move_horse(current, next,i,j)
                        if result == False:
                            return False
                        self.change_turn()
                        self.is_general_dead()
                        return True
                    #Guardian
                    elif (self._set[i][j] == 'RG' and self._turn == 'red') or \
                            (self._set[i][j] == 'BG' and self._turn == 'blue'):
                        result = self.move_palace_pieces(current, next,i,j)
                        if result == False:
                            return False
                        self.change_turn()
                        self.is_general_dead()
                        return True
                    #General
                    elif (self._set[i][j] == 'RGe' and self._turn == 'red') or \
                            (self._set[i][j] == 'BGe' and self._turn == 'blue'):
                        result = self.move_palace_pieces(current, next,i,j)
                        if result == False:
                            return False
                        self.change_turn()
                        self.is_general_dead()
                        return True
                    #Soldier
                    elif (self._set[i][j] == 'RS' and self._turn == 'red') or \
                            (self._set[i][j] == 'BS' and self._turn == 'blue'):
                        result = self.move_soldier(current, next, i, j)
                        if result == False:
                            return False
                        self.change_turn()
                        self.is_general_dead()
                        return True
                    #Canon
                    elif (self._set[i][j] == 'RCa' and self._turn == 'red') or \
                            (self._set[i][j] == 'BCa' and self._turn == 'blue'):
                        result = self.move_cannon(current, next, i, j)
                        if result == False:
                            return False
                        self.change_turn()
                        self.is_general_dead()
                        return True
                    else:
                        return False


    def is_general_dead(self):
        """Checks to see if during the move the general died"""
        #If general did die, we check which one and determine the winner
        if 'RGe' in self._dead:
            self._game_status = 'BLUE_WON'
            return True
        elif 'BGe' in self._dead:
            self._game_status = 'RED_WON'
            return True
        else:
            return False

    def change_turn(self):
        """Changes the turn. self._turn is used throughout the functions to verify
        like colors are moving like pieces"""
        if self._turn == 'blue':
            self._turn = 'red'
        else:
            self._turn = 'blue'

    def move_chariot(self,current,next,i,j):
        """Inputs: current location, next location, (i,j).
        Expected: output to move piece to next location, or return false for any other outcome"""
        if self._set[i][j] == 'RC' or self._set[i][j] == 'BC':
            if current == self._board[i][j]:
                for k in range(0, 10):
                    for l in range(0, 9):
                        if self._board[k][l] == next:
                            # Chariot must move horizontal
                            if i == k or j == l:
                                return self.move_pieces(self._set[i][j], i, j, k, l)
                            # Chariot is in diagonals
                            #Red palace diagonals
                            elif current in self.red_diagonal and next in self.red_diagonal:
                                if abs(i - k) > 2 or abs(j - l) > 2:
                                    return False
                                return self.move_pieces(self._set[i][j], i, j, k, l)
                            #Blue palace dagonals
                            elif current in self.blue_diagonal and next in self.blue_diagonal:
                                if abs(i - k) > 2 or abs(j - l) > 2:
                                    return False
                                return self.move_pieces(self._set[i][j], i, j, k, l)

                            else:
                                return False
                return False


    def move_elephant(self,current,next,i,j):
        """Inputs: current location, next location, (i,j).
            Expected: output to move piece to next location, or return false for any other outcome"""
        if self._set[i][j] == 'RE' or self._set[i][j] == 'BE':
            if current == self._board[i][j]:
                for k in range(0, 10):
                    for l in range(0, 9):
                        if self._board[k][l] == next:
                            # Making sure nothing is blocking our piece
                            #Moving up
                            if i - k == 3 and i + 1 <= 9 and i - 1 >= 0:
                                if self._set[i - 1][j] in self._blue_pieces or \
                                        self._set[i - 1][j] in self._red_pieces:
                                    return False
                                elif j - l == 2 and j + 1 <= 8 and j - 1 >= 0:
                                    if self._set[i - 2][j - 1] in self._blue_pieces or \
                                            self._set[i - 2][j - 1] in self._red_pieces:
                                        return False
                                elif j - l == -2 and j + 1 <= 8 and j - 1 >= 0:
                                    if self._set[i - 2][j + 1] in self._blue_pieces or \
                                            self._set[i - 2][j + 1] in self._red_pieces:
                                        return False
                            #Moving down
                            elif i - k == -3 and i + 1 <= 9 and i - 1 >= 0:
                                if self._set[i + 1][j] in self._blue_pieces or \
                                        self._set[i + 1][j] in self._red_pieces:
                                    return False
                                elif j - l == 2 and j + 1 <= 8 and j - 1 >= 0:
                                    if self._set[i + 2][j - 1] in self._blue_pieces or \
                                            self._set[i + 2][j - 1] in self._red_pieces:
                                        return False
                                elif j - l == -2 and j + 1 <= 8 and j - 1 >= 0:
                                    if self._set[i + 2][j + 1] in self._blue_pieces or \
                                            self._set[i + 2][j + 1] in self._red_pieces:
                                        return False
                            #Moving left
                            elif j - l == 3 and j + 1 <= 8 and j - 1 >= 0:
                                if self._set[i][j - 1] in self._blue_pieces or \
                                        self._set[i][j - 1] in self._red_pieces:
                                    return False
                                elif i - k == 2 and j + 1 <= 9 and j - 1 >= 0:
                                    if self._set[i + 1][j - 2] in self._blue_pieces or \
                                            self._set[i + 1][j - 2] in self._red_pieces:
                                        return False
                                elif i - k == -2 and j + 1 <= 9 and j - 1 >= 0:
                                    if self._set[i + 1][j + 2] in self._blue_pieces or \
                                            self._set[i + 1][j + 2] in self._red_pieces:
                                        return False
                            #Moving right
                            elif j - l == -3 and j + 1 <= 8 and j - 1 >= 0:
                                if self._set[i][j + 1] in self._blue_pieces or \
                                        self._set[i][j + 1] in self._red_pieces:
                                    return False
                                elif i - k == 2 and j + 1 <= 9 and j - 1 >= 0:
                                    if self._set[i + 1][j - 2] in self._blue_pieces or \
                                            self._set[i + 1][j - 2] in self._red_pieces:
                                        return False
                                elif i - k == -2 and j + 1 <= 9 and j - 1 >= 0:
                                    if self._set[i + 1][j + 2] in self._blue_pieces or \
                                            self._set[i + 1][j + 2] in self._red_pieces:
                                        return False

                            # Verify movement is in a valid direction, if true - move
                            if ((i + 3 == k or i - 3 == k) and (j + 2 == l or j - 2 == l)) or \
                                    ((i + 2 == k or i - 2 == k) and (j + 3 == l or j - 3 == l)):
                                return self.move_pieces(self._set[i][j], i, j, k, l)

                            else:
                                return False
                return False


    def move_horse(self, current, next,i,j):
        """Inputs: current location, next location, (i,j).
        Expected: output to move piece to next location, or return false for any other outcome"""
        if self._set[i][j] == 'RH' or self._set[i][j] == 'BH':
            if current == self._board[i][j]:
                for k in range(0, 10):
                    for l in range(0, 9):
                        if self._board[k][l] == next:
                            # Making sure nothing is blocking our piece
                            if i - k == 2 and i + 1 <= 9 and i - 1 >= 0:
                                if self._set[i - 1][j] in self._blue_pieces or \
                                        self._set[i - 1][j] in self._red_pieces:
                                    return False

                            elif i - k == -2 and i + 1 <= 9 and i - 1 >= 0:
                                if self._set[i + 1][j] in self._blue_pieces or \
                                        self._set[i + 1][j] in self._red_pieces:
                                    return False

                            elif j - l == 2 and j + 1 <= 8 and j - 1 >= 0:
                                if self._set[i][j - 1] in self._blue_pieces or \
                                        self._set[i][j - 1] in self._red_pieces:
                                    return False

                            elif j - l == -2 and j + 1 <= 8 and j - 1 >= 0:
                                if self._set[i][j + 1] in self._blue_pieces or \
                                        self._set[i][j + 1] in self._red_pieces:
                                    return False

                            # Verify movement is in a valid direction
                            if ((i + 2 == k or i - 2 == k) and (j + 1 == l or j - 1 == l)) or \
                                    ((i + 1 == k or i - 1 == k) and (j + 2 == l or j - 2 == l)):
                                return self.move_pieces(self._set[i][j], i, j, k, l)

                            else:
                                return False
                return False


    def move_palace_pieces(self,current,next,i,j):
        """Inputs: current location, next location, (i,j).
        Expected: output to move piece to next location, or return false for any other outcome"""
        #Making sure the palace pieces are being moved and moved only in the palace
        if current in self._red_palace:
            if next in self._red_palace:
                if self._set[i][j] == 'RG' or self._set[i][j] == 'RGe':

                    if current == self._board[i][j]:
                        for k in range(0, 10):
                            for l in range(0, 9):
                                if next == self._board[k][l]:
                                    if abs(i-k) == 1 or abs(j-l) == 1:
                                        return self.move_pieces(self._set[i][j],i,j,k,l)
                                    else:
                                        return False
                    return False

        elif current in self._blue_palace:
            if next in self._blue_palace:
                if self._set[i][j] == 'BG' or self._set[i][j] == 'BGe':
                    if current == self._board[i][j]:
                        for k in range(0, 10):
                            for l in range(0, 9):
                                if next == self._board[k][l]:
                                    if abs(i - k) == 1 or abs(j - l) == 1:
                                        return self.move_pieces(self._set[i][j],i,j,k,l)
                    return False
        return False

    def move_soldier(self,current,next,i,j):
        """Moves the soldier either forward or sideways, but not backwards"""
        for k in range(0, 10):
            for l in range(0, 9):
                if self._board[k][l] == next:
                    # moving a red soldier
                    if ((i + 1 == k and j == l) or (i == k and j - 1 == l) or \
                            (i == k and j + 1 == l)) and self._turn == 'red':
                        self.move_pieces(self._set[i][j], i, j, k, l)
                        return True

                    # Moving a blue soldier
                    elif ((i - 1 == k and j == l) or (i == k and j - 1 == l) or \
                            (i == k and j + 1 == l)) and self._turn == 'blue':
                        self.move_pieces(self._set[i][j], i, j, k, l)
                        return True

                    # Moving Diag in Palace
                    elif (next in self._red_palace or next in self._blue_palace) and \
                            (current in self._red_palace or current in self._blue_palace):
                        if (i + 1 == k and j + 1 == l) or (i + 1 == k and j - 1 == l) \
                                and self._turn == 'red':
                            self.move_pieces(self._set[i][j], i, j, k, l)
                            return True

                        elif (i - 1 == k and j + 1 == l) or (i - 1 == k and j - 1 == l) \
                                and self._turn == 'blue':
                            self.move_pieces(self._set[i][j], i, j, k, l)
                            return True

                        else:
                            return False
                    else:
                        return False





    def move_cannon(self,current,next,i,j):
        """Current is not used. Moves the cannon piece and makes sure only 1 piece exists between
        it and its target location. If there is another piece, cannon will not move."""
        for k in range(0, 10):
            for l in range(0, 9):
                if self._board[k][l] == next:
                    if i-k == 0:
                        #moves right
                        if l-j > 0:
                            for m in range(j+1,l):
                                if (self._set[i][m] in self._red_pieces or self._set[i][m] in self._blue_pieces)\
                                        and (self._set[i][m] != 'RCa' and self._set[i][m] != 'BCa'):
                                    #Cannons cannot jump over cannons
                                    for n in range(m+1,l):
                                        if (self._set[i][n] in self._red_pieces or self._set[i][n] in self._blue_pieces) \
                                                and (self._set[i][n] != 'RCa' and self._set[i][n] != 'BCa'):
                                            return False
                                    else:
                                        self.move_pieces(self._set[i][j], i, j, k, l)
                                        return True
                        #moves left
                        elif l-j < 0:
                            for m in range(l+1,j):
                                if (self._set[i][m] in self._red_pieces or self._set[i][m] in self._blue_pieces) \
                                        and (self._set[i][m] != 'RCa' and self._set[i][m] != 'BCa'):
                                    # Cannons cannot jump over cannons
                                    for n in range(m + 1, j):
                                        if (self._set[i][n] in self._red_pieces or self._set[i][n] in self._blue_pieces) \
                                                and (self._set[i][n] != 'RCa' and self._set[i][n] != 'BCa'):
                                            return False
                                    else:
                                        self.move_pieces(self._set[i][j], i, j, k, l)
                                        return True
                        else:
                            return False

                    elif j-l == 0:
                        # moves up
                        if i - k > 0:
                            for m in range(k+1,i):
                                if (self._set[m][j] in self._red_pieces or self._set[m][j] in self._blue_pieces) \
                                        and (self._set[m][j] != 'RCa' and self._set[m][j] != 'BCa'):
                                    # Cannons cannot jump over cannons
                                    for n in range(m + 1, i):
                                        if (self._set[n][j] in self._red_pieces or self._set[n][j] in self._blue_pieces) \
                                                and (self._set[n][j] != 'RCa' and self._set[n][j] != 'BCa'):
                                            return False
                                    else:
                                        self.move_pieces(self._set[i][j], i, j, k, l)
                                        return True
                        # moves down
                        elif i - k < 0:
                            for m in range(i + 1, k):
                                if (self._set[m][j] in self._red_pieces or self._set[m][j] in self._blue_pieces) \
                                        and (self._set[m][j] != 'RCa' and self._set[m][j] != 'BCa'):
                                    # Cannons cannot jump over cannons
                                    for n in range(m + 1, k):
                                        if (self._set[n][j] in self._red_pieces or self._set[n][j] in self._blue_pieces) \
                                                and (self._set[n][j] != 'RCa' and self._set[n][j] != 'BCa'):
                                            return False
                                    else:
                                        self.move_pieces(self._set[i][j], i, j, k, l)
                                        return True
                        else:
                            return False

                    #Moving diagonal in the palace
                    elif self._board[i][j] in self._red_palace or self._board[i][j] in self._blue_palace:
                        if j-l > 0:
                            #checking to make sure there is something between cannon and jump point
                            if self._set[i+1][j-1] in self._red_pieces or \
                                self._set[i+1][j - 1] in self._blue_pieces or \
                                self._set[i - 1][j - 1] in self._red_pieces or \
                                self._set[i - 1][j - 1] in self._blue_pieces:
                                self.move_pieces(self._set[i][j], i, j, k, l)
                                return True
                        elif j-l < 0:
                            if self._set[i+1][j + 1] in self._red_pieces or \
                                self._set[i+1][j + 1] in self._blue_pieces or \
                                self._set[i-1][j + 1] in self._red_pieces or \
                                self._set[i - 1][j + 1] in self._blue_pieces:
                                self.move_pieces(self._set[i][j], i, j, k, l)
                                return True
                        else:
                            return False
                    else:
                        return False
        return False


    def move_pieces(self,piece,i,j,k,l):
        """Helper function to move pieces. Uses array indexes to move"""

        if self._turn == 'blue':
            ally = self._blue_pieces
            enemy = self._red_pieces
        else:
            ally = self._red_pieces
            enemy = self._blue_pieces

        # So that player is not killing their own pieces
        if self._set[k][l] in ally:
            return False

        # Kills enemy
        elif self._set[k][l] in enemy:
            self._dead.append(self._set[k][l])
            self._set[i][j] = self._board[i][j]
            self._set[k][l] = piece
            return True
        # Just moves
        else:
            self._set[i][j] = self._board[i][j]
            self._set[k][l] = piece
            return True

if __name__ == "__main__":
    import numpy as np
    game = JanggiGame()
    print(np.array(game._set))
    ###Test 1###
    # print(game.make_move('e9','e8'))     #Blue: BGe move fwrd True
    # print(game.make_move('c4', 'b4'))     #Red: RS move left True
    # print(game.make_move('h8', 'd8'))  # Blue: BCa moves left True
    # print(game.make_move('e4', 'd4'))  # Red: RS move left True
    # print(game.make_move('f10', 'e9'))  # Blue: BG move fwrd True
    # print(game.make_move('d4', 'd4'))  # Red: skips
    # print(game.make_move('d8', 'f10'))  # Blue: BCa move back diag True
    # print(game.make_move('d4', 'd4'))  # Red: Skips
    # print(game.make_move('f10', 'f6'))  # Blue: BCa move fwrd False

    ###Test 2 ####
    # print(game.make_move('a1', 'a2'))   # red False
    # print(game.make_move('a10','a9'))   #blue True
    # print(game.make_move('a1', 'a2'))   #red True
    # print(game.make_move('a2', 'd2'))   #Blue moves red piece False
    # print(game.make_move('a9', 'c9'))   #blue True
    # print(game.make_move('b1', 'd4'))   # red True
    # print(game.make_move('b10', 'd7'))  # blue moves BE True
    # print(game.make_move('d4', 'a6'))   # red moves RE, but is blocked False
    # print(game.make_move('d4', 'f7'))   # red moves RE True
    # print(game.make_move('f7', 'd10'))  # red trys to move again False
    # print(game.make_move('c9', 'c8'))   # blue True
    # print(game.make_move('f7', 'd10'))  # red is blocked by piece diag False
    # print(game.make_move('c1', 'd3'))   # red horse moves True
    # print(game.make_move('d10', 'c10'))  # BG tries moving outside palace False
    # print(game.make_move('c10', 'd8'))  #blue moves BH True
    # print(game.make_move('f7', 'h4'))  # RE moves True
    # print(game.make_move('d10', 'c10'))  # BG tries moving outside palace False
    # print(game.make_move('e9', 'f8'))  # BGe moves diag True
    # print(game.make_move('h3', 'h5'))  # Red: RCa moves True
    # print(game.make_move('g7', 'g6'))  # Blue: BS moves fwrd True
    # print(game.make_move('g4', 'g5'))  # Red: RS moves fwrd True
    # print(game.make_move('d7', 'b4'))  # Blue: BE moves fwrd True
    # print(game.make_move('h5', 'a5'))  # Red: RCa moves left True
    # print(game.make_move('c7', 'c6'))  # Blue: BS moves fwrd True
    # print(game.make_move('i1', 'i2'))  # Red: RC moves fwrd True
    # print(game.make_move('c6', 'c5'))  # Blue: BS moves fwrd True
    # print(game.make_move('i2', 'f2'))  # Red: RC moves left True
    # print(game.make_move('f8', 'e8'))  # Blue: BGe moves left True
    # print(game.make_move('e4', 'd4'))  # Red: RS moves left True
    # print(game.make_move('e7', 'd7'))  # Blue: BS moves left False


    ###Test 3###
    # print(game.make_move('h10','g8'))    #Blue: move BS left TRUE
    # print(game.make_move('i4', 'h4'))  # Red: move RS down TRUE
    # print(game.make_move('h8', 'd8'))  # Blue: stays TRUE
    # print(game.make_move('h3', 'h9'))  # Red: move RS down TRUE
    # #print(game.make_move('f10', 'f9'))  # Blue: stays TRUE
    # # print(game.make_move('g5', 'g6'))  # Red: move RS down TRUE
    # # print(game.make_move('d7', 'd7'))  # Blue: stays TRUE
    # # print(game.make_move('g6', 'g7'))  # Red: move RS down and kills TRUE
    # # print(game.make_move('d7', 'd7'))  # Blue: stays TRUE
    # # print(game.make_move('g7', 'g8'))  # Red: move RS down TRUE
    # # print(game.make_move('d7', 'd7'))  # Blue: stays TRUE
    # # print(game.make_move('g8', 'f8'))  # Red: move RS left TRUE
    # # print(game.make_move('d7', 'd7'))  # Blue: stays TRUE
    # #print(game.make_move('f8', 'e8'))  # Red: move RS left TRUE
    # print(game.is_in_check('blue'))  # TRUE

    ###Test 4###
    # move_result = game.make_move('c1', 'e3')  # should be False because it's not Red's turn
    # move_result = game.make_move('a7', 'b7') #should return True
    # blue_in_check = game.is_in_check('blue')  # should return False
    # game.make_move('a4', 'a5')  # should return True
    # state = game.get_game_state()  # should return UNFINISHED
    # print(game.make_move('b7', 'b6'))  # should return True
    # print(game.make_move('b3', 'b6'))  # should return False because it's an invalid move
    # print(game.make_move('a1', 'a4'))  # should return True
    # print(game.make_move('c7', 'd7'))  # should return True
    # print(game.make_move('a4', 'a4'))  # this will pass the Red's turn and return True

    ###Test 5###
    # print(game.make_move('d10', 'd9'))  # Blue: move BG fwrd TRUE
    # print(game.make_move('b1', 'd4'))  # Red: move RE fwrd TRUE
    # print(game.make_move('e9', 'd10'))  # Blue: move BG fwrd TRUE
    # print(game.make_move('d4', 'b7'))  # Red: move RE fwrd TRUE
    # print(game.make_move('b8', 'b6'))  # Blue: move BG fwrd TRUE

    ###Test 6### Blue in check
    game.make_move('c7', 'c6') #Blue
    game.make_move('c1', 'd3') #Red
    game.make_move('b10','d7') #Blue
    game.make_move('b3', 'e3') #Red
    game.make_move('c10', 'd8') #Blue
    game.make_move('h1', 'g3') #Red
    game.make_move('e7', 'e6') #Blue
    game.make_move('e3', 'e6') #Red
    print(game.is_in_check('red'))  # True
    print(game.is_in_check('blue'))  # False

    game.make_move('h8', 'c8') #Blue
    game.make_move('d3', 'e5') #Red
    game.make_move('c8', 'c4') #Blue
    print(game.is_in_check('red'))  # True
    print(game.is_in_check('blue'))  # False
    game.make_move('e6', 'e6')  # Red
    game.make_move('g7', 'f7')  # Blue
    game.make_move('e6', 'e6')  # Red
    game.make_move('f7', 'e7')  # Blue
    print(game.is_in_check('blue'))  # False
    game.make_move('e7', 'e7')  # Blue
    game.make_move('e6', 'e9')  # Red
    print(game.make_move('e7', 'e7'))  # Blue
    #
    # game.make_move('e5', 'c4')
    # game.make_move('i10', 'i8')
    # game.make_move('g4', 'f4')
    # game.make_move('i8', 'f8')
    # game.make_move('g3', 'h5')
    # game.make_move('h10', 'g8')
    # game.make_move('e6', 'e3')

    ###Test 7### Red in check
    # game.make_move('c7', 'c6')
    # game.make_move('e4', 'f4')
    # game.make_move('b1', 'd7')
    # game.make_move('d1','d2')
    # game.make_move('c1', 'c9')
    # game.make_move('i1','i8')
    # game.make_move('e2','f2')
    # game.make_move('g7','h7')
    # game.make_move('h3','h5')
    # game.make_move('c1','e2')
    # game.make_move('i7','i6')
    # game.make_move('g1','e4')
    # game.make_move('i6','h6')
    # game.make_move('e4','b6')
    # game.make_move('a1','a8')
    # game.make_move('e2','d4')
    # game.make_move('c6','b6')
    # game.make_move('i4','i5')
    # game.make_move('b8','b5')
    # game.make_move('d4','e4')
    # game.make_move('d2','d1')
    # game.make_move('h6','i6')
    # game.make_move('f2','f2')
    # game.make_move('a8','c8')
    # game.make_move('d1','e1')
    # game.make_move('c8','c4')
    # game.make_move('g4','g5')
    # game.make_move('b6','c6')
    # game.make_move('e1','d1')
    # game.make_move('i6','i5')
    # game.make_move('a1','a2')
    # game.make_move('d7','f4')
    # game.make_move('a4','b4')
    # game.make_move('f4','d1')
    # game.make_move('a2','a7')

    # print(game.is_in_check('blue'))  # True
    # print(game.is_in_check('red'))  # False
    print(game._dead)
    print(game.get_game_state())
    print(np.array(game._set))