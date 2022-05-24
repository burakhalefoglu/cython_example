from performance import performance_aspect


def inner(i):
    return i + 1


@performance_aspect
def outer_1(n):
    x = 0
    for i in range(n):
        x = inner(x)
