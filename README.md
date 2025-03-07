# Stock Trading Engine

This repository contains an implementation of a real-time stock trading engine that matches buy and sell orders based on price and quantity.

## Features
- Supports up to 1,024 ticker symbols
- Uses a sorted list-based order book (without dictionaries/maps)
- Ensures O(n) time complexity for order matching
- Handles concurrency with a lock-free approach

