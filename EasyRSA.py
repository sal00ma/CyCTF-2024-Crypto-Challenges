from math import isqrt
from Crypto.Util.number import inverse
from Crypto.Util.number import long_to_bytes

# Given values (from your problem)
n = 114854551330746397263129982993756672657425665771296671706881645320578363250243895226947831737322408833284681636047594518253291485879906145940472873445092221773018178739139004177782457591466204757132843475741546364257477113473112678957000007604967008813948365220245465505883904012403529645409736792173273303687
ct = 63507487928240228617823698638510022797445924776203856776680617881005872428429025266825025046271350969720992923461926687931939109009819903377585105294225690945299837607033204795370884314323845934909409636360280104617531753610201377770302845036579992253661784282511949065277256787648221213870389940118236802795
e = 65537

# Function to check if the discriminant is a perfect square
def is_perfect_square(x):
    s = isqrt(x)
    return s * s == x

# Brute-force k and solve for p and q
for k in range(1, 100):  # Try small values of k
    discriminant = e**2 - 4 * k * n
    if discriminant >= 0 and is_perfect_square(discriminant):
        # Compute q using the quadratic formula
        sqrt_disc = isqrt(discriminant)
        q1 = (e + sqrt_disc) // (2 * k)
        q2 = (e - sqrt_disc) // (2 * k)

        # Check if q1 or q2 is a valid factor of n
        if n % q1 == 0:
            q = q1
        elif n % q2 == 0:
            q = q2
        else:
            continue

        # Compute p
        p = n // q
        
        # Check if both p and q are prime
        if p != q and p > 1 and q > 1:
            print(f"Found factors: p = {p}, q = {q}")
            # Compute phi(n)
            phi_n = (p - 1) * (q - 1)
            # Compute the private key d
         
            d = inverse(e, phi_n)
        print(f"{d = }")
print(long_to_bytes(pow(ct,d,n)))
            
