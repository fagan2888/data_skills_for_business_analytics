

def min_max_avg(lst = [3,10,7,5,6]):
    min, max, sum = float('inf'), 0, 0
    for i in lst:
        if i > max:
            max = i
        if i < min:
            min = i
        sum += i
    average = sum / len(lst)
    print(f"Average = {average}")
    print(f"Minimum = {min}")
    print(f"Maximum = {max}")

min_max_avg()
