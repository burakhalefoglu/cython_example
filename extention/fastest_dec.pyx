from performance import performance_aspect


cdef inner(int i):
    return i + 1


@performance_aspect
def outer_4(int n):
    cdef int x = 0
    cdef int i = 0
    for i in range(n):
        x = inner(x)
