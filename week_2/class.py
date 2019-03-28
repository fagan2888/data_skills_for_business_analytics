import calendar

def birthday():
    print("Enter Your Birthdate")
    month = int(input("Input Month:   "))
    day = int(input("Input Day:     "))
    year = int(input("Input Year:    "))
    print("You were born on", calendar.month_name[month], day,",", year)
    
def median():
    print("Enter Your Space Seperate List")
    x = sorted([float(num) for num in input().split()])
    print("Sorted:  ", x)
    if len(x)%2 == 0: 
        a = float(x[int(len(x)/2)])
        b = float(x[int(len(x)/2) - 1])
        y = (a + b) / 2
        print("Median:  ", y)
    else:
        print("Median:  ", x[int(len(x)/2)])

def computation():
    n = int(input())
    result = (n*n)+(2*n)+1
    print(result)

def arithmetic():
    print("Enter Your Desired Values")
    X = int(input("X Value:  "))
    Y = int(input("Y Value:  "))
    result = (X+Y)/(X-Y)
    print("Calculation:  ", result)

