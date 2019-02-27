
def modular(x, y, p):
    for i in range(1,100):
        if (y**i - x) % p == 0:
            return i

print(modular(1,177*113,250))