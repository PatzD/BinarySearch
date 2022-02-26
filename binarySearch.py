import random

inp1 = int(input("max arr size "))
inp2 = int(input("max number in arr "))
inp3 = int(input("what number to search for "))

#generating a random array of numbers
arr = []
def random_sorted_list(size, max_num):

    for n in range(size):
        temp = random.randint(0, max_num)
        arr.append(temp)

    arr.sort()
    return arr

def binary_search(arr, num_search):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < num_search:
            low = mid + 1
        elif arr[mid] > num_search:
            high = mid - 1
        else:
            return mid

    return "not found"

sorted_array = random_sorted_list(inp1, inp2)
print(sorted_array)
print(f"number at index {binary_search(sorted_array, inp3)}")