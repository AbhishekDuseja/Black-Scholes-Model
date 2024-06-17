# main.py
from generate_data import generate_option_data
from black_scholes import black_scholes_call, black_scholes_put, black_scholes_delta, black_scholes_gamma
from plotting import plot_option_prices, plot_greeks

def main():
    num_samples = 100
    S_min, S_max = 50, 150
    K_min, K_max = 80, 120
    r_min, r_max = 0.01, 0.05
    sigma_min, sigma_max = 0.1, 0.3
    T_min, T_max = 0.25, 2.0
    
    S, K, r, sigma, T = generate_option_data(num_samples, S_min, S_max, K_min, K_max, r_min, r_max, sigma_min, sigma_max, T_min, T_max)
    
    plot_option_prices(S, K, r, sigma, T)
    plot_greeks(S, K, r, sigma, T)

if __name__ == "__main__":
    main()





# main.py
# from generate_data import generate_option_data
# from black_scholes import black_scholes_call, black_scholes_put, black_scholes_delta, black_scholes_gamma
# from plotting import plot_option_prices, plot_greeks

# def main():
#     num_samples = 100
#     S_min, S_max = 50, 150
#     K_min, K_max = 80, 120
#     r_min, r_max = 0.01, 0.05
#     sigma_min, sigma_max = 0.1, 0.3
#     T_min, T_max = 0.25, 2.0
    
#     S, K, r, sigma, T = generate_option_data(num_samples, S_min, S_max, K_min, K_max, r_min, r_max, sigma_min, sigma_max, T_min, T_max)
    
#     while True:
#         print("Choose an option:")
#         print("1. Plot Call Option Prices")
#         print("2. Plot Option Greeks (Delta and Gamma)")
#         print("0. Exit")
        
#         choice = input("Enter your choice: ")
        
#         if choice == '1':
#             plt_call = plot_option_prices(S, K, r, sigma, T)
#             plt_call.show()
#         elif choice == '2':
#             plt_greeks = plot_greeks(S, K, r, sigma, T)
#             plt_greeks.show()
#         elif choice == '0':
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice. Please enter 1, 2, or 0.")

# if __name__ == "__main__":
#     main()
