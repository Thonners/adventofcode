"""
Test:
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

Prod
    [V] [G]             [H]        
[Z] [H] [Z]         [T] [S]        
[P] [D] [F]         [B] [V] [Q]    
[B] [M] [V] [N]     [F] [D] [N]    
[Q] [Q] [D] [F]     [Z] [Z] [P] [M]
[M] [Z] [R] [D] [Q] [V] [T] [F] [R]
[D] [L] [H] [G] [F] [Q] [M] [G] [W]
[N] [C] [Q] [H] [N] [D] [Q] [M] [B]
 1   2   3   4   5   6   7   8   9 
"""


STARTING_CRATES = {
    "prod": [
        "NDMQBPZ",
        "CLZQMDHV",
        "QHRDVFZG",
        "HGDFN",
        "NFQ",
        "DQVZFBT",
        "QMTZDVSH",
        "MGFPNQ",
        "BWRM",
    ],
    "test": ["ZN", "MCD", "p"],
}


def solve(lines: list[str], part: int = 1, test_type="test"):
    crates = STARTING_CRATES[test_type].copy()
    for line in lines:
        bits = line.split(" ")
        n_boxes = int(bits[1])
        # Subtract one as the piles are 1-indexed in the text examples
        i_from = int(bits[3]) - 1
        i_to = int(bits[5]) - 1
        # print(f"{n_boxes} From {i_from}, to {i_to}: {crates[i_from]} // {crates[i_to]}")
        if part == 1:
            for i in range(n_boxes):
                # Add the final letter (i.e. the top box) from the 'from' pile to the 'to' pile
                crates[i_to] += crates[i_from][-1]
                # Remove the final letter from the 'from' pile
                crates[i_from] = crates[i_from][:-1]
        else:
            # print(f"\t{crates[i_from][-n_boxes:]}")
            crates[i_to] += crates[i_from][-n_boxes:]
            crates[i_from] = crates[i_from][:-n_boxes]
    return "".join([pile[-1] for pile in crates])
