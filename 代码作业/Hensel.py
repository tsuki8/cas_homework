from sympy import *
from sympy import FiniteField

Z3=FiniteField(3)
x = symbols('x')
A=Poly(x**4-394*x**3-4193*x**2+126*x+596)
B0=Poly(x**2+x+1)
C0=Poly(x**2+x-1)
Bk=B0
Ck=C0
E0=A-B0*C0
U=-1
V=1
print(E0)
M=2**4*sqrt(5)*4193
p=3
k=0
Ek=Poly(E0,domain='ZZ')
while p**k<2*M:
    DB0=Poly(Ek , domain='ZZ') * V/p**(k+1)
    DC0=Poly(Ek , domain='ZZ') * U/p**(k+1)
    q1, DB1 = div(DB0, B0, domain=Z3)
    q2, DC1 = div(DC0, C0, domain=Z3)
    Bk = Bk + Poly(DB1, domain='ZZ')*p**(k+1)
    Ck = Ck + Poly(DC1, domain='ZZ')*p**(k+1)
    print(f"Bk:{Bk}")
    print(f"Ck:{Ck}")
    k=k+1
    Ek=A-Bk*Ck
    print(f"k={k},Ek:{Ek}")
    if Ek==0:
        print(f"Bk:{Bk}")
        print(f"Ck:{Ck}")
        print("success")
        break

print("NULL")


