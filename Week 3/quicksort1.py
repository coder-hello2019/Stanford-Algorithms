"""
Implementation of quicksort for week 3 of Stanford's algorithms course, which also counts the number of comparison in the given quicksort iteration.
In this iteration (for part 1 of pset 3), the pivot is always the first element of the unsorted array.
"""

import random

def quicksort(unsorted):

    if len(unsorted) <= 1:
        return (unsorted, 0)

    pivot = unsorted[0]

    #initiate i,j to the first array element which isn't the pivot
    i = 1

    counter = len(unsorted) - 1

    # look at each element in the array except for the pivot and partition the array
    for j in range (1, len(unsorted)):
        #print(f"Current i and j: {i}, {j}")
        if unsorted[j] > pivot:
            # we don't need to do anything other than advancing the j pointer
            pass
        # need to swap the jth element with the last element in the 'less than pivot' portion of the list and advance the i pointer
        elif unsorted[j] < pivot:
            unsorted[i], unsorted[j] = unsorted[j], unsorted[i]
            i += 1

    # put pivot in the correct place in the list by swapping the pivot with the last element of the 'smaller than pivot list'
    unsorted[i - 1], unsorted[0] = unsorted[0], unsorted[i - 1]

    # section of array with nums less than pivot
    leftList = unsorted[0:i - 1]
    # section of array with nums greater than pivot
    rightList = unsorted[i:]

    # call function recursively on the partitioned portions of the list
    # i think the prob here is that we're calling this on copies of the list as opposed to doing the partitioning sub-routine on the same list
    left = quicksort(leftList)
    right = quicksort(rightList)

    counter += left[1]
    counter += right[1]

    leftList = left[0]
    rightList = right[0]

    sorted = []
    sorted.extend(leftList)
    sorted.append(pivot)
    sorted.extend(rightList)

    """
    if len(sorted) == 10:
        print(f"Sorted array: {sorted}")
        print(f"Counter: {counter}")
    """

    return (sorted, counter)

# function to generate test lists
def testGenerator():
    list = []

    while len(list) < 10:
        randomNum = random.randrange(0, 100)
        if randomNum not in list:
            list.append(randomNum)

    return list


"""
Testcases
test1 = [3,6,7,2,1]
test2 = testGenerator()
print(f"Test2: {test2}")
"""

def main():

    qfile = open("quicksort.txt", "r")
    numsList = []

    for item in qfile.read().splitlines():
        numsList.append(int(item))

    qfile.close()
    print(quicksort(numsList))

main()
