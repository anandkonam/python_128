# creating list
x=["app1","app2","app3","app4","app5","app6","10"]
# it will dispaly 2 index obj and datatype
print("2nd index value:::",x[2])
# iterating obj
for i in x:
    print(i)
# update 2 index obj
x[2]="hai"
print("after updating 2 index:::",x[2])
# update more than one obj
x[2:4]=["pavan","nani"]
print("after updating 2 obj:::",x[2],"3rd index:::"+x[3])
# after 3rd index we want insert new element
x.insert(3, "hello")
print(x)
#remove all
x.clear()
print(x)