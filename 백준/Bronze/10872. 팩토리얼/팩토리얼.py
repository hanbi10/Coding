n = int(input())
ans = 1
for i in range(1, n):
    ans = ans*i
if n == 0:
    print(1)
else:
    print(ans*n)