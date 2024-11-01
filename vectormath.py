def cosine_sim(x, y):
    if(len(x) == len(y)):
        sum = 0
        xsq = 0
        ysq = 0
        for i in range(len(x)):
            sum = sum + (x[i]*y[i])
            xsq = xsq + (x[i]**2)
            ysq = ysq + (y[i]**2)
        X = xsq ** 0.5
        Y = ysq ** 0.5
        return sum/(X*Y)
    
def cosine_dist(x, y):
    return 1 - cosine_sim(x, y)
    
def euclidean_dist(x, y):
    if(len(x) == len(y)):
        sum = 0
        for i in range(len(x)):
           sum = sum + ((x[i] - y[i])**2)
        return sum**0.5 
    
