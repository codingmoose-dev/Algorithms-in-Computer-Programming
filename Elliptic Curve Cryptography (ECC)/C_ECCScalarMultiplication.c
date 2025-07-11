#include <stdio.h>
#include <stdlib.h>

typedef struct {
    long long x;
    long long y;
    int is_infinity;
} ECPoint;

typedef struct {
    long long a;
    long long b;
    long long p; // Prime modulus
} ECCurve;

// Modular inverse using Extended Euclidean Algorithm
long long modinv(long long a, long long p) {
    long long t = 0, newt = 1;
    long long r = p, newr = a;

    while (newr != 0) {
        long long quotient = r / newr;
        long long temp;

        temp = newt;
        newt = t - quotient * newt;
        t = temp;

        temp = newr;
        newr = r - quotient * newr;
        r = temp;
    }

    if (r > 1) {
        printf("No inverse!\n");
        exit(1);
    }

    if (t < 0)
        t += p;

    return t;
}

long long mod(long long a, long long p) {
    long long res = a % p;
    return (res < 0) ? res + p : res;
}

ECPoint ec_add(ECCurve curve, ECPoint P, ECPoint Q) {
    if (P.is_infinity) return Q;
    if (Q.is_infinity) return P;

    if (P.x == Q.x && (P.y != Q.y || P.y == 0)) {
        ECPoint R = {0, 0, 1};
        return R;
    }

    long long m;
    if (P.x == Q.x && P.y == Q.y) {
        long long num = 3 * P.x * P.x + curve.a;
        long long den = 2 * P.y;
        m = mod(num * modinv(den, curve.p), curve.p);
    } else {
        long long num = Q.y - P.y;
        long long den = Q.x - P.x;
        m = mod(num * modinv(den, curve.p), curve.p);
    }

    long long x_r = mod(m * m - P.x - Q.x, curve.p);
    long long y_r = mod(m * (P.x - x_r) - P.y, curve.p);

    ECPoint R = {x_r, y_r, 0};
    return R;
}

ECPoint ec_scalar_mult(ECCurve curve, ECPoint P, long long k) {
    ECPoint result = {0, 0, 1};
    ECPoint addend = P;

    while (k > 0) {
        if (k & 1) {
            result = ec_add(curve, result, addend);
        }
        addend = ec_add(curve, addend, addend);
        k >>= 1;
    }

    return result;
}

int main() {
    ECCurve curve = {2, 3, 97}; // y^2 = x^3 + 2x + 3 mod 97
    ECPoint G = {3, 6, 0};      // Generator point

    long long k = 20;
    ECPoint result = ec_scalar_mult(curve, G, k);

    if (!result.is_infinity)
        printf("%lld * G = (%lld, %lld)\n", k, result.x, result.y);
    else
        printf("%lld * G = Point at Infinity\n", k);

    return 0;
}
