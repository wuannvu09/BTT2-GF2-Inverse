# Extended Euclidean Algorithm in GF(2^10)

Multiplicative inverse computation in **GF(2¹⁰)** using the **Extended Euclidean Algorithm**.

## Parameters

- **Finite Field**: GF(2¹⁰)
- **Irreducible Polynomial**: `m(x) = x¹⁰ + x³ + 1` (decimal: 1033)

## Test Vectors

| Input | Inverse | Polynomial |
|-------|---------|------------|
| a = 523 | a⁻¹ = 798 | x⁹ + x⁸ + x⁴ + x³ + x² + x |
| b = 1015 | b⁻¹ = 709 | x⁹ + x⁷ + x⁶ + x² + 1 |

## How to Run

```bash
python gf2_10_inverse.py
```

The program prints all intermediate values (quotient, remainder, auxiliary polynomial) at each step of the algorithm.

## Algorithm Overview

1. Initialize `r₀ = m(x)`, `r₁ = a(x)`, `s₀ = 0`, `s₁ = 1`
2. At each step, compute:
   - `q, r = poly_div(rᵢ₋₁, rᵢ)` — polynomial division over GF(2)
   - `sᵢ₊₁ = sᵢ₋₁ ⊕ (q × sᵢ)` — update auxiliary polynomial
3. Repeat until remainder = 0
4. The last non-zero `s` value is the multiplicative inverse
