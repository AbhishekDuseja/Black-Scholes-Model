# plotting.py
import matplotlib.pyplot as plt
from black_scholes import black_scholes_call, black_scholes_put, black_scholes_delta, black_scholes_gamma

def plot_option_prices(S, K, r, sigma, T):
    call_prices = black_scholes_call(S, K, r, sigma, T)
    put_prices = black_scholes_put(S, K, r, sigma, T)
    
    plt.figure(figsize=(12, 6))
    plt.plot(S, call_prices, 'bo', label='Call Option Prices')
    plt.plot(S, put_prices, 'ro', label='Put Option Prices')
    plt.title('Option Prices using Black-Scholes Model')
    plt.xlabel('Underlying Asset Price (S)')
    plt.ylabel('Option Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_greeks(S, K, r, sigma, T):
    deltas_call = black_scholes_delta(S, K, r, sigma, T, option_type='call')
    deltas_put = black_scholes_delta(S, K, r, sigma, T, option_type='put')
    gamma = black_scholes_gamma(S, K, r, sigma, T)
    
    plt.figure(figsize=(12, 6))
    plt.plot(S, deltas_call, 'bo', label='Call Delta')
    plt.plot(S, deltas_put, 'ro', label='Put Delta')
    plt.plot(S, gamma, 'go', label='Gamma')
    plt.title('Option Greeks using Black-Scholes Model')
    plt.xlabel('Underlying Asset Price (S)')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()



# plotting.py
# import matplotlib.pyplot as plt
# from black_scholes import black_scholes_call, black_scholes_put, black_scholes_delta, black_scholes_gamma

# def plot_option_prices(S, K, r, sigma, T):
#     call_prices = black_scholes_call(S, K, r, sigma, T)
#     put_prices = black_scholes_put(S, K, r, sigma, T)
    
#     plt.figure(figsize=(12, 6))
#     plt.plot(S, call_prices, 'bo', label='Call Option Prices')
#     plt.title('Call Option Prices using Black-Scholes Model')
#     plt.xlabel('Underlying Asset Price (S)')
#     plt.ylabel('Option Price')
#     plt.legend()
#     plt.grid(True)
#     plt.tight_layout()

#     return plt

# def plot_greeks(S, K, r, sigma, T):
#     deltas_call = black_scholes_delta(S, K, r, sigma, T, option_type='call')
#     deltas_put = black_scholes_delta(S, K, r, sigma, T, option_type='put')
#     gamma = black_scholes_gamma(S, K, r, sigma, T)
    
#     plt.figure(figsize=(12, 6))
#     plt.plot(S, deltas_call, 'bo', label='Call Delta')
#     plt.plot(S, deltas_put, 'ro', label='Put Delta')
#     plt.plot(S, gamma, 'go', label='Gamma')
#     plt.title('Option Greeks using Black-Scholes Model')
#     plt.xlabel('Underlying Asset Price (S)')
#     plt.ylabel('Value')
#     plt.legend()
#     plt.grid(True)
#     plt.tight_layout()

#     return plt





