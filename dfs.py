ad_max = [
    #0 1 2 3 4 5
    [0,1,1,1,0,0],#0
    [1,0,0,0,1,1],#1
    [1,0,0,0,0,5],#2
    [1,0,0,0,0,0],#3
    [0,1,0,0,0,0],#4
    [0,1,1,0,0,0] #5
]
visited = [0,0,0,0,0,0]
ans = []
apar = []

def stack():
    for val in apar:
        print(val,end='|')
    print()

def dfs(n):
    if visited[n]:
        return
    else:
        visited[n] = 1
        num = 0
        apar.append(n)
        stack()
        for relation in ad_max[n]:
            if relation != 0:
                dfs(num)
            num += 1
    #print(n,end='|')
    ans.append(n)
    apar.pop()
    stack()

src_node = int(input('Enter the source node'))
dfs(src_node)
print(ans)