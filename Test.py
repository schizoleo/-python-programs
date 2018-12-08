A = list(map(int,input().split()))
for i in range(len(A)):
    A[i] = str(A[i])


A = sorted(A)
A = A[::-1]

print(''.join(A))
