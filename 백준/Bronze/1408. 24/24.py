h1, m1, s1 = map(int,input().split(":"))
h2, m2, s2 = map(int,input().split(":"))
sum1 = h1*3600 + m1*60 + s1
sum2 = h2*3600 + m2*60 + s2
sum3 = sum2 - sum1
if sum3 < 0:
    sum3 += 86400
h3 = sum3//3600
sum3 %= 3600
m3 = sum3//60
sum3 %= 60
s3 = sum3

print("%02d:%02d:%02d" %(h3,m3,s3))