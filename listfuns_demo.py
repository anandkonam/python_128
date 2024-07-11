# diff values in list
l1=["app1",True,False,16,18.0,"bye"]
for x in l1:
    print(x)
# case senstive objs
l2=["kavitha","nani","srinu","hello","hai"]    
c=l2.count("nani")
print(c)
l2.reverse()
print(l2)
# accessing the element using positive index
print(l2[1])
# accessing the element using negative index
print(l2[-1])
# accesssing the element using slice operator
print(l2[-4:-1])
print(l2[1:])
# assending  order using sort fun
l2.sort()
print(l2)
# dssending order using sort fun
l2.sort(reverse=True)
print(l2)

# remove 1 index obj from list
l2.pop(1)
print(l2)

l2.remove("hai")
print(l2)

# append 
l2.append("nani")
print(l2)

l3=["roja","PAVAN","JAGAN","SONU","kcr"]
# adding two list objs
l2.extend(l3)
print(l2)s