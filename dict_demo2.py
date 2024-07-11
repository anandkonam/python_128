stu={
    "sid":111,
    "sname":"rao",
    "scourses":["java","python"],
    "saddress":"hyd"
}
r1=stu.popitem()
print("after remove last from dict :::",r1)
del stu["sname"]
print("after remove sname from dict :::",stu)
myd1=stu.copy()
print("after calling copy funs",myd1)
s={2:"app2",1:"app1",3:"app3",4:"app4"}
l1=list(s)
l1.sort()
print("after sorting :::",l1)