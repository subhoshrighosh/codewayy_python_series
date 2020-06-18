# working with list

mylist = [1,2,3,4,5,6,7,8,9]


mylist.append(10)                   # adding the element at the end of the list
print(mylist)


mylist.remove(6)                    # revoming a particular element from the list
print(mylist)


mylist.extend([1,2,3,4,5])          # adding the iterable items at the end of the list
print(mylist)


firstcount = mylist.count(4)        # counting no. of times of a particular number occurred in the list
print(firstcount)


myindex = mylist.index(2)           # results the index of a particular element
print(myindex)


popitem = mylist.pop()              # popping item from the list
print(popitem)

print(mylist)


mylist.clear()                      # clearing the whole list
print(mylist)
print(mylist)
