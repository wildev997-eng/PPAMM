def chessboard(x):
    y = 0
    while y < x:
        y+=1
        z=0
        while z < x:
            z+=1
            if z % 2 == 0 and y % 2 != 0:
                print("O", end="")
            elif z % 2 != 0 and y % 2 == 0:
                print("O", end="")
            else:
                print("X", end="")
        print() 

chessboard(3)