# generate_data.py
import numpy as np

def generate_option_data(num_samples, S_min, S_max, K_min, K_max, r_min, r_max, sigma_min, sigma_max, T_min, T_max):
    S = np.random.uniform(S_min, S_max, num_samples)
    K = np.random.uniform(K_min, K_max, num_samples)
    r = np.random.uniform(r_min, r_max, num_samples)
    sigma = np.random.uniform(sigma_min, sigma_max, num_samples)
    T = np.random.uniform(T_min, T_max, num_samples)
    return S, K, r, sigma, T
