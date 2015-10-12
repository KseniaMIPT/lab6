f = open('input.txt')
A = f.readline().split()
N = int(A[0]) #кол-во должников
K = int(A[1]) #кол-во долговых расписок
S = [0]*N
for i in range(K):
    A = f.readline().split()
    S[int(A[0]) - 1] = S[int(A[0]) - 1] - int(A[2])
    S[int(A[1]) - 1] = S[int(A[1]) - 1] + int(A[2])
M = str()
for i in range(N):
    M += str(S[i]) + ' '
f = open('output.txt', 'w')
print(M, file = f)
f.close() 