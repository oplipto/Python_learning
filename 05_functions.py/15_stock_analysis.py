def price_at(x):
    """Finds the price on a given day x."""
    prices = [50, 52, 55, 53, 56, 58, 57, 60, 62, 65, 63, 66, 68, 70, 72, 71, 73, 75, 77, 76]  # Sample prices
    if 1 <= x <= 20:
        return prices[x - 1]
    else:
        return None  # Return None if the day is out of range


def max_price(a, b):
    """Finds the maximum price from day a to day b."""
    prices = [50, 52, 55, 53, 56, 58, 57, 60, 62, 65, 63, 66, 68, 70, 72, 71, 73, 75, 77, 76]  # Sample prices
    if 1 <= a <= 20 and 1 <= b <= 20:
        return max(prices[a - 1:b])
    else:
        return None  # Return None if any of the days is out of range


def min_price(a, b):
    """Finds the minimum price from day a to day b."""
    prices = [50, 52, 55, 53, 56, 58, 57, 60, 62, 65, 63, 66, 68, 70, 72, 71, 73, 75, 77, 76]  # Sample prices
    if 1 <= a <= 20 and 1 <= b <= 20:
        return min(prices[a - 1:b])
    else:
        return None  # Return None if any of the days is out of range


# Testing the functions
print("Price on day 5:", price_at(5))
print("Maximum price from day 3 to day 10:", max_price(3, 10))
print("Minimum price from day 12 to day 18:", min_price(12, 18))
