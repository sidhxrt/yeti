def ssquare(n, sumxsqr, sumx):
    value = (sumxsqr - ((sumx**2)/n))/(n-1)
    return value

def solve(x: list[float], y: list[float], fTab: float):
    n1 = len(x)
    n2 = len(y)
    sumx1 = sum(x)
    sumx2 = sum(y)
    sumxsqr1 = [x**2 for xv in x]
    sumxsqr2 = [y**2 for yv in y]
    s1sq = ssquare(n1, sumxsqr1, sumx1)
    s2sq = ssquare(n2, sumxsqr2, sumx2)
    if s1sq > s2sq:
        fCal = s1sq/s2sq
    else:
        fCal = s2sq/s1sq
    if fCal <= fTab:
        return "there is not much variance in both"
    else:
        return "there is variance in both"