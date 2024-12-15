def solve(lines: list[str], part: int = 1, test_type="test"):
    pOne = []
    pTwo = []
    for line in lines:
        print(line)
        a, b = line.split()
        pOne.append(a)
        pTwo.append(b)
    if part == 1:
        sortedOne = sorted(pOne)
        sortedTwo = sorted(pTwo)
        tot = 0
        for i in range(len(sortedOne)):
            tot += abs(int(sortedOne[i]) - int(sortedTwo[i]))
        return tot
    else:
        tot = 0
        for a in pOne:
            aint = int(a)
            count = 0
            for b in pTwo:
                bint = int(b)
                count += aint == bint
            tot += aint*count
        return tot
