def last_chair(n):
    return n - 1
def soln(n):
    lst = [0 for i in range(n)]
    lst[0], lst[-1], count = 1, 2, 3
    ind = -1
    while count <= n:
        maxdist = -1
        coord = (-1, -1)
        lo, hi = 0, 1
        while hi < n:
            if lst[hi]:
                temp = hi - lo
                if temp > maxdist:
                    maxdist = temp
                    coord = (lo, hi)
                lo = hi
            hi += 1
        lo, hi = coord
        lst[(lo+hi)//2] = count
        if count == n:
            ind = (lo+hi)//2
        count += 1
    return lst 