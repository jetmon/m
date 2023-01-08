import numpy as np

X = np.array(([1,9],[2,8],[3,6]),dtype=float)
X = X / np.amax(X, axis=0)

Y = np.array(([86],[89],[92]), dtype=float)
Y = Y / 100

def sig(x):
    return 1/1 + np.exp(-x)


def dsig(x):
    return x * (1 - x)

epoch = 7000
iln = 2
hln = 3
oln = 1
lr = 0.1

wh = np.random.uniform(size=(iln,hln))
bh = np.random.uniform(size=(1,hln))

wout = np.random.uniform(size=(hln,oln))
bout = np.random.uniform(size=(1,oln))

for i in range(epoch):
    # FWP
    HIP1 = np.dot(X, wh)
    HIP = HIP1 + bh
    HLA = sig(HIP)
    
    OUI1 = np.dot(HLA, wout)
    OUI = OUI1 + bout
    OUT = sig(OUI)
    
    # BWP
    EO = Y - OUT
    OG = dsig(OUT)
    DOUT = EO * OG
    
    EH = DOUT.dot(wout.T)
    HG = dsig(HLA)
    DHL = EH * HG
    
    wout += HLA.T.dot(DOUT) * lr
    wh += X.T.dot(DHL) *lr

print(f"{str(X)}\n\n{str(Y)}\n\n{OUT}")