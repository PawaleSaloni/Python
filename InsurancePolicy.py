class InsurancePolicy:
    def __init__(self, policy_number):
        self.policy_number = policy_number


# Create policy object
policy = InsurancePolicy("POL1002")

# Before deleting
print("Before deleting:")
print(policy.policy_number)

# Delete the reference
del policy

# Try to access after deleting
print("\nAfter deleting:")

try:
   print(policy.policy_number)
except NameError:
    print("Policy does not exist.")