import numpy as np


def solve(lines: list[str], part: int = 1, test_type="test"):
    size = len(lines)
    arr = np.zeros((size, size))
    visible = np.ones((size, size))
    scores = np.ones((size, size))
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            arr[i, j] = int(c)
    if part == 1:
        for row in range(1, size - 1):
            for col in range(1, size - 1):
                value = arr[row, col]
                visible[row, col] = any(
                    [
                        get_is_visible(arr[row, :col], value),
                        get_is_visible(arr[row, col + 1 :], value),
                        get_is_visible(arr[:row, col], value),
                        get_is_visible(arr[row + 1 :, col], value),
                    ]
                )
        print(
            f"Shape:{(len(lines), len(lines[0]))}:  \n{arr}\n{visible}\nTotal visible: {visible.sum()}"
        )
        return int(visible.sum())
    else:
        for row in range(1, size - 1):
            for col in range(1, size - 1):
                value = arr[row, col]
                left = get_visible_trees(arr[row, :col], value, False)
                right = get_visible_trees(arr[row, col + 1 :], value, True)
                top = get_visible_trees(arr[:row, col], value, False)
                bottom = get_visible_trees(arr[row + 1 :, col], value, True)
                scores[row, col] = left * right * top * bottom
        print(f"{scores}")
        return scores.max()


def get_is_visible(other_trees: list, height: int) -> bool:
    return max(other_trees) < height


def get_visible_trees(
    other_trees: list, height: int, looking_front_to_back: bool
) -> int:
    other_trees = list(other_trees)
    if not looking_front_to_back:
        other_trees.reverse()
    counter = 0
    for tree in other_trees:
        counter += 1
        if tree >= height:
            return counter
    return counter
