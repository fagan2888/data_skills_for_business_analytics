
def Q1_seasons():
    x  = input()
    print("Enter Month Name:")
    s1 = ["December","January","February"]
    s2 = ["March","April", "May",]
    s3 = ["June","July","August"]
    s4 = ["September","October","November"]
    if x in s1:
        print("Season: Winter")
    if x in s2:
        print("Season: Spring")
    if x in s3:
        print("Season: Summer")
    if x in s4:
        print("Season: Autumn")


def Q2_mulitples():
    num = 3
    for x in range(13,-1,-1):
        print(x*num)


def Q3_nested_loop():
    lst = [5,4,3,2,1,0]
    for x in range(1,6):
        print(" "*lst[x]*2,end="")
        for y in range(x,0,-1):
            print(y,end=" ")
        print(" "*x,end="\n\n")
        
def Q4_printing():
    for num in range(0,11):
        if num != 3 and num != 6:
            print(num, end=" ")

def Q5_sum_avg():
    print("Enter Numbers: \nEnter 'f' to Stop! \n")
    lst = []
    f,sum = 0,0
    while (f != 1):
        x = input()
        if x == "f":
            f += 1
        else:
            try:
                lst.append(int(x))
            except:
                print("Try Again!")
    for num in lst:
        sum += num
    print("\nSum: ",sum)
    print("Avg: ",(sum/len(lst)))

Q5_sum_avg()