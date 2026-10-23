
# Day 42 - Number of Islands

## Problem Statement
Given a 2D grid of land ("1") and water ("0"),
count the number of separate islands.

Land cells are connected only horizontally and vertically.
Diagonal connections do not count.

## Approach
### Depth-First Search (DFS)
1. Scan every cell.
2. When unvisited land is found, increase the island count.
3. Explore all connected land using DFS.
4. Mark visited cells as water.
5. Continue until every cell is checked.

### Breadth-First Search (BFS)
1. Find an unvisited land cell.
2. Increase the island count and add the cell to a queue.
3. Explore its four neighboring cells.
4. Mark land as visited when adding it to the queue.
5. Continue until the queue is empty.

## Example
Input:
11000
11000
00100
00011

Output: 3

## Test Cases
- Multiple separate islands
- One connected island
- All water
- Diagonal land cells
- Empty grid
- Single land cell

## Complexity
Time: O(R * C)
Space: O(R * C) worst case

R = number of rows
C = number of columns

## Real-World Applications
- Geographic mapping
- Flood and disaster analysis
- Connected component detection
- Image segmentation
- Network connectivity analysis

## Run
python day42_number_of_islands.py
