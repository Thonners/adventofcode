"""--- Day 3: Rucksack Reorganization ---
One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. 
A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
The fourth rucksack's compartments only share item type v.
The fifth rucksack's compartments only share item type t.
The sixth rucksack's compartments only share item type s.
To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
"""


lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()

filepath = "input.txt"
# filepath = "test.txt"


def main(part: int):
    totals = []
    with open(filepath, "r") as file:
        if part == 1:
            live_total = 0
            for line in file.readlines():
                midpoint = int(len(line.strip()) / 2)
                c_one = line.strip()[:midpoint]
                c_two = line.strip()[midpoint:]
                matched_letters = []
                for c in c_one:
                    if c in c_two and c not in matched_letters:
                        if c in lower:
                            score = lower.index(c) + 1
                        elif c in upper:
                            score = upper.index(c) + 27
                        print(f"Char: {c} matched. Score: {score}")
                        totals.append(score)
                        score = 0
                        matched_letters.append(c)
        else:
            lines = file.readlines()
            num_elves = int(len(lines) / 3)
            print(f"Num elves: {num_elves}")
            for i in range(num_elves):
                e1 = 3 * i
                e2 = e1 + 1
                e3 = e1 + 2
                matched_letters = []
                for c in lines[e1].strip():
                    if c in lines[e2] and c in lines[e3] and c not in matched_letters:
                        if c in lower:
                            score = lower.index(c) + 1
                        elif c in upper:
                            score = upper.index(c) + 27
                        print(f"Char: {c} matched. Score: {score}")
                        totals.append(score)
                        matched_letters.append(c)
                        score = 0

    print(f"Total score: {sum(totals)}")
    return sum(totals)


# Refactored to test the wrapper script
def solve(lines: list[str], part: int = 1):
    totals = []
    if part == 1:
        live_total = 0
        for line in lines:
            midpoint = int(len(line.strip()) / 2)
            c_one = line.strip()[:midpoint]
            c_two = line.strip()[midpoint:]
            matched_letters = []
            for c in c_one:
                if c in c_two and c not in matched_letters:
                    if c in lower:
                        score = lower.index(c) + 1
                    elif c in upper:
                        score = upper.index(c) + 27
                    print(f"Char: {c} matched. Score: {score}")
                    totals.append(score)
                    score = 0
                    matched_letters.append(c)
    else:
        num_elves = int(len(lines) / 3)
        print(f"Num elves: {num_elves}")
        for i in range(num_elves):
            e1 = 3 * i
            e2 = e1 + 1
            e3 = e1 + 2
            matched_letters = []
            for c in lines[e1].strip():
                if c in lines[e2] and c in lines[e3] and c not in matched_letters:
                    if c in lower:
                        score = lower.index(c) + 1
                    elif c in upper:
                        score = upper.index(c) + 27
                    print(f"Char: {c} matched. Score: {score}")
                    totals.append(score)
                    matched_letters.append(c)
                    score = 0
    return sum(totals)


if __name__ == "__main__":
    main(2)
