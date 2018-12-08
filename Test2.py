n = int(input())

count = [0]*10000
for i in range(n+1):
        k = sum(map(int,str(i)))
        print(k)
        count[k]=count[k]+1

print(max(count))

