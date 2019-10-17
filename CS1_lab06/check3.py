import lab06_util

bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

def print_sudoku(bd):
    row = len(bd)
    col = len(bd[0])
    print("-"*25)
    for i in range(0, row):
        for j in range(0, col):
            if(j % 3 == 0):
                print("|", end=" ")
            print(bd[i][j], end =" ")
        print("|",end=" ")
        print("") 
        if((i+1) % 3 == 0):
            print("-"*25)

def ok_to_add(row,col,num,bd):
    #Check validity
    can_add = True
    if (0 <= row < len(bd) and 0 <= col < len(bd[0]) and int(num) in range(1,10)):    
        #Check 1
        for x in range(len(bd[row])):
            if bd[x] == num and x != col:
                can_add = False
        
        #Check 2
        for i in range(len(bd)):
                if bd[i][col] == num and i != row:
                    can_add = False
        
        #Check 3
        start_row = (row//3)*3
        end_row = start_row + 3
        start_col = (col//3)*3
        end_col = start_col + 3
    
        for x in range(start_row,end_row):
            for y in range(start_col,end_col):
                if bd[x][y] == num and x != row and y != col:
                    can_add = False
    else:
        can_add = False
    return can_add

def verify_board(bd):
    if_solved = True
    for i in range(len(bd)):
        for j in range(len(bd[0])):
            if bd[i][j] == '.':
                if_solved = False
                break
            else: 
                if ok_to_add(i, j, bd[i][j], bd) == False:
                    if_solved = False
                    break
    return if_solved


filename=input("Input the file you want to open => ")
bd=lab06_util.read_sudoku(filename)

print_sudoku(bd)


while not verify_board(bd):
    input_row = int(input("Enter a row => "))
    input_col = int(input("Enter a column => "))
    input_num = input("Enter a number => ")
    
    if (bd[input_row][input_col] != '.'):
        print("can not be added here")
    elif ok_to_add(input_row, input_col, input_num, bd):
        bd[input_row][input_col]=input_num
    else:
        print("Not Satisfied Now",end="\n\n")
    print_sudoku(bd)

print("Finished ! Well Done !")