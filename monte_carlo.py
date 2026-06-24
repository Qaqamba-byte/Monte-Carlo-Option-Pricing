import numpy as np
import matplotlib.pyplot as plt

# Parameters
# -----------------------
S0 = 100
days = 252
dt = 1 / days

mu = 0.10
sigma = 0.2

num_paths = 1000

np.random.seed(42)

# -----------------------
# Simulation storage
# -----------------------
paths = np.zeros((days, num_paths))

# -----------------------
# Simulation loop

for j in range(num_paths):
    prices = [S0]

    for i in range(days):
        Z = np.random.normal(0, 1)

        S_next = prices[-1] * np.exp(
            (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z
        )

        prices.append(S_next)

    paths[:, j] = prices[1:]

# -----------------------
# Plot results
# -----------------------
plt.figure(figsize=(10,6))

for j in range(50):  # plot only 50 paths for clarity
    plt.plot(paths[:, j], alpha=0.6)

plt.title("Monte Carlo Simulation - 1000 Price Paths")
plt.xlabel("Days")
plt.ylabel("Price")

plt.show()

# -----------------------
# Final prices (last row)
# -----------------------
final_prices = paths[-1, :]

# 1. Expected value
expected_price = np.mean(final_prices)

# 2. Risk range (5% and 95%)
lower_bound = np.percentile(final_prices, 5)
upper_bound = np.percentile(final_prices, 95)

# 3. Probability of loss
prob_loss = np.mean(final_prices < S0)

print("\n--- Simulation Results ---")
print("Expected Final Price:", expected_price)
print("5% Worst Case:", lower_bound)
print("95% Best Case:", upper_bound)
print("Probability of Loss:", prob_loss)

# -----------------------
# Option Parameters
# -----------------------
strike_price = 105

# Call option payoff
payoffs = np.maximum(final_prices - strike_price, 0)

# Discount factor (risk-free rate approximation)
r = 0.05
T = 1  # 1 year

option_price = np.exp(-r * T) * np.mean(payoffs)

print("\n--- Option Pricing ---")
print("Call Option Price:", option_price)
