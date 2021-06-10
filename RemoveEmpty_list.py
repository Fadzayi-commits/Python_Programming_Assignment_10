list2 = [5, 6, [], 3, [], [], 9]


print("The original list is : " + str(list2))



res = list(filter(None, list2))


print("List after empty list removal : " + str(res))