# Name: Nathan Thompson
# OSU Email: thomnath@oregonstate.edu
# Course:       CS261 - Data Structures
# Assignment: Assignment 1
# Due Date: 04/18/2022
# Description: Implementation of 10 basic functions in O(n) time as Python review


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple:
    """
    Reads each element of an array of a given size, and returns a tuple of the minimum and maximum values.
    """
    min, max = arr.get(0), arr.get(0)
    for num in range(1, arr.length()):
        if arr.get(num) < min:
            min = arr.get(num)
        if arr.get(num) > max:
            max = arr.get(num)
    return (min, max)


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Function that determines in a number is divisible by 3, by 5, or by 15,
    and prints statements to the screen accordingly.
    """
    fizzy_arr = StaticArray(arr.length())
    for num in range (arr.length()):
        if arr.get(num) % 15 == 0:
            fizzy_arr.set(num, "fizzbuzz")
            num += 1
        elif arr.get(num) % 5 == 0:
            fizzy_arr.set(num, "buzz")
            num += 1
        elif arr.get(num) % 3 == 0:
            fizzy_arr.set(num, "fizz")
            num += 1
        else:
            fizzy_arr.set(num, arr.get(num))
            num += 1
    return fizzy_arr

# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    Function that reverses the order of the array.
    """
    x = 0
    y = arr.length() - 1
    while y >= (arr.length() // 2):
        m = arr.get(x)
        n = arr.get(y)
        arr.set(x, n), arr.set(y, m)
        x += 1
        y -= 1

# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    'Rotates' each value in an array by the specified value.

    :param arr: StaticArray object
    :param steps: number of 'steps' by which the index of each array value is moved

    :returns: new StaticArray object
    """
    arr_len = arr.length()
    rotated = StaticArray(arr_len)
    # Find the actual number of steps we need to move the values in order to satisfy the 'steps' parameter
    rotations = steps - ((steps//arr_len) * arr_len)
    x = 0
    while x < arr.length():
        new_arr_index = x + rotations
        # extra step if we 'fall off' the end of the array
        if new_arr_index > arr_len - 1:
            new_arr_index = abs(arr_len - (new_arr_index))
        rotated.set(new_arr_index, arr.get(x))
        x += 1
    return rotated


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    Creates a new Static Array instance that contains all integers from start to end, inclusive

    :param start: The first value of the new array
    :param end: The final value of the new array

    :returns: A new StaticArray object with the values from start to end
    """
    new_arr = StaticArray(abs(end-start)+1)
    index_num = 0
    if start < end:
        while index_num < new_arr.length():
            new_arr.set(index_num, start)
            index_num += 1
            start += 1
    elif start > end:
        while index_num < new_arr.length():
            new_arr.set(index_num, start)
            index_num += 1
            start -= 1
    else:
        new_arr.set(0, start)
    return new_arr


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    Checks elements in an array, and returns -1 if the array is sorted in descending order, 1 if sorted in ascending
    order, and 0 otherwise

    :param arr: StaticArray object

    :returns: Values -1, 0, or 1, depending on result
    """
    # Initialize a variable to that will hold the value to be returned
    x = 1
    # Check if there is only one element in the array
    if arr.length() == 1:
        return x
    # Check if 2nd element is smaller than the first- if so, check that the remaining elements are in descending order
    elif arr.get(0) > arr.get(1):
        for num in range(1, arr.length()):
            if arr.get(num-1) <= arr.get(num):
                return 0
        return -1

    # Check if 2nd element is greater than the first- if so, check that the remaining elements are in ascending order
    elif arr.get(0) < arr.get(1):
        for num in range(1, arr.length()):
            if arr.get(num-1) >= arr.get(num):
                return 0
    return x


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple:
    """
    Evaluates the values in an array and returns the mode and its frequency

    :param arr: StaticArray object

    :returns: Tuple of (mode: int, frequency: int)
    """
    # Set temporary variables to be updated as we traverse the StaticArray
    if arr.length() == 1:
        return (arr.get(0), 1)
    the_mode, the_freq, x, y = 0, 1, 1, 1
    while x < arr.length():
        while arr.get(x) == arr.get(x-1):
            y += 1
            x += 1
            if y > the_freq:
                the_freq = y
                the_mode = arr.get(x-1)
            # Stop if we've hit the end
            if x >= arr.length():
                return (the_mode, the_freq)
        x += 1
        y = 1
        if the_mode == 0:
            the_mode = arr.get(0)
    return (the_mode, the_freq)


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Creates a new array from the unique values of the given sorted array

    :param arr: StaticArray object

    :returns: new StaticArray object
    """
    size_arr = arr.length()
    for num in range(size_arr-1):
        if arr.get(num+1) == arr.get(num):
            size_arr -= 1
    # Second traverse: set new StaticArray to correct size & build the new array
    index_new, index_old = 0, 1
    new_arr = StaticArray(size_arr)
    # Initial value will always be added to the new array
    new_arr.set(index_new, arr.get(0))
    while index_old < arr.length():
        if new_arr.get(index_new) != arr.get(index_old):
            new_arr.set(index_new + 1, arr.get(index_old))
            index_new += 1
        index_old += 1
    return new_arr


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    Creates a new array with the same elements, but sorted in descending order.
    Unfortunately it's n*k and takes a long time.

    :param arr: Original, unsorted array which may or may not contain duplicates

    :returns: A new array containing all elements of the original array, but sorted in descending order
    """
    # Create an array of all values within the max range of the original array
    range_vals = min_max(arr)
    if range_vals[1] <= 0:
        range_arr = sa_range(0, abs(range_vals[0]))
    else:
        range_arr = sa_range(0, range_vals[1])
    new_arr = StaticArray(arr.length())
    # If there are negative values, we need two count arrays; otherwise, just one
    if range_vals[0] > 0 or range_vals[1] <= 0:
        count_arr = StaticArray(range_arr.length() + 1)
        # Set all count array to 0 instead of None
        for num in range(count_arr.length()):
            count_arr.set(num, 0)
        # Adds 1 for each instance of the value encountered - each value has an index in the count array
        for num in range(arr.length()):
            now_count = count_arr.get(abs(arr.get(num)))
            count_arr.set(abs(arr.get(num)), now_count + 1)
        # Loops through the count array to fill the new array
        new_arr_index = 0
        for num in range(count_arr.length()):
            x = count_arr.get(num)
            while x > 0:
                new_arr.set(new_arr_index, num)
                new_arr_index += 1
                x -= 1
        if (range_vals[0] < 0 and range_vals[1] <= 0):
            for num in range(new_arr.length()):
                new_arr.set(num, (new_arr.get(num) * -1))
    else:
        poz_count_arr = StaticArray(abs(range_vals[1] + 1)) # this is where we are having problems with arr size
        neg_count_arr = StaticArray(abs(range_vals[0]) + 1)
        # Set all count array to 0 instead of None
        for num in range(neg_count_arr.length()):
            neg_count_arr.set(num, 0)
        for num in range(poz_count_arr.length()):
            poz_count_arr.set(num, 0)
        # Adds 1 for each instance of the value encountered - each value has an index in the count array
        for num in range(arr.length()):
            if arr.get(num) >= 0:
                now_count = poz_count_arr.get(arr.get(num))
                poz_count_arr.set(arr.get(num), now_count + 1)
        for num in range(abs(range_vals[0])):
            if arr.get(num) < 0:
                now_count = neg_count_arr.get(abs(arr.get(num)))
                neg_count_arr.set(abs(arr.get(num)), now_count + 1)
        # Loops through the count array to fill the new array
        new_arr_index = 0
        neg_ind = neg_count_arr.length()-1
        while neg_ind >= 0:
        #for num in range(neg_count_arr.length()):
            x = neg_count_arr.get(neg_ind)
            while x > 0:
                new_arr.set(new_arr_index, (neg_ind * -1))
                new_arr_index += 1
                x -= 1
            neg_ind -= 1
        for num in range(poz_count_arr.length()):
            x = poz_count_arr.get(num)
            while x > 0:
                new_arr.set(new_arr_index, num)
                new_arr_index += 1
                x -= 1
    reverse(new_arr)
    return (new_arr)


# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    Returns a new array, in ascending order, of the squares of the given array's elements

    :param arr: Given array (sorted in any order)

    :returns: New sorted array of squares, ascending
    """
    sq_arr = StaticArray(arr.length())
    if (arr.get(0) < 0) ^ (arr.get(arr.length()-1) < 0):
        # Loop thru till we find a pivot index point
        pivot = 0
        for num in range(1, arr.length()):
            if arr.get(num) == 0 or (arr.get(num) < 0 and (num > 0 and (arr.get(num - 1) > 0)) or (arr.get(num) > 0 and arr.get(num + 1) < 0)):
                pivot = num
        # Since the pivot is the "threshold" value, all other values square will be over zero (larger).
        if pivot < arr.length() - 1:
            sq_arr.set(0, arr.get(pivot)**2)
        # Set temp variable to compare absolute value of each side of the pivot point, then compare
        r = pivot + 1
        l = pivot - 1
        index = 1
        while (l > 0) and (r < arr.length()):
            if abs(arr.get(l)) == abs(arr.get(r)):
                sq_arr.set(index, arr.get(r)**2)
                index += 1
                sq_arr.set(index, arr.get(r) ** 2)
                index += 1
                r += 1
                l -= 1
            elif abs(arr.get(l)) > abs(arr.get(r)):
                sq_arr.set(index, arr.get(r)**2)
                index += 1
                sq_arr.set(index, arr.get(l) ** 2)
                index += 1
                r += 1
                l -= 1
            else:
                sq_arr.set(index, arr.get(l)**2)
                index += 1
                sq_arr.set(index, arr.get(r) ** 2)
                index += 1
                r += 1
                l -= 1
        # If 'l' is equal to zero, we can't go any further on the left hand side
        if l == 0:
            for num1 in range(r-1, arr.length()):
                sq_arr.set(num1, arr.get(num1)**2)
        if r == arr.length():
            sq_arr.set(0, arr.get(0) ** 2)
            for num2 in range(index, arr.length()):
                sq_arr.set(num2, arr.get(num2)**2)
        if sq_arr.get(0) > sq_arr.get(arr.length() - 1):
            reverse(sq_arr)
        return sq_arr
    # If no negative values are found, we can just return the array, squared
    for num in range(arr.length()):
        sq_arr.set(num, (arr.get(num)**2))
    # Check to see if final array is in ascending order. If not, call reverse function
    if sq_arr.get(0) > sq_arr.get(arr.length()-1):
        reverse(sq_arr)
    return sq_arr


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":
    '''
    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    print(f"Min: {result[0]: 3}, Max: {result[1]: 3}")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    print(f"Min: {result[0]}, Max: {result[1]}")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        print(f"Min: {result[0]: 3}, Max: {result[1]}")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        mode, frequency = find_mode(arr)
        print(f"{arr}\nMode: {mode}, Frequency: {frequency}\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1],
        [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3],
        [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998],
        [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)
'''
    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
