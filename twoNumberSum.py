# Write a function that take in a non-empy array of distinct integers and an interger representing a targetsum. 
# If any two number in the input array sum up to the target sum, the function should return them in an array, in any order
# If no two numbers sum up to the target sum, the function should return an empty array

array = [-1, 3, 4, 11]
targetSum = 10

# O(n ^2) time
# 0(1) space
def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
        if firstNum + secondNum == targetSum:
            return [firstNum, secondNum]
    return []


print(twoNumberSum(array, targetSum))
