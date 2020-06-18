# working with tuple


# tuple declaration
mytuple = (1,2,3,4,5,6,7,8,9)


# counting the number of times a particular element occurred in the tuple
tuplcount = mytuple.count(7)
print(tuplcount)


# indexing
tuplindex = mytuple.index(2)
print(tuplindex)


# maximum element in the tuple
maxtup = max(mytuple)
print(maxtup)


# minimum element in the tuple
minTup = min(mytup)
print(minTup)


# length of the tuple
tuplelength = len(mytuple)
print(tuplelength)


# slicing a part of the tuple
slicetup = tuple1[1:3]
print(slicetup)


# looping in tuple
for x in mytuple:
    print(x)
 
    
# tuples are also immutable
