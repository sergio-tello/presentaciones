import matplotlib.pyplot as plt
import numpy as np

def expmodN(a, N, x):
    if x == 0:
        return 1
    else:
        return (a * (expmodN(a, N, x-1))) % N


a = 6
N = 91
Rango = 40

x = []
y = []
for i in range(Rango):
    x.append(i)
    y.append(i)


for i in range(len(x)):
    y[i] = expmodN(a, N, x[i])

labels = []
for k in range(Rango):
    labels.append(k)
    
index = np.arange(len(labels))
plt.figure(figsize=(14,6))
plt.bar(x, y, color='sandybrown')
plt.xlabel('x')
plt.ylabel(str(a)+'^x')
plt.xticks(index, labels, rotation=0)
plt.title('Valor de '+ str(a)+ '^x MOD '+ str(N))
plt.show()


