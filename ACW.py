#1번 상하좌우

N=int(input())
plans=input().split()

x,y=1,1

for plan in plans:
    if plan=='L' and y>1:
        y-=1
    elif plan=='R' and y<N:
        y+=1
    elif plan=='U' and x>1:
        x-=1
    elif plan=='D' and x<N:
        x+=1

print(x,y)   


#2번 음료수 얼려먹기

N,M=map(int,input().split())

while not (1<=N<=1000 and 1<=M<=1000):
    print("가로 및 세로의 길이는 1줄이상, 1000줄 이하입니다.")
    N,M=map(int,input().split())

while True:
    frame_ch=[]
    check=True
    for _ in range(N):
        row=input().strip()
        if len(row)!=M:
            check=False
        elif not all(ch in '01' for ch in row):
            check=False
        frame_ch.append(row)
        
    if check:
        frame=[list(map(int,row)) for row in frame_ch]
        break
    else:
        print("입력값이 정확하지 않습니다. 다시 입력해주세요.")
        
def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=M:
        return False
    
    if frame[x][y]==0:
        frame[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

cnt_ice=0

for i in range(N):
    for j in range(M):
        if dfs(i,j):
            cnt_ice+=1

print(cnt_ice)


#3번 미로탈출(BFS)

from collections import deque

N,M=map(int,input().split())

while not (4<=N<=200 and 4<=M<=200):
    print("미로의 가로 및 세로의 크기는 4칸이상,200칸 이하입니다.")
    N,M=map(int,input().split())


while True:
    miro_ch=[]
    check=True
    for _ in range(N):
        row=input().strip()
        if len(row)!=M:
            check=False
        elif not all(ch in '01' for ch in row):
            check=False
        miro_ch.append(row)

    if check:
        miro=[list(map(int,row)) for row in miro_ch]
        if miro[0][0]!=1 or miro[N-1][M-1]!=1:
            print("시작 칸과 마지막 칸은 항상 1이어야 합니다.")
        else:
            break
    else:
        print('입력값이 잘못되었습니다. 다시입력해주세요.')

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if miro[nx][ny]==0:
                continue
            if miro[nx][ny]==1:
                miro[nx][ny]=miro[x][y]+1
                queue.append((nx,ny))
    return miro[N-1][M-1]

print(bfs(0,0))


#4번 두 배열의 원소 교체

N,K=map(int,input().split())

while not (1<=N<=100000 and 0<=K<=N):
    print("입력조건이 맞지 않습니다. 다시 입력해주세요.")
    N,K=map(int,input().split())

while True:
    check=True
    A_lst=list(map(int,input().split()))
    B_lst=list(map(int,input().split()))
    for a in A_lst:
        if a<=0 or a>=10000000:
            check=False
    for b in B_lst:
        if b<=0 or b>=10000000:
            check=False
    if len(A_lst)!=N or len(B_lst)!=N:
        print("배열의 원소 개수가 %d개가 아닙니다. 다시 입력해주세요."%N)
        continue
    if check:
        break
    else:
        print("각 원소들의 값은 10,000,000 미만인 자연수입니다. 다시 입력해주세요.")

A_lst.sort()
B_lst.sort(reverse=True)

for i in range(K):
    if A_lst[i]<B_lst[i]:
        A_lst[i],B_lst[i]=B_lst[i],A_lst[i]
    else:
        break

print(sum(A_lst))


#5번 떡볶이 떡 만들기

N,M=map(int,input().split())

while not (1<=N<=1000000 and 1<=M<=2000000000):
    print("입력조건이 맞지 않습니다. 다시 입력해주세요.")
    N,M=map(int,input().split())

while True:
    d_lst=list(map(int,input().split()))
    check=True
    if len(d_lst)!=N:
        print("떡의 수가 %d개가 아닙니다. 다시 입력해주세요."%N)
        continue
    for a in d_lst:
        if a<0 or a>1000000000:
            check=False
    if check:
        break
    else:
        print("떡이 너무 깁니다. 다시 입력해주세요.")

start=0
end=max(d_lst)
cut_h=0

while start<=end:
    mid=(start+end)//2
    rice_cake=0
    for x in d_lst:
        if x>mid:
            rice_cake+=x-mid
    if rice_cake>=M:
        cut_h=mid
        start=mid+1
    else:
        end=mid-1

print(cut_h)


#6번 미래도시

N,M=map(int,input().split())

while not (2<=N<=100 and 1<=M<=1000):
    print("입력조건이 맞지 않습니다. 다시 입력해주세요.")
    N,M=map(int,input().split())

INF=int(1e9)

graph=[[INF]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    graph[i][i]=0

for _ in range(M):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

X,K=map(int,input().split())

for j in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            graph[a][b]=min(graph[a][b],graph[a][j]+graph[j][b])

distance=graph[1][X]+graph[X][K]

if distance>=INF:
    print(-1)
else:
    print(distance)