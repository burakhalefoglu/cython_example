from cpython.datetime cimport datetime, timedelta

cdef inner(int i):
    return i + 1


def outer_3(int n):
    cdef datetime start
    cdef datetime end
    cdef timedelta dt
    start = datetime.now()
    cdef int x = 0
    for i in range(n):
        x = inner(x)

    end = datetime.now()
    dt = end - start
    print("{:.12f}".format(dt.total_seconds()))
