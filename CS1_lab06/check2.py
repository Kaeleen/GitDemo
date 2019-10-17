bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

def print_sudoku():
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

def ok_to_add(row,col,num):
    can_add = True
    #Check validity
    if (0 <= row < len(bd) and 0 <= col < len(bd[0]) and int(num) in range(1,10)):    
        #Check 1
        for x in bd[row]:
            if x == num:
                can_add = False
    
        #Check 2
        for i in range(len(bd)):
            if bd[i][col] == num:
                can_add = False
    
        #Check 3
        start_row = (row//3)*3
        end_row = start_row + 3
        start_col = (col//3)*3
        end_col = start_col + 3
    
        for x in range(start_row,end_row):
            for y in range(start_col,end_col):
                if bd[x][y] == num:
                    can_add = False
    
        #Check 4
        if bd[row][col] != ".":
            can_add = False
    
        #Get Conclusion
        if can_add == True:
            bd[row][col]=num
            print_sudoku()
        else:
    
            print("This number cannot be added")
    #once invalid
    else:
        print("This number cannot be added") 

input_row = int(input("Enter a row => "))
input_col = int(input("Enter a column => "))
input_num = input("Enter a number => ")
    
ok_to_add(input_row,input_col,input_num)
