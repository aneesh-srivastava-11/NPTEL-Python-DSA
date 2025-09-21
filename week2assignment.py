def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def primeproduct(m):
    if m <= 0:
        return False
    for p in range(2, m):
        if isprime(p) and m % p == 0:
            q = m // p
            if isprime(q) and p != q:
                return True
    return False
#q2
def delchar(s, c):
    if len(c) != 1:
        return s
    return s.replace(c, '')
#q3
def shuffle(l1, l2):
    result = []
    min_length = min(len(l1), len(l2))
    for i in range(min_length):
        result.append(l1[i])
        result.append(l2[i])
    result.extend(l1[min_length:])
    result.extend(l2[min_length:])
    return result
