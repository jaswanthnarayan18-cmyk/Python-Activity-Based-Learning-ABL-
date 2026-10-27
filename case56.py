

# 56. Student Group Formation with Score Balancing

## Aim
To arrange students into groups of specified sizes while balancing their total scores and minimizing differences between group totals.

## Objectives
- Store student names and scores.
- Divide students into groups of a specified size.
- Balance scores between groups.
- Display group totals and score differences.

## Algorithm
1. Store students and their scores.
2. Sort students according to their scores.
3. Create empty groups.
4. Assign students to the group having the smallest current total.
5. Continue until all students are allocated.
6. Display group compositions and totals.

## Pseudocode
```text
START
INPUT students and scores
INPUT group size
SORT students by score descending
CREATE required number of groups

FOR each student
    FIND group with minimum total
    ADD student to that group
    UPDATE group total
END FOR

DISPLAY groups and totals
STOP
```

## Source Code
```python
students = [
    ("Asha", 90),
    ("Ravi", 85),
    ("Kiran", 80),
    ("Meena", 78),
    ("Arjun", 75),
    ("Priya", 72),
    ("Rahul", 70),
    ("Sneha", 68)
]

group_size = 2
number_of_groups = len(students) // group_size

students.sort(key=lambda x: x[1], reverse=True)

groups = [[] for _ in range(number_of_groups)]
totals = [0] * number_of_groups

for student in students:
    index = totals.index(min(totals))

    if len(groups[index]) < group_size:
        groups[index].append(student)
        totals[index] += student[1]

print("Student Groups")

for i, group in enumerate(groups, 1):
    print(f"\nGroup {i}:")
    for name, score in group:
        print(name, score)
    print("Total Score:", totals[i - 1])

print("\nScore Difference:",
      max(totals) - min(totals))
