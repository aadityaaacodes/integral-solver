def callFunc(x):
    return(x**1)

def rightSum(a, b, n):
    dx = (b-a)/n
    sum = 0
    term = 0
    i = 0
    while i<=(b-dx):
        term = callFunc(i)
        sum += (term*dx)
        i+=dx
    return(sum)

def leftSum(a, b, n):
    dx = (b-a)/n
    sum = 0
    term = 0
    i = a
    while i<=b:
        term = callFunc(i)
        sum += (term*dx)
        i+=dx
    return(sum)

def polynomial(deg, x):
    return((x**deg+1)/deg+1)

x = 3.14
dx = 0.00000000000000001
func = "x^2"

a = 0
b = 4
sum = 0
term = 0
deg = int(func[2])

def main():
    n = 1
    l = leftSum(a=0, b=10, n=n)
    r = rightSum(a=0, b=10, n=n)
    while l - r > 0.01:
        n +=1
        l = leftSum(a=0, b=10, n=n)
        r = rightSum(a=0, b=10, n=n)
    print((l+r)/2)

if __name__ == "__main__":
    main()