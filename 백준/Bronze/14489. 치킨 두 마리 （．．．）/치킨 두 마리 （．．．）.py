a, b = map(int,input().split())
c = int(input())

sum = a + b

price = c * 2

if sum >= price:
    print(sum - price) 
else:
    print(sum)