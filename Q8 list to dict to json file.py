import json
keys=["name","designation","age","salary"]
a=["neelam","programmer","24","24000"]
emp1={}
emp2={}
emp3={}
emp4={}
dict={}
for i in range(len(keys)):
    emp1[keys[i]]=a[i]
    dict["employees1"]=emp1
    keys1=["name","designation","age","salary"]
    b=["komal","trainer","24","20000"]
    for j in range(len(keys1)):
        emp2[keys1[j]]=b[j]
        dict["employess2"]=emp2
        keys2=["name","desiganation","age","salary"]
        c=["anuradha","hr","25","40000"]
        for x in range(len(keys2)):
            emp3[keys2[x]]=c[x]
            dict["employess3"]=emp3
            keys3=["name","desiganation","age"]
            d=["abhishek","manager","29",]
            for y in range(len(keys3)):
                emp4[keys3[y]]=d[y]
                dict["employess4"]=emp4
out_file=open("myfile.json","w")
json.dump(dict,out_file,indent=6)
out_file.close()

