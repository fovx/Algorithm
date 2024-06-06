star = int(input())

z = []
for i in range(1, star+1):
    z= "*"*i
    print(z.rjust(star))
