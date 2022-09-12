from dtw import *

def compute_dtw(X, Y):
    alignment = dtw(x=X, y=Y, dist_method="euclidean", keep_internals=True)
    d = alignment.distance.item()
    del alignment
    return d

def compute_dtw_series(X, Y):
    alignment = dtw(x=X, y=Y, dist_method="euclidean", keep_internals=True)
    index1 = alignment.index1
    index2 = alignment.index2
    time_series = []
    for i in range(len(index1)):
        ans = int(X[index1[i]] - Y[index2[i]])
        time_series.append(ans)

    return time_series