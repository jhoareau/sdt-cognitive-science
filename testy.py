import pickle
# Getting back the objects:
with open('table1_raw.pkl','rb') as f:
    raw = pickle.load(f)
    
for d in raw:
    print(d)
    for c in raw[d]:
        print("   ",c)
        print("   ",raw[d][c])