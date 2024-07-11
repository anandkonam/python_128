s1={"apple","gopi","hari"}
s2={"aws","azure","apple"}
s3=s1.difference(s2)
print(s3)
s4={"nani","suma","apple"}
s5=s1.difference(s2,s4)
print(s5)
# how use  -  in between 3 objs
s6=s1-s2-s4   # ===>s1-s2, s1-s4
print(s6)
# how to chaining original set
s1.difference_update(s2)
print("compare two sets:::: ",s1)
s1.difference_update(s2,s4)
print("compare three sets:::",s1)
s1 -= s2
s1 -= s4
print("compare 3 sets with :::",s1)
s10={"pavan","roja","ravi"}
s11={"pavan","rao","arora"}
s13={"pavan","chiru","ntr"}

# symmertic obj
s12=s10.symmetric_difference(s11)
print("symmetric obj::",s12)
s14=s10.symmetric_difference(s11).symmetric_difference(s13)
s7=s1.symmetric_difference(s2)
print("symmetric obj:::",s7)
s8=s1.symmetric_difference(s2,s4)
print("symmetric objs::::",s8)