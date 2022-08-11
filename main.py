# A “binary list” is a list containing only 0s and 1s. For example, [0, 1, 0, 0, 1] is a binary list. 
# A “sorted binary list” (in ascending order for this problem) is a binary list such that no 1s are ever followed by 0s. 
# For example, [0, 0, 0, 1, 1] is a sorted binary list. 
# Given a sorted binary list containing n elements, we can determine the number of 0s as follows:

# 	Algorithm count_0s(nums):
# 		For i from 0 to |nums|-1:  # using 0-based indexing
# 			If nums[i] is 1:
# 				Return i + 1
# 		Return |nums|

# However, for a list containing n elements, this simple algorithm requires us to look at all n elements in the worst-case scenario (all elements are 0s), which can become slow as n becomes large. 
# Can we compute the number of 0s in a sorted binary list by looking at fewer than n elements?


def count_0s(list):
  midpoint = len(list)//2
  zeros = 0
  if len(list) == 1:
    if list[0] == 0:
      zeros += 1
  elif list[midpoint] == 0:
    zeros += len(list[:midpoint+1])
    zeros += count_0s(list[midpoint+1:])
  elif list[midpoint] == 1:
    zeros += count_0s(list[:midpoint])
  return zeros

binary = [0,0,0,0,1,1,1]
print(binary.index(1))
print(count_0s(binary))