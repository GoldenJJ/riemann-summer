def f(x):
    return 2*x

def integrate(func, width, start, end):
    area = 0
    current = 0
    while current < (end-start):
        area += width * func(start+current)
        current += width
        #print(area)
    return area


print(integrate(f, 0.0000001, 0, 0.5))