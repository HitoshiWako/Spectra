import numpy as np
def peak(x):
#　リストからピークとボトムの位置を見つけ
#　その位置と両側の区切り（ピークであればボトム，ボトムであればピーク）を
#　返す。（端であれば，リストの両端を使う）

    c = np.sign(np.diff(x))
    c1 = np.append(0,c)
    c2 = np.append(c,0)
    p = np.where((c1 > 0) & (c2 < 0))[0].tolist()
    v = np.where((c1 < 0) & (c2 > 0))[0].tolist()

    bp = p
    bv = v
    
    if p[0] < v[0]:
        bv = [0] + bv
    else:
        bp = [0] + bp

    if p[-1] > v[-1]:
        bv = bv + [len(x)-1]
    else:
        bp = bp + [len(x)-1]

    pl = [(p[i],bv[i],bv[i+1]) for i in range(len(p))]
    vl = [(v[i],bp[i],bp[i+1]) for i in range(len(v))]
    
    return pl,vl
