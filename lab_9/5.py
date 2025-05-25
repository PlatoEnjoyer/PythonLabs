import numpy as np
from scipy.stats import multivariate_normal
from scipy.linalg import det, inv
import time

def log_multivariate_normal_pdf(X, m, C):
    D = len(m)
    N = X.shape[0]
    log_pdf = np.zeros(N)
    
    log_2pi = np.log(2 * np.pi)
    log_det_C = np.log(det(C))
    inv_C = inv(C)
    X_centered = X - m
    
    for i in range(N):
        x_centered = X_centered[i]
        quad_form = x_centered.T @ inv_C @ x_centered
        log_pdf[i] = -0.5 * (D * log_2pi + log_det_C + quad_form)
    
    return log_pdf

D = 3
N = 1000
m = np.array([1.0, 2.0, 3.0])
C = np.array([[2.0, 0.5, 0.3],
              [0.5, 1.0, 0.2],
              [0.3, 0.2, 1.5]])
X = np.random.multivariate_normal(m, C, size=N) 

start_time = time.time()
our_logpdf = log_multivariate_normal_pdf(X, m, C)
our_time = time.time() - start_time

start_time = time.time()
scipy_logpdf = multivariate_normal(m, C).logpdf(X)
scipy_time = time.time() - start_time

difference = np.max(np.abs(our_logpdf - scipy_logpdf))
print(f"Максимальное расхождение: {difference:.2e}")
print(f"Наша реализация: {our_time:.5f} сек")
print(f"Scipy: {scipy_time:.5f} сек")