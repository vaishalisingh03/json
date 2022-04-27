import json
d={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
x=json.dumps(d,indent=4,sort_keys=True)
print(x)