# Thuat toan Euclidean mo rong trong GF(2^10)

Tinh nghich dao nhan trong truong GF(2^10) su dung thuat toan Euclidean mo rong.

## Thong so

- Truong huu han: GF(2^10)
- Da thuc toi gian: m(x) = x^10 + x^3 + 1 (thap phan: 1033)

## Ket qua test

| Dau vao | Nghich dao | Da thuc |
|---------|------------|---------|
| a = 523 | a^-1 = 798 | x^9 + x^8 + x^4 + x^3 + x^2 + x |
| b = 1015 | b^-1 = 709 | x^9 + x^7 + x^6 + x^2 + 1 |

## Cach chay

```bash
python gf2_10_inverse.py
```

Chuong trinh in ra tat ca cac gia tri trung gian (thuong, du, da thuc phu) tai moi buoc cua thuat toan.

## Mo ta thuat toan

1. Khoi tao r0 = m(x), r1 = a(x), t0 = 0, t1 = 1
2. Tai moi buoc tinh:
   - q, r = chia da thuc r(i-1) cho r(i) tren GF(2)
   - t(i+1) = t(i-1) XOR (q nhan t(i))
3. Lap lai cho den khi du bang 0
4. Gia tri t cuoi cung chinh la nghich dao nhan
