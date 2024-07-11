t=("hello",10,True,False,15.0)
print(t)

# tuple convert into list type
l1=list(t)
l1[0]="bye"
print(l1)
# iterating objs
for x in t:
    print(x)

t3=("ravi","komal","vamshi") 
(x,y,z)=t3
print(x)   
print(y)
print(z)

t4=("lokesh","sai","uday","pavan","naresh")
(n1,n2,*n3)=t4
print("n1 value:::",n1)
print("n2 value:::",n2)
print("n3 value:::",n3)

t5=("lokesh","sai","uday","pavan","naresh")
(s1,*s2,s3)=t5
print(s1)
print(s2)
print(s3)

t6=("lokesh","sai","uday","pavan","naresh")
l3=list(t6)
r1=l3[0:2]
r2=l3[2:4]
r3=l3[4:]
print(r1)
print(r2)
print(r3)