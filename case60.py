

# 60. Manufacturing Quality Control Matrix

## Aim
To analyse production quantities and defective units across products and batches, calculate defect percentages, and identify batches exceeding quality thresholds.

## Objectives
- Store production and defect information in a matrix.
- Calculate defect percentages.
- Compare defect percentages with the quality threshold.
- Identify products or batches requiring attention.

## Algorithm
1. Store production and defective quantities.
2. Calculate defect percentage for every batch.
3. Compare the percentage with the specified threshold.
4. Mark batches exceeding the threshold.
5. Display the quality report.

## Pseudocode
```text
START
INPUT production matrix
INPUT defect matrix
INPUT defect threshold

FOR each product
    FOR each batch
        defect_percentage = defects / production * 100

        IF defect_percentage > threshold
            MARK "QUALITY VIOLATION"
        ELSE
            MARK "ACCEPTABLE"
        END IF
    END FOR
END FOR

DISPLAY quality report
STOP
```

## Source Code
```python
products = ["Product A", "Product B", "Product C"]

production = [
    [1000, 1200, 1100],
    [800, 900, 1000],
    [1500, 1400, 1600]
]

defects = [
    [20, 50, 15],
    [40, 30, 25],
    [60, 35, 80]
]

threshold = 4

print("Manufacturing Quality Control Report")

for i in range(len(products)):
    print("\n", products[i])

    for j in range(len(production[i])):
        produced = production[i][j]
        defective = defects[i][j]

        percentage = (defective / produced) * 100

        if percentage > threshold:
            status = "QUALITY VIOLATION"
        else:
            status = "ACCEPTABLE"

        print(
            f"Batch {j + 1}: Production={produced}, "
            f"Defects={defective}, "
            f"Defect%={percentage:.2f}%, "
            f"{status}"
        )
