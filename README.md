# Monte Carlo Simulation for Stock Prices & Option Pricing

## Overview
This project uses Monte Carlo simulation and Geometric Brownian Motion (GBM) to model stock price movements and price a European call option.

## What the project does
- Simulates stock price paths using Geometric Brownian Motion (GBM)
- Generates 1,000+ possible future price scenarios
- Models uncertainty in financial markets
- Estimates expected price distribution and risk
- Prices a European call option using Monte Carlo simulation

## Key Financial Concept
Stock prices are modelled using:

S(t) = S₀ · exp((μ − ½σ²)t + σWₜ)

This is a standard model used in quantitative finance for modelling stochastic price movements.

## Key Outputs
- Simulated stock price paths
- Expected final price
- Probability of loss
- European call option price

## Tools Used
Python, NumPy, Matplotlib

## Author
Qaqamba Mantyi