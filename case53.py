

 53. Food Waste Monitoring System

 AIM:
To compare prepared meals, meals served, and leftovers over several days, calculate wastage percentages, and identify days exceeding the acceptable waste limit.

OBJECTIVES:
- Record daily food preparation and consumption.
- Calculate leftover quantities.
- Calculate food wastage percentages.
- Identify days where wastage exceeds the permitted limit.

ALGORITM:
1. Store prepared and served meals for each day.
2. Calculate leftovers as prepared minus served.
3. Calculate wastage percentage.
4. Compare the percentage with the acceptable limit.
5. Display days exceeding the limit.

PSEUDO CODE:
```text
START
INPUT daily food data
FOR each day
    leftovers = prepared - served
    wastage_percentage = leftovers / prepared * 100
    IF wastage_percentage > limit
        DISPLAY "Exceeds limit"
    END IF
END FOR
STOP
```

SOURCE CODE:
```python
food_data = [
    ("Monday", 500, 450),
    ("Tuesday", 600, 510),
    ("Wednesday", 550, 520),
    ("Thursday", 700, 600),
    ("Friday", 650, 620)
]

limit = 10

print("Food Waste Report")

for day, prepared, served in food_data:
    leftovers = prepared - served
    percentage = (leftovers / prepared) * 100

    print(f"{day}: Prepared={prepared}, Served={served}, "
          f"Leftover={leftovers}, Waste={percentage:.2f}%")

    if percentage > limit:
        print("  Status: EXCEEDS ACCEPTABLE LIMIT")
    else:
        print("  Status: Within acceptable limit")
