# Calculate values
def calculate_change(open_price, close_price):
    """Return the price change (close - open)."""
    return close_price - open_price


def calculate_percent_change(open_price, close_price):
    """Return the percent change relative to the opening price."""
    change = close_price - open_price
    return (change / open_price) * 100


# Decide
def get_market_status(change):
    """Return GAIN, LOSS, or NO CHANGE based on the price change."""
    if change > 0:
        return "GAIN"
    elif change < 0:
        return "LOSS"
    else:
        return "NO CHANGE"


# Display
def display_summary(stock_name, open_price, close_price,
                    change, percent_change, status):
    """Print the daily stock summary."""
    print()
    print("DAILY STOCK SUMMARY")
    print("Stock:", stock_name)
    print("Opening Price:", open_price)
    print("Closing Price:", close_price)
    print("Price Change:", change)
    print("Percent Change:", percent_change, "%")
    print("Status:", status)


# Main program
def main():
    print("Welcome to the Daily Stock Analyzer!")

    stock_name = input("Enter stock name: ")
    open_price = float(input("Enter opening price: "))
    close_price = float(input("Enter closing price: "))

    change = calculate_change(open_price, close_price)
    percent_change = calculate_percent_change(open_price, close_price)
    status = get_market_status(change)

    display_summary(stock_name, open_price, close_price,
                    change, percent_change, status)


main()
