def multiplyList(dtList):

    result = 1
    for x in dtList:
        result = result * x
    return result



list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))