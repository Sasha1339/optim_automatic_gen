import gen_algorithm
from connect import connect, shim, draw

f_discret = 4000
f1 = 50
f2 = 51

pair = gen_algorithm.start(f_discret, f1, f2)
sig1, sig2 = connect(f_discret, f1, f2)
y, x = shim(f_discret, sig1, sig2, pair.get_K(), pair.get_T(), True)
print("K = " +str(pair.get_K())+", T = "+str(pair.get_T()))
draw(x, y)