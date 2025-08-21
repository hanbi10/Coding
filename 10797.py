day = int(input())
l = list(map(int,input().split()))
cnt = 0

for i in l:
    if i == day:
        cnt += 1
        
print(cnt)