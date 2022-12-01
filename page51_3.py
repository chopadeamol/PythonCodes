# """
# R-1.3: Write a short pyton function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two, Do not use the built in functions min or max in implementing your solution
# """
# import sys
# def minmax(data):
#     largest = data[0]
#     smallest = data[0]
#     for num in data:
#         if num > largest:
#             largest = num
#         if num < smallest:
#             smallest = num
#     return smallest, largest

# iData = ([1,2,3,4,5])
# iObj = minmax(iData)
# print(iObj)

# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         num = []
#         for i in nums:
#             if i not in num:
#                 num.append(i)
#         print(len(num),",", num)

# nums = [0,0,1,1,1,2,2,3,3,4]
# numbers = sorted(nums)
# s = Solution()
# s.removeDuplicates(numbers)

python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
for i in python_students:
    #for j in i:
    print(i[1][0])
