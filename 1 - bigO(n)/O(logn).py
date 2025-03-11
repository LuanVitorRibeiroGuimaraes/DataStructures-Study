# base 2³ = 8
# log 8 = 3
# how many times to multiply 2 to give 8
# how many times you have to take the number eight and divide it by two

def binarySearch (list, item):
    first = list[0]
    last = len(list) - 1

    while (first <= last):
        mid = (first + last) // 2
        attempt = list[mid]

        if attempt == item:
            return mid
        if attempt > item:
            print("too higher!")
            last = mid - 1
        else:
            print("too lower!")
            first = mid + 1
    
    return None

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print(binarySearch(my_list, 2))