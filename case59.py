

# 59. Campus Transport Allocation

## Aim
To determine the number of buses required for different campus routes based on passenger demand and bus capacity and identify unserved passengers.

## Objectives
- Store route-wise passenger demand.
- Store bus capacities.
- Calculate the number of buses required.
- Determine total available capacity.
- Identify unserved passengers.

## Algorithm
1. Store passenger demand for each route.
2. Store the capacity of one bus.
3. Calculate buses required using ceiling division.
4. Calculate total capacity.
5. Compare capacity with demand.
6. Report unserved passengers if any.

## Pseudocode
```text
START
INPUT route demands
INPUT bus capacity

FOR each route
    buses = CEILING(demand / capacity)
    available capacity = buses * capacity
    unserved = MAX(0, demand - available capacity)
    DISPLAY route details
END FOR
STOP
```

## Source Code
```python
routes = {
    "Route A": 95,
    "Route B": 140,
    "Route C": 72,
    "Route D": 210
}

bus_capacity = 50

print("Campus Transport Allocation")

total_buses = 0

for route, demand in routes.items():
    buses = (demand + bus_capacity - 1) // bus_capacity
    capacity = buses * bus_capacity
    unserved = max(0, demand - capacity)

    total_buses += buses

    print(route)
    print("  Passenger Demand:", demand)
    print("  Buses Required:", buses)
    print("  Available Capacity:", capacity)
    print("  Unserved Passengers:", unserved)

print("\nTotal Buses Required:", total_buses)
