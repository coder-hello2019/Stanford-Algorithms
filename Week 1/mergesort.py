# Merge sort implementation, done for practice

def mergesort(unsorted):
    # base case - if the list has only 1 element, it is sorted
    if len(unsorted) <= 1:
        return unsorted

    # recursive case
    else:
        # use // so that we can deal with uneven numbers of lists
        midpoint = len(unsorted) // 2
        # split the list into 2 sections and call mergesort on those
        left = unsorted[:midpoint]
        right = unsorted[midpoint:]
        print(left, right)

        # then merge the sorted sub-lists
        sortedLeft = mergesort(left)
        sortedRight = mergesort(right)

        sorted = []

        # merge the sorted sub-lists
        # what do we do when one list runs out before the other?
        for i in range(len(unsorted)):
            if len(sortedLeft) == 0:
                sorted.extend(sortedRight)
                break
            elif len(sortedRight) == 0:
                sorted.extend(sortedLeft)
                break
            elif sortedLeft[0] <= sortedRight[0]:
                sorted.append(sortedLeft[0])
                sortedLeft = sortedLeft[1:]
            else:
                sorted.append(sortedRight[0])
                sortedRight = sortedRight[1:]

        return sorted

print(mergesort([5,6,3,1,5]))
print(mergesort([94, 34231, 4, 6837, 45, 34]))
print(mergesort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(mergesort([]))
print(mergesort([1,1,1,1,1,1]))
