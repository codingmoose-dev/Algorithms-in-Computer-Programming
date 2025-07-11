Elliptic Curve Point Multiplication is core to Elliptic Curve Cryptography (ECC), used in modern security systems like Bitcoin, TLS, and more. It’s a practical algorithm in cryptography, relying on group theory, modular arithmetic, and number theory.

---
**C implementation of Elliptic Curve Scalar Multiplication**, which is the significant for **ECDSA** (Elliptic Curve Digital Signature Algorithm) and **ECC cryptography**.

Understanding required for the following code:
* A curve over a finite field: $y^2 = x^3 + ax + b \mod p$
* Modular inverse function
* Point addition
* Point doubling
* **Scalar multiplication**: Implements the optimized double-and-add method.
* **Finite field math**: Carefully handles negative mods and modular inverses.
* **Point-at-infinity logic**: Needed to model the elliptic curve group correctly.
* **C language**: Required for handling of edge cases and arithmetic.
---
