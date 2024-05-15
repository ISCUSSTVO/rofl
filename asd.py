x = int(input())
y = int(input())

def qwe(*n):
    j = []
    for d in n:
        z = [i for i in range(1, d + 1) if d % i == 0]
        j.append(z)
    return j

yu = qwe(x)
yui = qwe(y)
p = qwe(x)[0]
m = qwe(y)[0]
asd = [i for i in p if i in m]

def find_subset_sum(numbers, target):
    dp = [0] + [float('inf')] * target

    for num in numbers:
        for i in range(num, target + 1):
            dp[i] = min(dp[i], dp[i - num] + 1)

    if dp[target] == float('inf'):
        return None

    subset = []
    while target > 0:
        for num in numbers:
            if target - num >= 0 and dp[target] == dp[target - num] + 1:
                subset.append(num)
                target -= num
                break

    return subset

result = find_subset_sum(yui[0], x)

# Добавление элементов из asd до тех пор, пока сумма не превысит x
while sum(result) < x:
    for num in asd:
        result.append(num)
        if sum(result) > x:
            result.pop()
            break

print(result)