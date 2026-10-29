

 54. Multi-Branch Expense Matrix Analysis

AIM:
To analyse monthly expenses of multiple branches and categories using nested lists, calculate totals and averages, and identify the largest contributors.

OBJECTIVES:
- Store branch-wise and category-wise expenses.
- Calculate monthly and branch totals.
- Calculate average expenses.
- Identify the branch or category with the highest expenditure.

ALGORITHM:
1. Store expenses in a nested list.
2. Calculate the total expense of each branch.
3. Calculate the average expense.
4. Calculate category-wise totals.
5. Find the largest contributor.
6. Display the results.

PSEUDO CODE:
```text
START
INPUT expense matrix
FOR each branch
    CALCULATE branch total
    CALCULATE branch average
END FOR

FOR each category
    CALCULATE category total
END FOR

FIND maximum branch and category
DISPLAY results
STOP
``
 
flowchart TD:(mermaid)
    A([Start]) --> B[/Input expense matrix/]
    B --> C[Calculate each branch total and average]
    C --> D[Calculate category-wise totals]
    D --> E[Find maximum branch expense]
    E --> F[Find maximum category expense]
    F --> G[/Display totals, averages and largest contributors/]
    G --> H([Stop])


SOURCE CODE:
```python
expenses = [
    [12000, 15000, 10000, 8000],
    [14000, 13000, 11000, 9000],
    [10000, 16000, 12000, 7000]
]

branches = ["Branch A", "Branch B", "Branch C"]
categories = ["Rent", "Salaries", "Utilities", "Maintenance"]

branch_totals = []

for i in range(len(expenses)):
    total = sum(expenses[i])
    average = total / len(expenses[i])
    branch_totals.append(total)

    print(branches[i],
          "Total =", total,
          "Average =", round(average, 2))

category_totals = []

for j in range(len(categories)):
    total = sum(expenses[i][j] for i in range(len(expenses)))
    category_totals.append(total)

print("\nCategory Totals:")
for category, total in zip(categories, category_totals):
    print(category, "=", total)

max_branch = branches[branch_totals.index(max(branch_totals))]
max_category = categories[category_totals.index(max(category_totals))]

print("\nLargest Branch Contributor:", max_branch)
print("Largest Category Contributor:", max_category)
