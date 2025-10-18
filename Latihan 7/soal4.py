import math

def euler_phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def pow_with_cap(base, exp, cap):
    result = 1
    while exp > 0:
        if exp & 1:
            result *= base
            if result > cap:
                return cap + 1
        exp >>= 1
        if exp:
            base *= base
            if base > cap:
                base = cap + 1
    return result

A, B, C, N = map(int, input().split())
M = N + 1

if M == 1:
    print(0)
else:
    phi = euler_phi(M)
    exp_mod_phi = pow(B, C, phi)
    is_large = pow_with_cap(B, C, phi) >= phi

    if math.gcd(A, M) == 1:
        exp = exp_mod_phi + (phi if is_large else 0)
    else:
        exp = exp_mod_phi + (phi if is_large else 0)

    print(pow(A, exp, M))
