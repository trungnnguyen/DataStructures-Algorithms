import sys

def ind(A):
    # finds the indegree of all the nodes
    for i in range(0,N):
        sum0=0
        for j in range(0,N):
            sum0=sum0+A[j][i]
        indegree[i+1]=sum0
        
    return indegree

def modi(indegree):
    #checks topological ordering
    t=0
    
    for key in indegree:
        if (int(indegree[key])==0):
            t=(int(key)-1)
            print 'h'
            print t
            
        if (0 not in indegree.values()):
            print 'Not acyclic'
            sys.exit()
    return t

N=int(raw_input())
A=[] # node - node adjacency matrix ( initial matrix and residual matrix)
C=[] # Cost ( initial matrix and residual matrix)
B=[]
indegree={}

for i in range(0,N):
    a=[]
    b=[]
    c=[]
    for j in range(0,N):
        
        a.append(int(raw_input('A('+str(i+1)+','+str(j+1)+ '): ')))
        b.append(0)
        if(a[j]!=0):
            c.append(int(raw_input('C('+str(i+1)+','+str(j+1)+ '): ')))
            
        else:
            c.append(10000)   
    A.append(a)
    B.append(b)
    C.append(c)
for i in range(0,N):
    for j in range(0,N):
        B[i][j]=A[i][j]
s=[]

indegree=ind(A)  
while(len(indegree)>0):    
    s.append(modi(indegree))
    
    key=s[-1]+1
    
    for i in range(0,N):
        A[int(key)-1][i]=0
        A[i][int(key)-1]=0
    
    indegree=ind(A)
    
    for i in s:
        del indegree[i+1]
    print indegree
    
print s
print B
        
# s is the topological ordering
#B is the original graph

d={} #shortest distance from node 1
d[s[0]+1]=0
pred={}#predecessor of node
pred[s[0]+1]=1
for i in range(1,N):
    d[i+1]=1000000 # assigning to infinity
    pred[i+1]=i+1

#arc processing and checking for termination
for i in range(0,N):
    for j in range(0,N):
        if(B[s[i]][s[j]] != 0):
            if(d[s[j]+1]>d[s[i]+1]+C[s[i]][s[j]]):
                d[s[j]+1]=d[s[i]+1]+C[s[i]][s[j]]
                pred[s[j]+1]=s[i]+1

print "All nodes are printed based on their original graph"
print "shortest distance from node 1 to all other nodes "
print d
print "predecessor of each node"
print pred
    
