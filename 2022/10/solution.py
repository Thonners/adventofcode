"""
noop            1
addx 3          1 1 4
addx -5         1 1 4 4 -1 


vs = [1]
lines = [
    "noop","addx 3","addx -5"
]

"""


def solve(lines: list[str], part: int = 1, test_type="test"):
    vs = [1]
    for line in lines:
        # print(f"Evaluating '{line}'")
        split_str = line.split(" ")
        if split_str[0] == "noop":
            vs += noop(vs[-1])
        elif split_str[0] == "addx":
            vs += addx(vs[-1], int(split_str[1]))
    if part == 1:
        total = 0
        print(vs[:39])
        for i in range(len(vs)):
            if i in [20, 60, 100, 140, 180, 220]:
                v = vs[i - 1]
                strength = v * i
                total += strength
                # print(f"{i-1:03d}: {vs[i-1]}")
                print(f"{i:03d}: {v} | {strength}")
        return total
    else:
        for i in range(len(vs)):
            col = i % 40
            if vs[i] - 1 == col or vs[i] == col or vs[i] + 1 == col:
                print("#", end="")
            else:
                print(" ", end="")
            if col == 39:
                print("")


def noop(v):
    # print("\tnoop")
    return [v]


def addx(v, x):
    # print(f"\taddx: {x}")
    return [v, v + x]
