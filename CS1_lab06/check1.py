bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

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
        