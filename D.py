f = open('input.txt')
A = f.readline().split()
k = int(A[0])
n = int(A[1])
MIN = f.readline().split()
for i in range(n):
    MIN[i] = int(MIN[i])
for i in range(k - 1):
    A = f.readline().split()
    for i in range(n):
        A[i] = int(A[i])
    for i in range(n):
        if A[i] < MIN[i]:
            MIN[i] = A[i]

M = str()
for i in range(n):
    M += str(MIN[i]) + ' '

f = open('output.txt', 'w')
print(M, file = f)
f.close()   