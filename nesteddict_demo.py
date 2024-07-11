d1={
    "emp1":{
        "ename":"kishor",
        "esal":"15000"
    },
    "stud":{
        "sid":102,
        "sname":"nike"
    },
    "dept":{
        "did":111,
        "dname":"css"
    },
    "product":{
        "pid":1555,
        "pname":"mobile"
    }
}

# access dname from dept
print (d1["dept"]["dname"])
print("")
# access pname
print(d1["product"]["pname"])
print("")

for x,y in d1.items():
    print(x,"::::",y)