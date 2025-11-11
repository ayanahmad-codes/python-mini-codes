list = [1, 2, 3, 44, 7, 43, 98, 7]
list.sort() # ascending order 
print(list)

list.sort(reverse=True) # descending order 
print(list)

list.reverse() # reverse ulta karega
print(list)

# list.index(2)
# print(list)
print(list.count(7)) # count karega list me kitna bar 7 aata hai

# modified = list
# modified[0] = 100 # index change hoga or m = l hoga
# print(list)

list.copy()
print(list)

list.append(555)
print(list)

list.insert(1, 786)
print(list)