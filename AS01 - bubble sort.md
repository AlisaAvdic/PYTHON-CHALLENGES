import random
list = random.sample(range(1, 100), 9)
print ("Random number list is : " +  str(list)) 
#sort
for X in range(len(list) - 1, 0, -1):
    for j in range(X):
        if list[j] > list[j + 1]:
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
print("sorted array is : ", list)


result : 
Random number list is : [16, 31, 55, 42, 91, 26, 64, 86, 59]
sorted array is :  [16, 26, 31, 42, 55, 59, 64, 86, 91]
