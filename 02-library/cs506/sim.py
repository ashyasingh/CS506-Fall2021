def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    sum = 0
    for i in range(len(x)):
        sum += abs(x[i]-y[i])
    return sum

def jaccard_dist(x, y):
    intersect = len(list(set(x).intersection(y)))
    union = (len(x) + len(y)) - intersect
    return intersect / union

def cosine_sim(x, y):
    return 1 - math.cos(x, y)
