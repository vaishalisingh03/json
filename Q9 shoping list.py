import json
d={
    "shopping_list":
  { 
    "choco":"15",
    "Biscuits":"50",
    "Diary_milk":"30",
    "ice_cream":"20",
    } 
}
x=open("txt.shoping_list","w")
json.dump(d,x,indent=4)
x.close()
item=input("which item you want to by:>")
quant=int(input("which quantiy you want to by:>"))
with open("txt.shoping_list") as fh:
    data=json.load(fh)
    for i,y in data.items():
        if item in y:
            for a,b in y.items():
                if quant<=int(b):
                    b1=int(b)-quant
                    y[a]=b1
                        # y[a]=quant
                else:
                    d=quant-int(b)
                    b2=int(b)-d
                    y[a]=b2
                        # y[a]=quant
        else:
            y[item]=str(quant)
            print(data)
with open("txt.shoping_list","w") as f:
    json.dump(data,f,indent=4)
