x=input('Enter file name: ')
if len(x)<1: x='short1.txt'
f=open(x)
dis=dict()

for line in f:
    line = line.rstrip()
    if not line.startswith('From'):continue
    words=line.split()
    word=words[1]
    dis[word]=dis.get(word, 0)+1

BC=None
BW=None
for k,v in dis.items():
    if BC is None or BC < v:
        BC=v
        BW=k
print(BW,BC)
