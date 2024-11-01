def ssquare(n, sumxsqr, sumx):
    value = (sumxsqr - ((sumx**2)/n))/(n-1)
    return value

def solve(x: list[float], y: list[float], fTab: float):
    n1 = len(x)
    n2 = len(y)
    sumx1 = sum(x)
    sumx2 = sum(y)
    sqr1 = [xv**2 for xv in x]
    sqr2 = [yv**2 for yv in y]
    sumxsqr1 = sum(sqr1)
    sumxsqr2 = sum(sqr2)
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
    
x = [12.29, 12.25, 11.86, 12.13, 12.44, 12.78, 12.77, 11.90, 12.47]
y = [12.39, 12.46, 12.34, 12.22, 11.98, 12.46, 12.23, 12.06]
ftab = 3.73 
answer = solve(x, y, ftab)
print(answer)