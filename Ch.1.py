

protocolList = []
protocolList.append("ftp")
protocolList.append("smtp")
protocolList.append("http")
protocolList.append("ssh")

print(protocolList)
protocolList.sort()  # sorts list


print(protocolList)

print(len(protocolList))  # gives length(counts the number of elements) of the array/list
print(type(protocolList)) # specifies what the variable is

position = protocolList.index("ssh")  # access the specific index of an element in a list
print ("ssh position " + str(position))


protocolList.remove("ssh") # removes an element from the list/array
print(protocolList)

for i in protocolList:   # loops through array/list
    print (i + "\n")


# .append(value): Appends an element at the end of the list
# .count('x'): Gets the number of 'x' in the list
# .index('x'): Returns the index of 'x' in the list
# .insert('y','x'): Inserts 'x' at location 'y'
# .pop(): Returns the last element and also removes it from the list
# .remove('x'): Removes the first 'x' from the list
# .reverse(): Reverses the elements in the list
# .sort(): Sorts the list alphabetically in ascending order, or numerically in
# ascending order


protocolList.reverse()
print(protocolList)

# another way to reverse a list/array is to use the -1 index.
protocolList[::-1]
print(protocolList)

# comprehension 