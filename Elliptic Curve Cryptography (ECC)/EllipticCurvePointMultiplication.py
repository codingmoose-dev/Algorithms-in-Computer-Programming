# Elliptic Curve over a Finite Field: y^2 = x^3 + ax + b mod p
# Elliptic curve point (scalar) multiplication using the double-and-add method.

class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b 
        self.p = p

        assert (4 * a**3 + 27 * b**2) % p != 0, "Singular curve!"

    def is_on_curve(self, P):
        if P is None:  # Point at infinity
            return True
        x, y = P
        return (y ** 2 - (x ** 3 + self.a * x + self.b)) % self.p == 0

    def inverse_mod(self, x):
        return pow(x, -1, self.p)

    def point_add(self, P, Q):
        if P is None: return Q
        if Q is None: return P
        x1, y1 = P
        x2, y2 = Q

        if x1 == x2 and y1 != y2:
            return None # Point at infinity

        if P == Q:
            s = (3 * x1 * x1 + self.a) * self.inverse_mod(2 * y1) % self.p # Point doubling
        else:
            s = (y2 - y1) * self.inverse_mod(x2 - x1) % self.p # Point addition

        x3 = (s * s - x1 - x2) % self.p
        y3 = (s * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def scalar_mult(self, k, P):
        result = None 
        addend = P

        while k:
            if k & 1:
                result = self.point_add(result, addend)
            addend = self.point_add(addend, addend)
            k >>= 1
        return result

a, b, p = 2, 3, 97  # Curve: y² = x³ + 2x + 3 mod 97
curve = EllipticCurve(a, b, p)

G = (3, 6)  # Base point (on the curve)
assert curve.is_on_curve(G), "Base point is not on the curve!"

k = 20
P = curve.scalar_mult(k, G)
print(f"{k} * G = {P}")
