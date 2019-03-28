def minimum(x,y,z):
    min = float("inf")
    for num in [x,y,z]:
        if num < min:
            min = num
    return min

# print(minimum(1,2,3))








def trinomial_algo(row,col):
    if row == 0 and col == 0: 
        return 1
    if col < -row or col > row: 
        return 0
    upLeft  = trinomial_algo(row - 1, col - 1)
    up      = trinomial_algo(row - 1, col)
    upRight = trinomial_algo(row - 1, col + 1)
    return upLeft + up + upRight

def Q1_trinomial_triangle():
    n = int(input("Enter Row Count: "))
    lst = []
    for val in range(n,0,-1):
        lst.append(val)
    for row in range(n):
        print("     "* lst[row],end="")
        for col1 in range(-row,1):
            x = trinomial_algo(row,col1)
            print("{:4d}".format(x), end=" ")
        for col2 in range(1,row+1):
            x = trinomial_algo(row,col2)
            print("{:4d}".format(x), end=" ")
        print("")

Q1_trinomial_triangle()

  