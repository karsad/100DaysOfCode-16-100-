def add_num(*args):
    sum_ret = 0
    for num in args:
        sum_ret += num
    print(sum_ret)

add_num(3, 5, 9, 12, 11)

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    return n


print(calculate(10, add=3, multiply=5))