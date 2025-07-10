n=5
edges=((1,2,2),(2,3,5),(3,4,1),(4,5,2),(5,1,1))
adjMatrix=[[0]*(n+1) for i in range (n+1)]
adj={}
for i in range(1,n+1):
    adj[i]=[]
print(adj)
for i in edges:
    u,v,w = i
    adjMatrix[u][v]=w    
    adjMatrix[v][u]=w
for row in adjMatrix:

    print(row)