def fibanocii(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b, a+b

a = int(input("Enter Range:"))

for i in fibanocii(a):
    print(i)
