def modInverse(ai, m):
    ai = ai % m
    for x in range(1, m):
        if (ai * x) % m == 1:
            return x
    return 1


def pointAdd(xpp, ypp, xqq, yqq):
    if (xpp == xqq) and (ypp == yqq):
        lam = ((3 * (xpp ** 2) + a) * (modInverse(2 * ypp, p))) % p
    else:
        lam = ((ypp - yqq) * (modInverse(xpp - xqq, p))) % p
    xrr = ((lam ** 2) - xpp - xqq) % p
    yrr = ((lam * (xpp - xrr)) - ypp) % p
    return xrr, yrr


def pointMul(xpp, ypp, sc):
    xrr = xpp
    yrr = ypp
    if sc >= 2:
        for i in range(0, sc - 1):
            xrr, yrr = pointAdd(xpp, ypp, xrr, yrr)
    return xrr, yrr


# INPUT STATEMENTS:
p = int(input("Enter the modulus value: "))
a = int(input("Enter the co-efficient 'a': "))
b = int(input("Enter the co-efficient 'b': "))
xp = int(input("Enter the x-coordinate of the first point: "))
yp = int(input("Enter the y-coordinate of the first point: "))
xq = int(input("Enter the x-coordinate of the second point: "))
yq = int(input("Enter the y-coordinate of the second point: "))
# POINT ADDITION:
xr, yr = pointAdd(xp, yp, xq, yq)
print("The sum is: p = (", xr, ",", yr, ") ")
# POINT MULTIPLICATION:
sca = int(input("Enter the scalar value: "))
xr, yr = pointMul(xp, yp, sca)
print("The product of ", sca, "p: (", xr, ",", yr, ") ")
