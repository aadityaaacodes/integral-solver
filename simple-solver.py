
def callFunc(x):
    return(x**1)

def rightSum():
    pass

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


print(leftSum(a=0, b=10, n=1))


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

