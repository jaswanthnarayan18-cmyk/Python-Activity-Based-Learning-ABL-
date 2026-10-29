

 58. Library Borrowing and Fine Reconciliation

AIM:
To analyse library borrowing records, calculate fines for delayed returns, identify overdue books, and reconcile book availability.

OBJECTIVES:
- Store book borrowing information using tuples.
- Identify overdue books.
- Calculate fines based on delay.
- Determine which books are available and unavailable.
- Generate a fine reconciliation report.

ALGORITHM:
1. Store book ID, borrowing period, and return delay.
2. Define the permitted borrowing period.
3. Calculate overdue days.
4. Calculate fine using the fine rate.
5. Mark books with delays as overdue.
6. Display total fines and book availability.

PSEUDO CODE:
```text
START
INPUT borrowing records
SET allowed period
SET fine per day

FOR each record
    IF borrowing period > allowed period
        overdue = borrowing period - allowed period
        fine = overdue * fine rate
        MARK overdue
    ELSE
        fine = 0
        MARK available/normal
    END IF
END FOR

DISPLAY overdue books
DISPLAY total fine
STOP
```

SOURCE CODE:
```python
records = [
    ("B101", 7, 0),
    ("B102", 10, 3),
    ("B103", 14, 7),
    ("B104", 5, 0),
    ("B105", 12, 5)
]

allowed_days = 7
fine_per_day = 5

total_fine = 0

print("Library Fine Report")

for book_id, borrowed_days, delay in records:
    overdue = max(0, borrowed_days - allowed_days)
    fine = overdue * fine_per_day
    total_fine += fine

    if overdue > 0:
        status = "OVERDUE"
    else:
        status = "ON TIME"

    print(book_id,
          "Overdue Days:", overdue,
          "Fine:", fine,
          "Status:", status)

print("\nTotal Fine:", total_fine)
