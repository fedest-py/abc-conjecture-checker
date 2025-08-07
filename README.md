# abc-conjecture-checker
This program explores the **ABC Conjecture**, a famous problem in number theory. For each pair of integers `a` and `b` in a file, it:
- Computes `c = a + b`
- Checks if `GCD(a, b) = 1`
- Calculates the **radical** of `a`, `b`, and `c` (product of all distinct prime factors)
- Tests whether `radical > c`

## 🧠 Concepts:
- Greatest Common Divisor (GCD)
- Prime checking and radical calculation
- Real-world application of mathematical conjectures

## 📋 Files:
- `abc.py` – Main Python script
- `ab.txt` – Contains 200 lines of integer pairs `a b`

## 🧪 Sample Output:
- a: 104, b: 33, GCD: 1, c: 137, Radical: 117546
- a: 3, b: 105, GCD: 3
- ...
- Fraction where radical > c: 0.9123
