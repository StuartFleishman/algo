# Write a function that take in a non-empy array of distinct integers and an interger representing a targetsum.
# If any two number in the input array sum up to the target sum, the function should return them in an array, in any order
# If no two numbers sum up to the target sum, the function should return an empty array

array = [-1, 3, 4, 11]
targetSum = 10

# O(n ^2) time
# 0(1) space


def twoNumberSumFirst(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
        if firstNum + secondNum == targetSum:
            return [firstNum, secondNum]
    return []


# 0(n) time
# 0(n) space
def twoNumberSumSecond(array, targetSum):
    nums = {}
    for num in array:
        potentailMatch = targetSum - num
        if potentailMatch in nums:
            return [potentailMatch, num]
        else:
            nums[num] = True
    return []


#O(nLog(n)) time
#O(1) space
def twoNumerSumThird(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
      currentSum = array[left] + array[right]
      if currentSum == targetSum:
          return [array[left], array[right]]
      elif currentSum < targetSum:
            left += 1
      elif currentSum > targetSum:
            right -= 1
    return []


print(twoNumberSumFirst(array, targetSum))
print(twoNumberSumSecond(array, targetSum))
print(twoNumerSumThird(array, targetSum))
