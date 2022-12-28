def solve(lines: list[str], part: int = 1):
    count = 0
    if part == 1:
        for line in lines:
            e1, e2 = line.split(",")
            e1_start, e1_stop = e1.split("-")
            e2_start, e2_stop = e2.split("-")
            if (
                int(e1_start) <= int(e2_start)
                and int(e1_stop) >= int(e2_stop)
                or int(e2_start) <= int(e1_start)
                and int(e2_stop) >= int(e1_stop)
            ):
                print(f"Fully contained: {e1} / {e2}")
                count += 1
    else:
        for line in lines:
            e1, e2 = line.split(",")
            e1_start, e1_stop = e1.split("-")
            e2_start, e2_stop = e2.split("-")
            if (
                int(e1_start) <= int(e2_stop)
                and int(e1_stop) >= int(e2_start)
                or int(e2_start) <= int(e1_stop)
                and int(e2_stop) >= int(e1_start)
            ):
                print(f"Partial overlap: {e1} / {e2}")
                count += 1
    return count
