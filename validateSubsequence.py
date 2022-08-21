#Given two non-empty arrays of integers, 
# Write a function that determins whether the second array is a subsequence of the first one
# O(n) time
# O(1) space
def validateSubsequence(array, sequence):
    arrIndex = 0
    sequenceIndex = 0
    while (arrIndex < len(array) and sequenceIndex < len(sequence)):
        if array[arrIndex] == sequence[sequenceIndex]:
            sequenceIndex += 1
        arrIndex += 1
    return sequenceIndex == len(sequence)

# O(n) time
# O(1) space
def validateSubsequenceTwo(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence) 


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

print(validateSubsequence(array, sequence))
print(validateSubsequenceTwo(array, sequence))
