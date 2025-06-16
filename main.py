def initialize_stock_prices():
    """Initialize and return the dictionary of stock prices"""
    return {
        "AAPL": 180.50,   # Apple
        "TSLA": 250.75,   # Tesla
        "MSFT": 300.25,   # Microsoft
        "GOOGL": 135.40,  # Alphabet (Google)
        "AMZN": 150.60    # Amazon
    }

def get_user_portfolio(stock_prices):
    """Collect user input and build the portfolio"""
    portfolio = {}
    total_investment = 0.0
    
    print("\nAvailable stocks:", ", ".join(stock_prices.keys()))
    print("Enter 'done' when finished.\n")
    
    while True:
        stock_name = input("Enter stock symbol: ").strip().upper()
        
        if stock_name == 'DONE':
            break
            
        if stock_name not in stock_prices:
            print(f"Error: {stock_name} not found. Available stocks: {', '.join(stock_prices.keys())}")
            continue
            
        try:
            quantity = int(input(f"Enter quantity of {stock_name}: ").strip())
            if quantity <= 0:
                print("Quantity must be a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
            
        # Calculate stock value and add to portfolio
        stock_value = stock_prices[stock_name] * quantity
        portfolio[stock_name] = {
            'quantity': quantity,
            'price': stock_prices[stock_name],
            'value': stock_value
        }
        total_investment += stock_value
        
        print(f"Added {quantity} shares of {stock_name} at ${stock_prices[stock_name]:.2f} each (${stock_value:.2f} total)")
    
    return portfolio, total_investment

def display_portfolio(portfolio, total_investment):
    """Display the portfolio summary"""
    if not portfolio:
        print("\nYour portfolio is empty.")
        return
    
    print("\n--- Portfolio Summary ---")
    for stock, data in portfolio.items():
        print(f"{stock}: {data['quantity']} shares @ ${data['price']:.2f} = ${data['value']:.2f}")
    print(f"\nTotal Investment Value: ${total_investment:.2f}")

def save_portfolio_to_file(portfolio, total_investment):
    """Save portfolio to a file in CSV format"""
    while True:
        filename = input("\nEnter filename to save (e.g., portfolio.csv): ").strip()
        if not filename:
            print("Filename cannot be empty.")
            continue
            
        try:
            with open(filename, 'w') as file:
                file.write("Stock,Quantity,Price Per Share,Total Value\n")
                for stock, data in portfolio.items():
                    file.write(f"{stock},{data['quantity']},{data['price']:.2f},{data['value']:.2f}\n")
                file.write(f"Total,,,{total_investment:.2f}")
            print(f"Portfolio successfully saved to {filename}")
            break
        except Exception as e:
            print(f"Error saving file: {e}")
            retry = input("Would you like to try again? (y/n): ").lower()
            if retry != 'y':
                break

def main():
    print("=== Stock Portfolio Tracker ===")
    print("Track your investments and calculate total portfolio value\n")
    
    stock_prices = initialize_stock_prices()
    portfolio, total_investment = get_user_portfolio(stock_prices)
    display_portfolio(portfolio, total_investment)
    
    if portfolio:
        save_option = input("\nWould you like to save this portfolio? (y/n): ").lower()
        if save_option == 'y':
            save_portfolio_to_file(portfolio, total_investment)
    
    print("\nThank you for using Stock Portfolio Tracker!")

if __name__ == "__main__":
    main()