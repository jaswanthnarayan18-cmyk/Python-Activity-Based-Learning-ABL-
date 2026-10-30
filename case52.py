52. Hackathon Team Formation and Ranking

 Aim
To analyse student scores and team compositions, validate team sizes, calculate aggregate round-wise scores, and resolve tied rankings using predefined rules.

 OBJECTIVES:
- Validate whether teams contain the required number of members.
- Calculate total scores of teams across multiple rounds.
- Rank teams according to their total scores.
- Resolve ties using the highest individual score as a secondary criterion.

ALGORITHM:
1. Store team names, members, and round-wise scores.
2. Validate the size of every team.
3. Calculate the total score of each team.
4. Find the highest individual score in each team.
5. Sort teams by total score in descending order.
6. If totals are equal, use the highest individual score as the tie-breaker.
7. Display the final ranking.

PSEUDO CODE:
```text
START
INPUT teams
FOR each team
    CHECK team size
    CALCULATE total round scores
    FIND highest individual score
END FOR
SORT teams by total score descending
IF scores are equal
    SORT by highest individual score descending
END IF
DISPLAY ranking
STOP
```
 
flowchart TD
    A([START]) --> B[/Input team names, members and round-wise scores/]
    B --> C[Set required team size]
    C --> D{Is team size valid?}
    D -- No --> E[Display invalid team size]
    D -- Yes --> F[Calculate total round-wise score]
    F --> G[Find highest individual score]
    G --> H[Store valid team details]
    E --> I{Are more teams available?}
    H --> I
    I -- Yes --> B
    I -- No --> J[Sort teams by total score in descending order]
    J --> K{Are total scores tied?}
    K -- Yes --> L[Compare highest individual scores]
    K -- No --> M[Assign team rankings]
    L --> M
    M --> N[/Display final team ranking and scores/]
    N --> O([STOP])



SOURCE CODE:
```python
teams = [
    {"name": "Team Alpha", "members": 3, "rounds": [85, 90, 88],
     "individual": [90, 85, 88]},
    {"name": "Team Beta", "members": 2, "rounds": [90, 90, 85],
     "individual": [92, 85]},
    {"name": "Team Gamma", "members": 3, "rounds": [85, 90, 88],
     "individual": [89, 88, 86]}
]

required_size = 3
valid_teams = []

for team in teams:
    if team["members"] == required_size:
        total = sum(team["rounds"])
        highest = max(team["individual"])

        team["total"] = total
        team["highest"] = highest
        valid_teams.append(team)
    else:
        print(team["name"], "has an invalid team size")

valid_teams.sort(
    key=lambda x: (x["total"], x["highest"]),
    reverse=True
)

print("\nHackathon Ranking")
for rank, team in enumerate(valid_teams, 1):
    print(rank, team["name"], "Total:", team["total"],
          "Highest Individual:", team["highest"])
