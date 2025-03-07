import threading
import random
import time
from collections import deque


class Order:
    def __init__(self, order_type, ticker, quantity, price):
        self.order_type = order_type  # 'Buy' or 'Sell'
        self.ticker = ticker  # Stock symbol
        self.quantity = quantity  # Number of shares
        self.price = price  # Price per share


class OrderBook:
    def __init__(self):
        self.buy_orders = deque()  # Sorted in descending order of price
        self.sell_orders = deque()  # Sorted in ascending order of price
        self.lock = threading.Lock()

    def add_order(self, order):
        """Adds an order to the order book while maintaining sorted order."""
        with self.lock:
            if order.order_type == "Buy":
                self._insert_order(self.buy_orders, order, descending=True)
            else:
                self._insert_order(self.sell_orders, order, descending=False)

            self.match_order()

    def _insert_order(self, orders_list, order, descending):
        """Inserts an order in a sorted manner."""
        i = 0
        while i < len(orders_list) and (
        (order.price < orders_list[i].price) if descending else (order.price > orders_list[i].price)):
            i += 1
        orders_list.insert(i, order)

    def match_order(self):
        """Matches buy and sell orders."""
        with self.lock:
            while self.buy_orders and self.sell_orders and self.buy_orders[0].price >= self.sell_orders[0].price:
                buy_order = self.buy_orders.popleft()
                sell_order = self.sell_orders.popleft()

                trade_quantity = min(buy_order.quantity, sell_order.quantity)
                buy_order.quantity -= trade_quantity
                sell_order.quantity -= trade_quantity

                print(f"Trade executed: {trade_quantity} shares of {buy_order.ticker} at price {sell_order.price}")

                if buy_order.quantity > 0:
                    self.buy_orders.appendleft(buy_order)  # Reinsert remaining portion
                if sell_order.quantity > 0:
                    self.sell_orders.appendleft(sell_order)


# Simulating Stock Trading
order_book = OrderBook()


def random_order_simulation():
    tickers = [f"T{i}" for i in range(1024)]
    while True:
        order_type = random.choice(["Buy", "Sell"])
        ticker = random.choice(tickers)
        quantity = random.randint(1, 100)
        price = round(random.uniform(10, 500), 2)
        order = Order(order_type, ticker, quantity, price)
        order_book.add_order(order)
        time.sleep(random.uniform(0.1, 1.0))  # Simulate order flow


# Running order simulation in multiple threads
threads = [threading.Thread(target=random_order_simulation) for _ in range(5)]
for t in threads:
    t.start()
