def hungarian_algorithm(cost_matrix):
    num_rows = len(cost_matrix)
    num_cols = len(cost_matrix[0])

    marked_rows = [False] * num_rows
    marked_cols = [False] * num_cols
    match = [-1] * num_cols

    for row in range(num_rows):
        min_cost = min(cost_matrix[row])
        for col in range(num_cols):
            cost_matrix[row][col] -= min_cost
            if cost_matrix[row][col] == 0 and match[col] == -1:
                marked_rows[row] = True
                marked_cols[col] = True
                match[col] = row
                break

    while True:
        col = marked_cols.index(False)

        while True:
            row = -1
            for r in range(num_rows):
                if not marked_rows[r] and cost_matrix[r][col] == 0:
                    row = r
                    break

            if row == -1:
                break

            marked_rows[row] = True
            marked_cols[col] = True

            if match[col] == -1:
                break

            marked_rows[match[col]] = True
            col = match[col]

        if row == -1:
            break

        min_unmarked_cost = float('inf')
        for r in range(num_rows):
            if not marked_rows[r]:
                for c in range(num_cols):
                    if not marked_cols[c] and cost_matrix[r][c] < min_unmarked_cost:
                        min_unmarked_cost = cost_matrix[r][c]

        for r in range(num_rows):
            if marked_rows[r]:
                for c in range(num_cols):
                    cost_matrix[r][c] += min_unmarked_cost
            else:
                for c in range(num_cols):
                    if not marked_cols[c]:
                        cost_matrix[r][c] -= min_unmarked_cost

        for c in range(num_cols):
            if not marked_cols[c]:
                for r in range(num_rows):
                    if not marked_rows[r] and cost_matrix[r][c] == 0:
                        match[c] = r
                        break

    return match


def visualize_matching(cost_matrix, match):
    num_rows = len(cost_matrix)
    num_cols = len(cost_matrix[0])

    for col in range(num_cols):
        row = match[col]
        if row != -1:
            print(f"Worker {col} is assigned to Task {row}.")

    unmatched_workers = [col for col in range(num_cols) if match[col] == -1]
    unmatched_tasks = [row for row in range(num_rows) if row not in match]

    if unmatched_workers:
        print("Unmatched workers:", unmatched_workers)
    if unmatched_tasks:
        print("Unmatched tasks:", unmatched_tasks)


# 示例使用
cost_matrix = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

print("成本矩阵:")
for row in cost_matrix:
    print(row)
print()

match = hungarian_algorithm(cost_matrix)

print("匹配结果:")
visualize_matching(cost_matrix, match)