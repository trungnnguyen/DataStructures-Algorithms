N=int(raw_input('No of Nodes: '))
n={}
p=[]
p.append(1)
for i in range(1,N):
    heads=()
    p.append(int(raw_input('Point('+str(i+1)+'): ')))
    
    
p.append(p[N-1]+1)

for i in range(0,N):
    a=[]
    outgoing=[]
    for j in range(0,p[i+1]-p[i]):
        a.append(int(raw_input('Heads for node '+str(i+1)+': ')))
        outgoing.append(str(p[i]+j))
    n[i+1]=(p[i],p[i+1]-p[i],outgoing,a)

for i in range(0,N):
    print str(i+1)+':'+ str(n[i+1])
    
        
    
    
