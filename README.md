# Stock Trading Engine

This repository contains an implementation of a real-time stock trading engine that matches buy and sell orders based on price and quantity.

## Features
- Supports up to 1,024 ticker symbols
- Uses a sorted list-based order book (without dictionaries/maps)
- Ensures O(n) time complexity for order matching
- Handles concurrency with a lock-free approach

## Running the Code
To run the simulation, ensure you have Python installed (version **3.7+** recommended).

1. Clone the repository:
   ```sh
   git clone https://github.com/JoshuaLauu/stock-trading-engine.git
   cd stock-trading-engine
   ```
2. Run the trading engine:
   ```sh
   python trading_engine.py
   ```
3. The program will generate random buy and sell orders, and you will see executed trades in the console.

## Example Output
Trade executed: 50 shares of T123 at price 45.00

Trade executed: 20 shares of T789 at price 32.50

## Notes
- The program simulates real-time stock trading using multi-threading.
- You can modify the parameters in trading_engine.py to change the order flow.
