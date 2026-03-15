def deg(a):
    return a.bit_length() - 1 if a else -1

def poly_str(a):
    if a == 0: return "0"
    terms = []
    for i in range(deg(a), -1, -1):
        if (a >> i) & 1:
            terms.append("1" if i == 0 else "x" if i == 1 else f"x^{i}")
    return " + ".join(terms)

def poly_div(a, b):
    q = 0
    while deg(a) >= deg(b):
        shift = deg(a) - deg(b)
        q ^= (1 << shift)
        a ^= b << shift
    return q, a

def poly_mul(a, b):
    r = 0
    while b:
        if b & 1: r ^= a
        a <<= 1; b >>= 1
    return r

def ext_gcd_inv(a, m):
    r0, r1 = m, a
    s0, s1 = 0, 1
    step = 0

    print(f"\nFinding inverse of {a} (bin: {bin(a)}) = {poly_str(a)}")
    print(f"m(x) = {poly_str(m)}\n")

    print(f"Init:")
    print(f"  r0 = m(x) = {poly_str(r0)} ({r0})")
    print(f"  r1 = a(x) = {poly_str(r1)} ({r1})")
    print(f"  t0 = {poly_str(s0)} ({s0})")
    print(f"  t1 = {poly_str(s1)} ({s1})\n")

    while r1 != 0:
        step += 1
        q, r = poly_div(r0, r1)
        s = s0 ^ poly_mul(q, s1)

        print(f"Step {step}: {poly_str(r0)} / {poly_str(r1)}")
        print(f"  q = {poly_str(q)} ({q}),  r = {poly_str(r)} ({r})")
        print(f"  s = {poly_str(s)} ({s})\n")

        r0, r1 = r1, r
        s0, s1 = s1, s

    print(f"Result: {a}^(-1) = {s0} (bin: {bin(s0)}) = {poly_str(s0)}")

    prod = poly_mul(a, s0)
    _, check = poly_div(prod, m)
    print(f"Verify: {a} * {s0} mod m(x) = {check} {'OK' if check == 1 else 'FAIL'}\n")
    return s0

if __name__ == "__main__":
    M = 0b10000001001

    print("=" * 50)
    print("Extended Euclidean Algorithm in GF(2^10)")
    print("m(x) = x^10 + x^3 + 1")
    print("=" * 50)

    for val in [523, 1015]:
        ext_gcd_inv(val, M)
