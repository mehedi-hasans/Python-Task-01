list1 = []
list2 = []
newList = []
newList2 = []
#Input two list items and append in newList
for i in range(4):
    i = int(input("Number: "))
    list1.append(i)
newList.append(list1)

print('List2 itmes put 8')
for i in range(4):
    i = int(input("Number: "))
    list2.append(i)
newList.append(list2)

#New List 2 program
def assignment (newList):
    for i in newList:
        for j in i:
            newList2.append(j)
    newList2.pop()
    newList2.pop()
    print('New List is: ',newList2)
assignment(newList)

#Even and Odd conditions
def odd(newList2):
    evenList = []
    oddList = []
    for i in newList2:
        if i%2==0:
            evenList.append(i)
        else:
            oddList.append(i)
    print('Even List from new list: ', evenList)
    print('Odd List from new list: ', oddList)
    return evenList
odd(newList2)


#Even List Maximum and Minimum
def evenMax(evenList):
    max = newList2[0]
    for i in evenList:
        if i > max:
            max=i
    print('even List maximum Number', max)
    print(evenList)
evenMax(odd(newList2))



























# def even(list):
#     print(list)

#Minimum item from newList2
# def min(newList2):
#     min = newList2[0]
#     for i in newList2:
#         if i < min:
#             min=i;
#     print('New List Minimum Number', min)
# min(newList2)

# def max(newList2):
#     max = newList2[0]
#     for i in newList2:
#         if i > max:
#             max=i;
#     print('New List maximum Number', max)
# max(newList2)








    # ==============

#==============================================


# def assignment (newList):

#     for i in newList:
#         for j in i:
#             newList2.append(j)
#     newList2.pop()
#     newList2.pop()
#     #Even and Odd conditions
#     evenList = []
#     oddList = []
#     for i in newList2:
#         if i%2==0:
#             evenList.append(i)
#         else:
#             oddList.append(i)

#     print('List 1: ', list1)
#     print('List 2: ', list2)
#     print('New List2: ',newList2)
#     print('Even List from new list: ', evenList)
#     print('Odd List from new list: ', oddList)
        
#     #------------------------------
#     #Minimum item from newList2
#     min = newList2[0]
#     for i in newList2:
#         if i < min:
#             min=i;
#     #Minimum item from evenList
#     minEven = evenList[0]
#     for i in newList2:
#         if i < min:
#             minEven=i;
#     #Minimum item from oddList
#     minOdd = oddList[0]
#     for i in newList2:
#         if i < min:
#             minOdd=i;


#     print('New List Minimum Number', min)
#     print('Even List Minimum Number', minEven)
#     print('Odd List Minimum Number', minOdd)

# assignment(newList)