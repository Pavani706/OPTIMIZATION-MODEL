# Step 1: Install PuLP if not already installed
# !pip install pulp

from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, value

# Step 2: Define data
cities = ['A', 'B', 'C']
demands = {'A': 100, 'B': 80, 'C': 120}
distances = {'A': 30, 'B': 50, 'C': 70}
cost_per_km_per_package = 2  # e.g., Rs.2 per km per package

trucks = ['T1', 'T2']
truck_capacities = {'T1': 150, 'T2': 200}

# Cost matrix: (truck, city) → cost
cost = {(t, c): distances[c] * cost_per_km_per_package for t in trucks for c in cities}

# Step 3: Define LP Problem
model = LpProblem("Delivery_Route_Optimization", LpMinimize)

# Step 4: Define Variables
x = LpVariable.dicts("deliver", [(t, c) for t in trucks for c in cities], lowBound=0, cat='Integer')

# Step 5: Objective Function - Minimize total delivery cost
model += lpSum(x[t, c] * cost[t, c] for t in trucks for c in cities)

# Step 6: Constraints

# Demand constraint: demand at each city must be met
for c in cities:
    model += lpSum(x[t, c] for t in trucks) >= demands[c], f"Demand_{c}"

# Truck capacity constraint: each truck cannot exceed its capacity
for t in trucks:
    model += lpSum(x[t, c] for c in cities) <= truck_capacities[t], f"Capacity_{t}"

# Step 7: Solve
model.solve()

# Step 8: Print Results
print("Status:", LpStatus[model.status])
print("Total Cost:", value(model.objective))

print("\nPackage Distribution Plan:")
for t in trucks:
    for c in cities:
        qty = x[t, c].varValue
        if qty > 0:
            print(f"Truck {t} → City {c}: {int(qty)} packages")
