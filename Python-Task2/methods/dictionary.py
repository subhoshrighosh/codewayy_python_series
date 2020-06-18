# working with dictionary


# keys and values
mydictionary = {'name' : 'Subhoshri' ,'dept' : 'ECE' , 'univroll' : '33' ,'year' : 'second' , 'college' : 'AEC' }
print(mydictionary)

print(mydictionary.items())


# displaying the keys
print(mydictionary.keys())


# displaing the values
print(mydictionary.values())

# looping in dictionary
for x in mydictionary:
    print(x)


# adding more elements in dictionary
mydictionary['dob'] = '25/06/1999'


# editing the corresponding key
mydictionary['name'] = "deepak"
print(mydictionary)


# displaying the length of my dictionary
mydictionarylength = len(mydictionary)
print(mydictionarylength)


# displaying a particular value of a key
myname = mydictionary.get('name')
print(myname)


# popping
popname = mydictionary.pop('name')
print(popname)
popelement = mydictionary.popitem()
print(popelement)


# clearing the dictionary
mydictionary.clear()

print(mydictionary)
