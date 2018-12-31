def multiples(N):
    return sum([i for i in range(1, N) if div_by_3_or_5(i)])

def div_by_3_or_5(x):
    return x % 3 == 0 or x % 5 == 0

print(multiples(1000))
