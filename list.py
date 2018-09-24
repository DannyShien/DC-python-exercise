#List exercise: 
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Sum the numbers. 

b = sum(num)
print('Sum =', b)

#Largest Number in list.
print('Largest number: ', max(num))

#Smallest number in list. 
print('Smallest number: ', min(num))

#Even numbers. 
i = 0 
while i < len(num): 
  if num[i] % 2 == 0: 
    print(num[i] , end = '')
  i += 1
print()    

#Positive numbers. 
pos_num = [1, -3, 4, -2,  9, 5, 2]
i = 0
while i < len(pos_num): 
  if pos_num[i] > 0: 
    print('Positive numbers: ', pos_num[i])
  i += 1

#Positive numbers II. 
nums = [3, -5, 7, -2, -3, 9, 1, 6]
list_b = []

i = 0 
while i < len(nums): 
  if nums[i] > 0:
    list_b.append(nums[i])
  i += 1
print('Postive numbers II: ', list_b)

# Multiply a list: 
# num variable already established up top
# using list_b from before

i = 0
list_c = []
factor = 2 
while i < len(num):  
  list_c.append(num[i] * factor)
  i += 1
print('Multiplied list: ', list_c)

# Multiply Vectors
list_1 = [2, 4, 6, 8]
list_2 = [3, 5, 7, 9]
list_3 = []
i = 0 
while i < len(list_1 and list_2): 
  list_3.append(list_1[i] * list_2[i])
  i += 1
print('Multiplied vector list = ', list_3)

# Matrix Addition
m1 = [[2, 4], [1, 3]]
m2 = [[6, 8], [5, 7]]
m3 = []
i = []
j = []
count = 0
print(m1 and m2)
while count < len(m1):
  i.append(m1[count][0] + m2[count][0])
  count1 = 0 
  if count < (count1 +1): # if (count - 1) < count1:
    while (count1) < len(m2): 
      j.append(m1[count1][1] + m2[count1][1])
      count1 += 1
  count += 1
m3.append(i)
m3.append(j)
print('Matrix addition: ', m3)

#Refactored Matrix Addtion: 
m1 = [[2, 4], [1, 3]]
m2 = [[6, 8], [5, 7]]
m3 = [[],[]]

count = 0
while count < len(m1):
  m3[0].append(m1[count][0] + m2[count][0])
  count1 = 0 
  if count < (count1 +1): # if (count - 1) < count1:
    while (count1) < len(m2): 
      m2[1].append(m1[count1][1] + m2[count1][1])
      count1 += 1
  count += 1
print('Refactored Matrix: ', m3)

# import numpy as np
# matrix1 = np.matrix([[2, 4], [1, 3]])
# matrix2 = np.matrix([[6, 8], [5, 7]])
# matrix3 = []

# matrix3.append(matrix1 + matrix2)
# print(matrix3)

# Matrix Addition II

m1 = [[2, 4], [1, 3]]
m2 = [[6, 8], [5, 7]]
m3 = []
i = []
j = []
count = 0

while count < len(m1 and m2):
  i.append(m1[count][0] + m2[count][0])
  count1 = 0 
  if count < (count1 +1): # if (count - 1) < count1:
    while (count1) < len(m2): 
      j.append(m1[count1][1] + m2[count1][1])
      count1 += 1
  count += 1
m3.append(i)
m3.append(j)
print('Matrix addition: ', m3)