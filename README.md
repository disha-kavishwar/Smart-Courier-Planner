
# Smart Courier Planning System

## 1. Introduction
The Smart Courier Planning System is a Python-based application
that helps courier companies prioritize parcels, optimize package
selection and generate efficient delivery routes.

## 2. Objectives
- Prioritize parcels using Merge Sort.
- Optimize parcel selection using 0/1 Knapsack.
- Calculate shortest paths using Dijkstra's algorithm.
- Generate delivery routes using Nearest Neighbour approximation.
- Analyze algorithm execution time.

## 3. Technologies Used
- Python
- CSV
- Heap Queue
- Time module

## 4. Algorithms
1. Merge Sort - O(n log n)
2. 0/1 Knapsack - O(nW)
3. Dijkstra - O((V + E) log V) using a priority queue
4. Nearest Neighbour - O(V^2) for a general adjacency-list implementation

## 5. Project Files
- main.py
- sorting.py
- knapsack.py
- graph.py
- route_optimizer.py
- performance.py
- parcels.csv

## 6. How to Run
1. Install Python.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run: python main.py

## 7. Input Dataset
The parcels.csv file contains parcel ID, name, weight,
value and priority.

## 8. Output
The system displays:
- Sorted parcel priorities
- Selected parcels
- Total packing weight and value
- Shortest paths
- Delivery route
- Execution times

## 9. Conclusion
The project demonstrates how sorting, dynamic programming,
graph algorithms and approximation techniques can be combined
to simulate an intelligent courier planning system.
