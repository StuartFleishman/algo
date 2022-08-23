

def nonConstructibleChange(array): 
  min = 1
  max = maxSum(array)
  
return min



def maxSum(array):
    totalSum = 0
    for num in range(len(array)):
        totalSum += array[num]
    return totalSum


array = [5, 7, 1, 1, 2, 3, 22]
print(maxSum(array))
