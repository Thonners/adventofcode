from pathlib import Path

total_space = 70000000
target = 30000000


def solve(lines: list[str], part: int = 1, test_type="test"):
    dirs = {"/": 0}
    active_dir = "/"
    path = Path("/")
    size = 0
    for i, line in enumerate(lines):
        segments = line.split(" ")
        if line.startswith("$ cd /"):
            pass
        elif line == "$ cd ..":
            dirs[str(path.parent.absolute())] += dirs[str(path.absolute())]
            path = path.parent
            size = 0
        elif line.startswith("$ cd"):
            path = Path(path, line.split(" ")[2])
            dirs[str(path.absolute())] = 0
        elif segments[0].isnumeric():
            dirs[str(path.absolute())] += int(segments[0])
    # The final dir never goes 'up', as we just finish the script, so add it now
    dirs[str(path.parent.absolute())] += dirs[str(path.absolute())]
    if part == 1:
        size = 0
        for key in dirs:
            if dirs[key] < 100000:
                size += dirs[key]
    else:
        size = total_space
        free_space = total_space - dirs["/"]
        required_to_clear = target - free_space
        for key in dirs:
            if dirs[key] > required_to_clear and dirs[key] < size:
                size = dirs[key]

    # print(f"{dirs}")
    return size
