import json

policy = {
        "policy_number": "POL1001",
        "customer_name": "Sneha",
        "premium": 25000,
        "status": "Active"
    }
with open("policies.json", "w") as file:
    json.dump(policy, file)