thislist = ['apple','banna','tomato','carrit']

print(thislist[0:2])

if 'apple ' in thislist:
    print("T")

thislist.append("orange")
print(thislist)


thislist[-1]="kiwi"

print(thislist)

thislist.pop(-1)
print(thislist)
num=(1,2,3,45,6)
thislist.extend(num)
print(thislist)


newlist= [x for x in thislist if  True ]

print(newlist)


for i in newlist:
    type(int) == True
    newlist.pop()

print(newlist)
    
newlist.sort()
print(newlist)
