

 55. Tuple-Based Transaction Audit

AIM:
To process transaction tuples containing identifiers, amounts, and transaction types and detect duplicate identifiers, invalid amounts, and suspicious transaction sequences.

OBJECTIVES:
- Process transaction data using tuples.
- Detect duplicate transaction identifiers.
- Identify invalid or negative transaction amounts.
- Detect suspicious consecutive transaction patterns.

ALGORITHM:
1. Store transactions as tuples.
2. Maintain a set of transaction identifiers.
3. Check each identifier for duplication.
4. Validate transaction amounts.
5. Examine consecutive transactions for suspicious patterns.
6. Display all audit violations.

PSEUDO CODE:
```text
START
INPUT transaction tuples
CREATE empty identifier set

FOR each transaction
    IF identifier already exists
        REPORT duplicate
    ELSE
        ADD identifier
    END IF

    IF amount <= 0
        REPORT invalid amount
    END IF
END FOR

CHECK transaction sequences
IF suspicious sequence found
    REPORT it
END IF
STOP
```

SOURCE CODE:
```python
transactions = [
    ("T101", 500, "DEPOSIT"),
    ("T102", 200, "WITHDRAW"),
    ("T102", 300, "DEPOSIT"),
    ("T103", -100, "WITHDRAW"),
    ("T104", 5000, "WITHDRAW"),
    ("T105", 600, "DEPOSIT")
]

ids = set()
duplicates = []
invalid_amounts = []

for transaction in transactions:
    tid, amount, ttype = transaction

    if tid in ids:
        duplicates.append(tid)
    else:
        ids.add(tid)

    if amount <= 0:
        invalid_amounts.append(transaction)

print("Duplicate IDs:", duplicates)
print("Invalid Amounts:", invalid_amounts)

print("\nSuspicious Sequences:")
for i in range(len(transactions) - 1):
    current = transactions[i]
    next_transaction = transactions[i + 1]

    if current[2] == "WITHDRAW" and next_transaction[2] == "WITHDRAW":
        print(current, "followed by", next_transaction)
