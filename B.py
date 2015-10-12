f = open('input.txt')
bargain = int(f.readline())
coins = f.readline().split()
for i in range(bargain):
    coins[i] = int(coins[i])
amount = 0
fives = 0
for coin in coins:
    if coin == 5:
        fives += 1
    else:
        change = (coin - 5)//5
        if fives > 0:
            if fives >= change:
                fives -= change
            else:
                amount += change - fives
                fives = 0
        else:
            amount += change
f = open('output.txt', 'w')
print(amount, file = f)
f.close()