#list - shopping list
#milk , bread , butter , poha
#add item
#remove item
#update item
#print list

list = ["milk","bread","butter","poha"]
print(list)
print(len(list))
print(list[0])
print(list[-1])

list.append("chips")
print(list)

list.insert(2,"chocolate")
print(list)

list.extend(["cookies","cakes"])
print(list)

list.remove("cakes")
print(list)

list.reverse()
list.sort()
print(list)

#list= [1,2,3,4, True , 3.14, "Ranjeet"]
#print(type(list))  #<class 'list'>
#print(list)