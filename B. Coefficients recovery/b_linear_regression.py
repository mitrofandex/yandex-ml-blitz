import numpy as np

X = []
ys = []
with open('data.txt') as file:
    for line in file:
        x, y = map(float, line.split())
        ys.append(y)

        features = [np.sin(x)**2, np.sin(x)*np.log(x), np.log(x)**2, x**2]
        X.append(features)

X = np.array(X)
ys = np.array(ys)

theta = np.linalg.inv(np.dot(X.T, X)).dot(X.T).dot(ys)

a = np.sqrt(theta[0])
b = np.sqrt(theta[2])
c = theta[3]

print(f'{theta[1]:.2f} {2*a*b:.2f}')
print(f'{a:.2f} {b:.2f} {c:.2f}')
