# Input variables
days_until_expiration = 5  # Example value
stock_level = 60           # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"

if product_type == "Perishable":
    # 30% discount: ≤3 days AND stock > 50
    if days_until_expiration <= 3 and stock_level > 50:
        print("30% discount applied")
    # 20% discount: 4–6 days AND stock > 50
    elif 4 <= days_until_expiration <= 6 and stock_level > 50:
        print("20% discount applied")
    # 10% discount: >6 days OR stock ≤ 50
    elif days_until_expiration > 6 or stock_level <= 50:
        print("10% discount applied")
else:
    print("No discount available for non-perishable items.")