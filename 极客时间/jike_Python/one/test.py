import date_time

date_time.date()
date_time.time()





# pip3 install matplotlib

import matplotlib.pyplot as plot

x = [1, 2, 3]
y = [4, 5, 6]
plot.plot(x, y, marker='o')
plot.plot(y, x, marker='x')
plot.show()






import sympy

n = sympy.Symbol('n')
print(sympy.limit((1+1/n)**n,n,sympy.oo))



