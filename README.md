# goit-algo-hw-06

# Task 2: DFS vs BFS Pathfinding in a Real-World Graph (Hadley Transport Network)

## Task Description

We were asked to:

1. Implement **DFS (Depth-First Search)** and **BFS (Breadth-First Search)** algorithms.
2. Use them to find paths in a real-world graph built in Task 1 (Hadley-centered transport network).
3. Compare the paths and explain the difference in results.

---

## Implementation Summary

- The graph models 10 key locations in and around **Hadley, Telford**.
- Connections represent bus or train links with weights (travel time in minutes).
- Both **DFS** and **BFS** were implemented to find a path from one node to another.

---

## Test Case 1: `start = "Hadley"`, `goal = "Priorslee"`

### DFS Result:

```
Hadley → Donnington → Priorslee
```

### BFS Result:

```
Hadley → Donnington → Priorslee
```

### Why the same?

In this case, both DFS and BFS return the **same path** because:

- There is a **direct short path** from Hadley to Priorslee.
- DFS explores one branch and quickly finds the goal.
- BFS also finds the shortest path first (as expected).

---

## Test Case 2: `start = "Hadley"`, `goal = "Telford Central"`

### DFS Result:

```
Hadley → Ketley → Wellington → Telford Central
```

### BFS Result:

```
Hadley → Telford Central
```

### Why different?

- **BFS** guarantees the shortest path by steps, so it uses the **direct Hadley → Telford Central** edge.
- **DFS** explores depth-first. It first picks another branch (Hadley → Ketley → Wellington) and reaches the goal via a **longer path**.

---

## Conclusion:

- **DFS** goes deep first. It may find **any valid path**, not necessarily the shortest.
- **BFS** explores all neighbors first and **finds the shortest path** (by number of steps).
- In small graphs with few branches, both may return the same result.
- In more complex graphs, their behavior differs significantly.

---

## Висновок:

- **DFS (Пошук у глибину)** спочатку йде в глиб гілки. Він знаходить **будь-який шлях**, не обов’язково найкоротший.
- **BFS (Пошук у ширину)** спочатку досліджує всіх сусідів і **знаходить найкоротший шлях** (за кількістю кроків).
- У невеликих графах обидва алгоритми можуть дати однаковий результат.
- У складніших мережах вони показують різну поведінку.

---

## Files

- `task_1.py` — builds the transport graph for Hadley and surroundings.
- `task_2.py` — implements DFS and BFS pathfinding and prints results.
- `task_3.py` — Implements Dijkstra's algorithm to find the shortest path in the developed graph:
