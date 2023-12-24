#   Created by Elshad Karimov on 10/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Accessing/Traversing the list

shoppingList = ['Milk', 'Cheese', 'Butter']

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    # print(shoppingList[i])
empty = []
for i in empty:
    print("I am empty")


# Update/Insert - List 

myList = [1,2,3,4,5,6,7]
print(myList)
myList.insert(4,15)

myList.append(55)

newList = [11,12,13,14]
myList.extend(newList)
print(myList)


#  Searching for an element in the List
myList =  [10,20,30,40,50,60,70,80,90]

def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'

print(searchinList(myList, 100))


#  List operations / functions
total = 0 
count = 0
while (True):
    inp = input('Enter a number: ') 
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1 
    average = total / count
					
print('Average:', average)



numlist = list() 
while (True):
    inp = input('Enter a number: ') 
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
					
average = sum(numlist) / len(numlist) 
print('Average:', average)


a = [0,1,2,3,4,5,6]
print(max(a))

a = 'spam-spam1-spam'
b = a.split("-")
print (b)


# List Comprehension

prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]
new_list = [number if number> 0 else 'negative number' for number in prev_list]
# print (new_list[3:0:-1])


a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50
print(a)


a=[1,2,3,4,5]
print(a[3:0:-1])



fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
 
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
 
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
    print(ls)
 
print(sum)


def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])


data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
 
    for row in m:
        for element in row:
            if v < element: v = element
            print(v)
 
    return v
print(fun(data[0]))