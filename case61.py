
# 61. Nested List Examination Seating Validation
## Aim
To validate a complete examination seating matrix by detecting duplicate roll numbers, reserved positions, empty seats, and invalid student allocations.

## Objectives
- Validate the examination seating matrix.
- Detect duplicate roll numbers.
- Identify reserved seats that are incorrectly occupied.
- Detect empty seats.
- Detect invalid student roll numbers.
- Generate a complete seating validation report.

## Algorithm
1. Create the examination seating matrix.
2. Define the valid roll-number range.
3. Define reserved seat positions.
4. Traverse every position in the matrix.
5. Check whether the seat is empty.
6. Check whether the seat is reserved.
7. Check whether the roll number is within the valid range.
8. Maintain a set of encountered roll numbers.
9. Report duplicate roll numbers.
10. Display the validation results.

## Pseudocode
START
INPUT seating matrix
INPUT valid roll number range
INPUT reserved positions

CREATE empty set for roll numbers
CREATE empty lists for errors

FOR each row
    FOR each seat
        IF seat is empty
            ADD seat to empty seat list

        ELSE IF position is reserved
            ADD position to reserved violation list

        ELSE IF roll number is outside valid range
            ADD roll number to invalid allocation list

        ELSE IF roll number already exists
            ADD roll number to duplicate list

        ELSE
            ADD roll number to set
        END IF
    END FOR
END FOR

DISPLAY duplicate roll numbers
DISPLAY reserved seat violations
DISPLAY empty seats
DISPLAY invalid allocations

IF no errors exist
    DISPLAY "Seating arrangement is valid"
ELSE
    DISPLAY "Seating arrangement contains errors"

## Source Code
```python
seating = [
    [101, 102, 103, 104],
    [105, None, 107, 108],
    [109, 110, 102, 112],
    [113, 114, 999, 116]
]

valid_roll_numbers = set(range(101, 117))

# Reserved seat positions: (row, column)
reserved_positions = {(1, 1)}

duplicates = []
reserved_violations = []
empty_seats = []
invalid_allocations = []

seen = set()

for i in range(len(seating)):
    for j in range(len(seating[i])):
        roll = seating[i][j]
        position = (i, j)

        # Check empty seats
        if roll is None:
            empty_seats.append(position)
            continue

        # Check reserved positions
        if position in reserved_positions:
            reserved_violations.append((position, roll))
            continue

        # Check invalid roll numbers
        if roll not in valid_roll_numbers:
            invalid_allocations.append((position, roll))
            continue

        # Check duplicates
        if roll in seen:
            duplicates.append(roll)
        else:
            seen.add(roll)

print("Examination Seating Validation")

print("\nDuplicate Roll Numbers:")
if duplicates:
    print(duplicates)
else:
    print("None")

print("\nReserved Seat Violations:")
if reserved_violations:
    for position, roll in reserved_violations:
        print("Position:", position, "Roll Number:", roll)
else:
    print("None")

print("\nEmpty Seats:")
if empty_seats:
    for position in empty_seats:
        print("Position:", position)
else:
    print("None")

print("\nInvalid Student Allocations:")
if invalid_allocations:
    for position, roll in invalid_allocations:
        print("Position:", position, "Roll Number:", roll)
else:
    print("None")

total_errors = (
    len(duplicates)
    + len(reserved_violations)
    + len(empty_seats)
    + len(invalid_allocations)
)

print("\nTotal Validation Errors:", total_errors)

if total_errors == 0:
    print("Seating arrangement is VALID")
else:
    print("Seating arrangement contains ERRORS")
