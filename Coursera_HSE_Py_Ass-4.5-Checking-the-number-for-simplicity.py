n = int(input())


def IsPrime(n):
    if n > 1:
        for p in range(2, int(n**0.5) + 7):
            if n % p == 0 and p**2 <= n:
                return False
            elif p**2 >= n:
                return True


if IsPrime(n):
    print('Yes')
else:
    print('No')
