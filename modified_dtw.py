from dtw import *

def compute_dtw(self, X, Y):
    alignment = dtw(x=X, y=Y, dist_method="euclidean", keep_internals=True)
    d = alignment.distance.item()
    del alignment
    return d