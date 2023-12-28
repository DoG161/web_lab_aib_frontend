n = int(input())
sequence = list(map(int, input().split()))
medians = []

for i in range(n):
    sequence[:i+1]= sorted(sequence[:i+1])
    if (i + 1) % 2 == 1:
        median = sequence[(i + 1) // 2]
    else:
        median = sequence[i // 2]
    medians.append(median)

sum = 0
for median in medians:
    sum += median
print(sum)