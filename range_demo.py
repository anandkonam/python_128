n1=int(input("enter range value"))
# y=int(n1)
# dynamic elements we can store inside list
x=list(range(n1))
print(x,"::::",type(x))
for i in range(10,0,-1):
    print(i)
for i in range(0,10,2):
    print("even :::",i)    
r1=int(input("enter even range"))    
for i in range(0,r1,2):
    print("even :::",i)
for i in range(1,10,2):
    print("odd :::",i)
r2=int(input("given range"))    
for i in range(1,5,2):
    print(list(range(r2)))
       