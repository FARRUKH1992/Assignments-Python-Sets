# Flight routes of the two airlines
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# 1. Destinations that both airlines fly to (intersection)
shared_routes = our_routes.intersection(competitor_routes)
print(f"Destinations both airlines fly to: {shared_routes}")

# 2. Destinations  (difference)
unique_to_our_airline = our_routes.difference(competitor_routes)
print(f"Destinations unique to our airline: {unique_to_our_airline}")

# 3. Check if there are destinations  (symmetric difference)
neither_shared = our_routes.symmetric_difference(competitor_routes)
print(f"Destinations that neither airline shares: {neither_shared}")




# List of customer IDs with duplicates
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

# Convert the list to a set to remove duplicates
unique_customer_ids = set(customer_ids)

# Display the unique customer IDs
print(f"Unique customer IDs: {unique_customer_ids}")
