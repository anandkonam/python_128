s1={"ravi","naresh","vamshi","sai","sonu"}
print(s1)
print("")

s1.remove("naresh")
print("after remove naresh",s1)
print("")
s1.discard("sai")
print("after discard",s1)

# iterating objs
for x in s1:
    print(x)