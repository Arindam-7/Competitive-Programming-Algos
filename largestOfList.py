# python program to find the largest number from a list

def largestOfList ( list ):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max

largest = largestOfList([1, -7, 39, 69])
print(largest)