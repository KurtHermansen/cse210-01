

def main():
    print('Lets play Tic Tac Toe!')
    player = nextPlayer('')
    width = int(input('What size of board do you want to play tic tacktoe on?\n(2 =2x2, 3 =3x3, 4 =4x4, 5 =5x5)'))
    split = width - 1
    totalMoves = width * width
    spaces = boardSize(width)
    #board = buildBoard(spaces, split, width)
    #print(board)
    # 
    while not (winnerRow(spaces, width) or winnerColumn(spaces, width) or winnerCross(spaces, width) or draw(spaces, totalMoves)):
        buildBoard(spaces, split, width)
        playMove(spaces, player)
        player = nextPlayer(player)
    buildBoard(spaces, split, width)
    print('game oveer')


def boardSize(width):

    board = []
    for space in range(width * width):
        board.append(space + 1)
    return board

def buildBoard(spaces, split, width):
    start = '---+'
    end = '---'
    digit = 1
    if width > 3:
        start = '----+'
        end = '----'
        digit = 2
    add = ''
    
    index = 0
    for i in range(split):               

        add = start + add
        add = add
    divide = add + end
    for i in range(width):
        if i == 0 or i == width:
            print()
        else:
            print()
            print(divide)
        for c in range(width):
            print(f' {spaces[index]:{digit}} |', end="")
            index += 1
    return ''
def winnerRow(space, width):
    row = []    
    for columns in range(width):
        checkX = 0 
        checkY = 0
        for i in range(width):
            row.append(str(space[i + (columns * width)]))
        for x in row:
            if "x" in x:
                checkX += 1
                if checkX == width:
                    print('Row Win!')
                    return True
        for o in row:
            if "o" in o:
                checkY += 1
                if checkY == width:
                    print('Row Win!')
                    return True
        row.clear()
    # index = 0
    # endRow = len(space)
    # for column in range(width):
    #     for row in range(width -1):
    #         if space[index] != space[index + 1]:
    #             index +=1
    #             if row >= (width-2) and column >= (width -1):
    #                 return False
    #         if index + 1 == endRow - (endRow - ((row+1)*width)) and space[index] == space[index + 1]:
    #             print('Row Win!')
    #             return True
    #     index += 1
    # # return True
def winnerColumn(space, width):
    column = [] 
    for row in range(width):
        checkX = 0 
        checkY = 0
        for i in range(width):
            column.append(str(space[row + (i * width)]))
        for x in column:
            if "x" in x:
                checkX += 1
                if checkX == width:
                    print('Column Win!')
                    return True
        for o in column:
            if "o" in o:
                checkY += 1
                if checkY == width:
                    print('Column Win!')
                    return True
        column.clear()
#     endColumn = len(space)
#     startColum = 0
#     for row in range(width):        
#         columnIndex = 0
#         for column in range(width -1):                        
#             if space[columnIndex + startColum] != space[columnIndex + startColum + width]:
#                 if column >= (width - 2) and row >= (width-1):
#                     return False
#             elif columnIndex + startColum + width == endColumn + startColum - width and space[columnIndex + startColum] == space[columnIndex + startColum + width]:
#                 print('Column Win!')
#                 return True
#             columnIndex += width
#         startColum += 1
#     # return True
def winnerCross(space, width):
    if width == 5:
        if space[0] == space[6] == space[12] == space[18] == space[24] or space[4] == space[8] == space[12] == space[16] == space[20]:
            print('Diagonal Win')
            return True
    elif width == 4:
        if space[0] == space[5] == space[10] == space[15] or space[3] == space[6] == space[9] == space[12]:
            print('Diagonal Win')
            return True
    elif width == 3:
        if space[0] == space[4] == space[8] or space[2] == space[4] == space[6]:
            print('Diagonal Win')
            return True
    elif width == 2:
        if space[0] == space[3] or space[1] == space[2]:
            print('Diagonal Win')
            return True
    else:
        return False

    # startColum = 0
    # for row in range(width):        
    #     columnIndex = 0
    #     for column in range(width -1):                        
    #         if space[columnIndex + startColum] != space[columnIndex + startColum + width]:
    #             if column >= (width - 2) and row >= (width-1):
    #                 return False
    #         columnIndex += width
    #     startColum += 1
    # return True

            
def draw(space, length):
    for value in range(length):
        if space[value] != "x" and space[value] != "o":
            return False
    return True
def nextPlayer(current):
    if current == '' or current == 'o':
        return 'x'
    elif current == 'x':
        return 'o'
        


def playMove(space, player):
    print()
    move = int(input(f'Player {player} pick an open space on the game board. 1-{len(space)}.'))
    space[move -1] = player

if __name__ == "__main__":
    main()          