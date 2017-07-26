import pickle
object1=[]
s=raw_input("Enter keyword=")

with (open("aaa.txt", "rb")) as f:
    while True:
        try:
            object1=pickle.load(f)
        except EOFError:
            break

rec=[]
for key in object1.keys():
    for keyword in object1[key]:
        if s in keyword:
            rec.append(key)

rec=set(rec)
for d in rec:
 print d
 
            
