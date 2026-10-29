57.smart canteen order and stock management
AIM:
To process customer orders, calculate bills, update inventory, reject unavailable quantities, and generate a summary of daily sales and remaining stock.

OBJECTIVES:
- Maintain food item prices and stock.
- Process successive customer orders.
- Calculate customer bills.
- Reject orders when stock is insufficient.
- Calculate total daily sales.
- Display remaining inventory.

ALGORITHM:
1. Create an inventory containing item price and quantity.
2. Read customer orders.
3. Check whether the requested quantity is available.
4. If available, calculate the cost and update stock.
5. Otherwise, reject the order.
6. Add successful order values to daily sales.
7. Display sales and remaining stock.

PSEUDO CODE:
```text
START
CREATE inventory
SET total sales = 0

FOR each customer order
    CHECK stock
    IF sufficient stock
        CALCULATE bill
        REDUCE inventory
        ADD bill to sales
    ELSE
        REJECT order
    END IF
END FOR

DISPLAY total sales
DISPLAY remaining stock
STOP
```
               
flowchart TD:(mermaid)
    A([Start]) --> B[Initialize inventory and prices]
    B --> C[/Input customer order/]
    C --> D{Item exists?}
    D -- No --> E[Reject unavailable item]
    D -- Yes --> F{Sufficient stock?}
    F -- No --> G[Reject insufficient stock]
    F -- Yes --> H[Calculate bill]
    H --> I[Update stock and total sales]
    E --> J{More orders?}
    G --> J
    I --> J
    J -- Yes --> C
    J -- No --> K[/Display sales and remaining stock/]
    K --> L([Stop])


SOURCE CODE:
```python
inventory = {
    "Burger": {"price": 80, "stock": 10},
    "Pizza": {"price": 150, "stock": 5},
    "Juice": {"price": 40, "stock": 15},
    "Sandwich": {"price": 60, "stock": 8}
}

orders = [
    ("Customer 1", "Burger", 2),
    ("Customer 2", "Pizza", 2),
    ("Customer 3", "Juice", 5),
    ("Customer 4", "Pizza", 5),
    ("Customer 5", "Sandwich", 3)
]

total_sales = 0

for customer, item, quantity in orders:
    if item not in inventory:
        print(customer, ": Item not available")
        continue

    if inventory[item]["stock"] >= quantity:
        bill = inventory[item]["price"] * quantity
        inventory[item]["stock"] -= quantity
        total_sales += bill

        print(customer, "Bill =", bill)
    else:
        print(customer, ": Insufficient stock for", item)

print("\nDaily Sales:", total_sales)

print("\nRemaining Stock:")
for item, details in inventory.items():
    print(item, ":", details["stock"])
```

