
from collections import deque
from copy import deepcopy


def count_islands_dfs(grid, show_trace=False):
    """Count islands using Depth-First Search."""
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    def dfs(r, c):
        # Stop if outside the grid or not land.
        if (
            r < 0 or r >= rows
            or c < 0 or c >= cols
            or grid[r][c] != "1"
        ):
            return

        # Mark this land cell as visited.
        grid[r][c] = "0"

        if show_trace:
            print(f"  Visit land at row {r}, column {c}")

        # Explore up, down, left, and right.
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1

                if show_trace:
                    print(f"\nDiscover island #{islands} at ({r}, {c})")

                dfs(r, c)

    return islands


def count_islands_bfs(grid):
    """Count islands using Breadth-First Search."""
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1":
                continue

            islands += 1
            grid[r][c] = "0"
            queue = deque([(r, c)])

            while queue:
                current_r, current_c = queue.popleft()

                for dr, dc in [
                    (-1, 0),  # Up
                    (1, 0),   # Down
                    (0, -1),  # Left
                    (0, 1),   # Right
                ]:
                    nr = current_r + dr
                    nc = current_c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == "1"
                    ):
                        # Mark when enqueuing to avoid duplicates.
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))

    return islands


def print_grid(grid):
    """Display the grid."""
    for row in grid:
        print(" ".join(row))


def run_tests():
    """Check normal cases and edge cases."""
    tests = [
        (
            "Three separate islands",
            [
                list("11000"),
                list("11000"),
                list("00100"),
                list("00011"),
            ],
            3,
        ),
        (
            "All land connected",
            [
                list("111"),
                list("111"),
                list("111"),
            ],
            1,
        ),
        (
            "All water",
            [
                list("000"),
                list("000"),
            ],
            0,
        ),
        (
            "Diagonal cells are separate",
            [
                list("10"),
                list("01"),
            ],
            2,
        ),
        ("Empty grid", [], 0),
        ("Single land cell", [list("1")], 1),
    ]

    print("\n=== TEST RESULTS ===")
    all_passed = True

    for name, original_grid, expected in tests:
        dfs_result = count_islands_dfs(deepcopy(original_grid))
        bfs_result = count_islands_bfs(deepcopy(original_grid))

        passed = dfs_result == expected and bfs_result == expected
        all_passed = all_passed and passed

        print(
            f"{name}: DFS={dfs_result}, BFS={bfs_result}, "
            f"Expected={expected} -> {'PASS' if passed else 'FAIL'}"
        )

    print(
        "\nOverall:",
        "ALL TESTS PASSED" if all_passed else "SOME TESTS FAILED",
    )


def main():
    grid = [
        list("11000"),
        list("11000"),
        list("00100"),
        list("00011"),
    ]

    print("=" * 45)
    print("       SATELLITE ISLAND COUNTER")
    print("=" * 45)

    print("\n=== ORIGINAL GRID ===")
    print_grid(grid)

    print("\n=== DFS TRAVERSAL ===")
    dfs_result = count_islands_dfs(deepcopy(grid), show_trace=True)
    print("\nTotal islands using DFS:", dfs_result)

    bfs_result = count_islands_bfs(deepcopy(grid))
    print("Total islands using BFS:", bfs_result)

    print("\n=== COMPLEXITY ===")
    print("Time: O(rows * columns) for both methods")
    print("Space: O(rows * columns) worst case")

    run_tests()


if __name__ == "__main__":
    main()
