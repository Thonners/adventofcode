import numpy as np
from math import copysign


class Rope:
    def __init__(self, num_knots=1, array_size=(6, 5)):
        self.knots = [Knot(i + 1) for i in range(num_knots)]
        self.output_array_size = array_size
        # print(f"Created knots: {self.knots}")

    def move(self, direction):
        self.knots[0].move(direction)
        # print(f"Moving: {direction}")
        for i in range(1, len(self.knots)):
            self.knots[i].head_position = self.knots[i - 1].tail_position
            self.knots[i].move_tail()

    def get_tail_positions_count(self) -> int:
        return self.knots[-1].get_tail_positions_count()

    def get_extremities(self):
        x_coords = [
            coord[0] for knot in self.knots for coord in knot.tail_positions
        ] + [self.knots[0].head_position[0]]
        y_coords = [
            coord[1] for knot in self.knots for coord in knot.tail_positions
        ] + [self.knots[0].head_position[1]]
        return [(min(x_coords), min(y_coords)), (max(x_coords), max(y_coords))]

    def get_position_array(self):
        extremities = self.get_extremities()
        width = (max(extremities[1][0] - extremities[0][0], 1),)
        height = (max(extremities[1][1] - extremities[0][1], 1),)
        x_offset = -extremities[0][0]
        y_offset = -extremities[0][1]
        print(f"Extremities: {extremities}")
        print(f"width: {width}")
        print(f"height: {height}")
        print(f"x_offset: {x_offset}")
        print(f"y_offset: {y_offset}")
        array = np.zeros((width, height))
        # Mark the starting point (can't mix text/ints so just use -1)
        array[x_offset, height - y_offset] = -1
        # Mark the head with 99
        array[
            self.knots[0].head_position[0] + x_offset,
            height - self.knots[0].head_position[1] + y_offset,
        ] = 99
        print(f"Knots: {self.knots}")
        for knot in self.knots[::-1]:
            array[
                knot.tail_position[0], height - knot.tail_position[1]
            ] = knot.knot_count
        return array

    def __repr__(self) -> str:
        # extremities = self.get_extremities()
        # x_offset = -extremities[0][0]
        # y_offset = -extremities[0][1]
        # for row in range(extremities[0][1] - extremities[0][0]):
        #     for col in range(extremities[1][1] - extremities[1][0]):
        #         tail_been_there = False
        return f"Knot(\n{self.get_position_array()}\n)"


class Knot:
    def __init__(self, knot_count: int) -> None:
        self.knot_count = knot_count
        self.head_position = (0, 0)
        self.tail_position = (0, 0)
        self.tail_positions = [(0, 0)]

    def __repr__(self):
        return f"Knot(head={self.head_position},tail={self.tail_position})"

    def move(self, direction: str):
        self.move_head(direction)
        self.move_tail()

    def move_head(self, direction):
        if direction == "U":
            self.head_position = (self.head_position[0], self.head_position[1] + 1)
        elif direction == "D":
            self.head_position = (self.head_position[0], self.head_position[1] - 1)
        if direction == "R":
            self.head_position = (self.head_position[0] + 1, self.head_position[1])
        if direction == "L":
            self.head_position = (self.head_position[0] - 1, self.head_position[1])

    def move_tail(self):
        x_delta = self.head_position[0] - self.tail_position[0]
        y_delta = self.head_position[1] - self.tail_position[1]
        if abs(x_delta) > 1:
            self.tail_position = (
                int(self.head_position[0] - copysign(1, x_delta)),
                int(self.head_position[1]),
            )
        if abs(y_delta) > 1:
            self.tail_position = (
                int(self.head_position[0]),
                int(self.head_position[1] - copysign(1, y_delta)),
            )
        self.tail_positions.append(self.tail_position)

    def get_tail_positions_count(self) -> int:
        return len(set(self.tail_positions))

    def get_extremities(self):
        x_coords = [coord[0] for coord in self.tail_positions] + [self.head_position[0]]
        y_coords = [coord[1] for coord in self.tail_positions] + [self.head_position[1]]
        return [(min(x_coords), min(y_coords)), (max(x_coords), max(y_coords))]


def solve(lines: list[str], part: int = 1, test_type="test"):
    if part == 1:
        r = Rope()
    else:
        r = Rope(10)
    for line in lines:
        direction, count = line.split(" ")
        count = int(count)
        for i in range(count):
            r.move(direction)
        if test_type == "test":
            print(r)

    print(r.get_extremities())
    return r.get_tail_positions_count()
