# 0(nLogn) time
# O(n) space
def sortedSquaredArray(array):
    s = [0 for _ in array]

    for idx in range(len(array)):
        value = array[idx]
        s[idx] = value * value
    s.sort()
    return s


#O(n) time
#O(n) space
def sortedSquaredArrayTwo(array):
    sortedSqr = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSqr[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSqr[idx] = largerValue * largerValue
            largerValueIdx -= 1
    return sortedSqr


array = [1, 4, 5]
print(sortedSquaredArray(array))
print(sortedSquaredArrayTwo(array))
