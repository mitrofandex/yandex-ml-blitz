import numpy as np
import sys

X = []
y = []
n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    data = sys.stdin.readline().split()
    X.append(data[:m])
    y.append(data[-1])

X = np.array(X, float)
y = np.array(y, int).reshape(n, 1)

def Loss(X, w, y):
    return np.exp(- X.dot(w) * y).sum()

def Grad(X, w, y):
    return - np.dot((X*y).T, np.exp(- X.dot(w) * y))

def Model(X, y, n_iterations=100, learning_rate=0.1, verbose=10):
    w = np.zeros((m, 1))
    
    for i in range(n_iterations):
        loss = Loss(X, w, y)                
        grad = Grad(X, w, y)
        
        w -= learning_rate * grad
        
        if verbose and (i % verbose == 0):
            print('Iter: {}, Loss: {}'.format(i, loss))
                
    return w

w = Model(X, y, verbose=False)
print(*w.flatten())