f = open('input.txt')
N = int(f.readline())
A = f.readline().split()
for i in range(len(A)):
    A[i] = int(A[i])
min = 999

for i in range(len(A) - 1):
    for j in range(i + 1, len(A)):
        if A[i] == A[j]:
            x = j - i
            if x < min:
                min = x

f = open('output.txt', 'w')
if min == 999:
    print(0, file = f)
else:
    print(min, file = f)
f.close()    