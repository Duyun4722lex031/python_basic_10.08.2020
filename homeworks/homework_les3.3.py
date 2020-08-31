
def my_funk(x, y):
    x = float(x)
    y = int(y)
    a = 0
    n = 1
    a = x
    while n < abs(y):
        a *= x
        n += 1
    if y < 0:
        print(1 / a)
    else:
        print(a)
if __name__ == '__main__':
    my_funk(2, -2)