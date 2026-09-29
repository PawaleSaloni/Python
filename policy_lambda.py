# A lambda function in Python is a small anonymous function.
# Lambda is a quick way of writing a small function without explicitly using def.

## lambda arguments: expression --------- lambada x : x+2
# List of dictionaries


policies = [
    {"policy_id": 1, "customer": "Ravi", "premium": 25000, "coverage":500000},
    {"policy_id": 2, "customer": "Saloni", "premium": 15000, "coverage":600000},
    {"policy_id": 3, "customer": "Amit", "premium": 50000, "coverage":100000},
    {"policy_id": 4, "customer": "Sneha", "premium": 20000, "coverage":900000},
    {"policy_id": 5, "customer": "Priya", "premium": 30000, "coverage":100000},
    {"policy_id": 6, "customer": "Sanika", "premium": 40000, "coverage":800000}   
]

# map()
discounted_policies = list(
    map(
        lambda p: {**p,"discounted_premium": p["premium"] * 0.90}, 
        policies
    )
)
print(discounted_policies)


# filter()
high_coverage = list(
    filter(
        lambda p: p["coverage"] > 100000,
        policies
    )
)
print(high_coverage)


# sorted()
sorted_policies = sorted(
    policies,
    key=lambda p: p["premium"],
    reverse=True
)

print(sorted_policies)
# ByDefault it will give in ascending order 