from scipy.special import cbrt
from scipy.special import exp10
from scipy.special import comb
from scipy.special import perm
from scipy.special import logsumexp
from scipy.special import jn
cb = cbrt([27, 64])
print(cb)
exp = exp10([1,10])
print(exp)
com = comb(5, 2, exact = False, repetition=True)
print(com)
per = perm(5, 2, exact = True)
print(per)
lb = logsumexp([27, 64])
print(lb)
lb1 = jn([1,2],[3,4])
print(lb1)

#scipy.special.logsumexp(x) 
#scipy.special.jn()
