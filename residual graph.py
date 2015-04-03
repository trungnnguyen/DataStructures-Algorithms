N=int(raw_input())
A=[] # node - node adjacency matrix ( initial matrix and residual matrix)
C=[] # Cost ( initial matrix and residual matrix)
U=[] # Capacity
X=[] # Flow	
X_b=[] # Base Flow
R=[]	#Residual Capacity
X_prime=[] # Residual flow
for i in range(0,N):
    a=[]
    c=[]
    u=[]
    x=[]
    x_b=[]
    r=[]
    x_prime=[]
    for j in range(0,N):
        r.append(0)
        x_prime.append(0)
        a.append(int(raw_input('A('+str(i+1)+','+str(j+1)+ '): ')))
        if(a[j]!=0):
            c.append(int(raw_input('C('+str(i+1)+','+str(j+1)+ '): ')))
            u.append(int(raw_input('U('+str(i+1)+','+str(j+1)+ '): ')))
            x.append(int(raw_input('X('+str(i+1)+','+str(j+1)+ '): ')))
            x_b.append(int(raw_input('X_b('+str(i+1)+','+str(j+1)+ '): ')))
        else:
            c.append(10000)
            u.append(0)
            x_b.append(0)
            x.append(0)
    A.append(a)
    C.append(c)
    U.append(u)
    X.append(x)
    X_b.append(x_b)
    R.append(r)
    X_prime.append(x_prime)

for i in range(0,N):
    for j in range(0,N):
        if(A[i][j]==0):
            A[i][j]=A[j][i]
        if(C[i][j]==10000):
            C[i][j]=-C[j][i]
            
for i in range(0,N):        
    for k in range(0,N):
        if(U[i][k]>0):
            R[i][k]=U[i][k]-X_b[i][k]
            R[k][i]=X_b[i][k]
        if(X[i][k]>=X_b[i][k]):
            X_prime[i][k]=X[i][k]-X_b[i][k]
            
        else:
            X_prime[k][i]=X_b[i][k]-X[i][k]
            

print "A is"
for i in range(0,N):
    for j in range(0,N):
        print (A[i][j]),
    print ''

print "C is"
for i in range(0,N):
    for j in range(0,N):
        print (C[i][j]),
    print ''

print "R is"
for i in range(0,N):
    for j in range(0,N):
        print (R[i][j]),
    print ''
print "X_prime is"
for i in range(0,N):
    for j in range(0,N):
        print (X_prime[i][j]),
    print ''
