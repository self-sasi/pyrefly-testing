def extracted_function(prices):
    total = 0
    for price in prices:
        total += price
    
    with_tax = total * 1.085
    return with_tax

def calculate_total_price(prices: list[int]) -> float:
    with_tax = extracted_function(prices)

    return with_tax
