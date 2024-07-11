person={
    "name":"pvrao",
    "age":28
}
gen={
    "human_type1":"male",
    "human_type2":"female"
}
qualification={
    "q1":"MBA",
    "q2":"BTECH",
    "q3":"MCA"
}

mydict={
    "person":person,
    "gen":gen,
    "qualification":qualification
}
print(mydict["person"]["name"])
print(mydict["gen"]["human_type1"])
print(mydict["qualification"]["q1"])
for x,y in mydict.items():
    print(x,"::::",y)
