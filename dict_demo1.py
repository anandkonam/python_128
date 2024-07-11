emp={
    "eid":101,
    "ename":"suma",
    "esal":15000,
    "deptno":1
}
x=emp.get("ename")
print("value:::",x)
# it has to Iterating only for keys
for i in emp.keys():
    print("keys:::",i)
#it has to Iterating only values
for v1 in emp.values():
    print("values:::",v1)
# Iterating both
for k,v in emp.items():
    print("keys::::",k,"values:::;",v)
# how to search given key value
k2=input("enter a key    ")    
s2=emp.get(k2)
print(k2,"::::::",s2)
# to remove given key vaue form dict
d=input("enter a dict key  ")
d2=emp.pop(d)
print(" remove value ::::",d2)
print(" after removing the obj ::",emp)
# adding new key
emp["comm"]=300
print("after adding new key :::",emp)