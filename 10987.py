n = input()
vow = ['a', 'e', 'i', 'o', 'u']
cnt = 0

for i in vow:
    for j in range(len(n)):
        if i == n[j]:
            cnt += 1

print(cnt)