def calc_customer_return(base_customers, left_percent, interest_percent):
    # Convert percentage represented numbers to floats
    if left_percent.endswith('%'):
        left_percent = float(left_percent[:-1]) / 100
    else:
        left_percent = float(left_percent)
    
    if interest_percent.endswith('%'):
        interest_percent = float(interest_percent[:-1]) / 100
    else:
        interest_percent = float(interest_percent)

    # Calculate the potential return of customers
    potential_return = base_customers * left_percent * interest_percent / (1 - left_percent * interest_percent)
    return f"The potential range of customer return is from {potential_return / base_customers:.2%} to {potential_return:.2f}"

# Test the function with different inputs
print(calc_customer_return(100, "70%", "85%"))
print(calc_customer_return(500, 0.3, 0.75))
print(calc_customer_return(1000, "50%", 0.9))
