# Monte Carlo Simulation for Option Pricing

Monte Carlo simulations are used extensively in finance to model and predict the behavior of financial instruments under various conditions. This technique is particularly useful for options pricing, where the future price of the underlying asset is uncertain.

## Concept

The Monte Carlo method involves generating random paths for the underlying asset price, calculating the payoff for each path at the end of the option's life, and then averaging these payoffs. By discounting the average payoff back to the present value using the risk-free rate, we obtain an estimate of the option's price.

### Parameters

- `s`: Initial spot price of the asset.
- `t`: Time to maturity of the option (in years).
- `r`: Risk-free discount rate.
- `sigma`: Volatility of the underlying asset.
- `nSimulations`: Number of paths to simulate.
- `nSteps`: Number of time steps in the simulation.
- `K`: Strike price of the option.

### Calculations

1. **Time Step Size (`dt`)**: This is calculated by dividing the total time to maturity by the number of steps.
2. **Drift and Diffusion**: These terms are derived from the risk-free rate, volatility, and time step size.
   - **Drift**: Adjusted mean of the asset returns.
   - **Diffusion**: Random component associated with the volatility.
3. **Simulation**: Generate asset prices for each time step using the geometric Brownian motion model.

## Python Code Explanation

```python
import numpy as np

# Input parameters
s = 100  # Initial spot price
t = 1    # Time to maturity
r = 0.07 # Risk-free discount rate
sigma = 0.2  # Volatility of the underlying asset
nSimulations = 5000  # Number of Monte Carlo simulations
nSteps = 250  # Number of time steps
K = 100  # Strike price

# Calculate the size of each time step
dt = t / nSteps

# Calculate drift and diffusion components
drift = (r - 0.5 * sigma**2) * dt
a = sigma * np.sqrt(dt)

# Generate random components for simulation
x = np.random.normal(0, 1, (nSimulations, nSteps))

# Initialize matrix to store simulated asset paths
sMat = np.zeros((nSimulations, nSteps))
sMat[:, 0] = s

# Generate asset prices for each simulation
for i in range(1, nSteps):
    sMat[:, i] = sMat[:, i-1] * np.exp(drift + a * x[:, i])

# Calculate the payoff for calls and puts
q = np.maximum(sMat[:, -1] - K, 0)
p = np.maximum(K - sMat[:, -1], 0)

# Average the payoffs across simulations
payOffCall = np.mean(q)
payOffPut = np.mean(p)

# Discount the average payoffs back to present value
call = payOffCall * np.exp(-r * t)
put = payOffPut * np.exp(-r * t)

# Print the results
print(f"Call Option Price: {call:.2f}")
print(f"Put Option Price: {put:.2f}")
