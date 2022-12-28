class Monkey:
    def __init__(self, lines) -> None:
        self.i_monkey = int(lines[0].replace(":", "").split(" ")[1])
        self.items = [
            int(item) for item in lines[1].strip().replace(",", "").split(" ")[2:]
        ]
        self.operation = self._get_op_from_string(lines[2])
        self.test_denominator = int(lines[3].replace(":", "").split(" ")[-1])
        self.target_if_true = int(lines[4].replace(":", "").split(" ")[-1])
        self.target_if_false = int(lines[5].replace(":", "").split(" ")[-1])
        self.inspection_count = 0

    def take_turn(self):
        for item in self.items:
            self.inspection_count += 1
            item = self.operation(item)
            item = int(item / 3)
            if item % self.test_denominator == 0:
                self.monkeys[self.target_if_true].items.append(item)
            else:
                self.monkeys[self.target_if_false].items.append(item)
        self.items = []

    def _get_op_from_string(self, string):
        op_full = string.split("=")
        var_1, operator_string, var_2 = op_full[1].strip().split(" ")

        if operator_string == "+":
            return self._add(var_2)
        elif operator_string == "*":
            if var_2 == "old":
                return self._square()
            return self._multiply(var_2)

    def _add(self, to_be_added):
        return lambda x: x + int(to_be_added)

    def _multiply(self, multiplicand):
        return lambda x: x * int(multiplicand)

    def _square(self):
        return lambda x: x**2

    def __repr__(self):
        return f"Monkey(i={self.i_monkey}, inspected: {self.inspection_count}, items: {self.items})"


def solve(lines: list[str], part: int = 1, test_type="test"):
    monkey_count = int((len(lines) + 1) / 7)
    monkeys = []
    print(f"n Monkeys: {monkey_count}")
    if part == 1:
        num_rounds = 20
        for i in range(monkey_count):
            monkeys.append(Monkey(lines[i * 7 : i * 7 + 6]))
        for i in range(monkey_count):
            monkeys[i].monkeys = monkeys
            print(f"Starting Monkeys: {monkeys[i]}")
        for round in range(num_rounds):
            print(f"Round: {round +1}")
            for i in range(monkey_count):
                monkeys[i].take_turn()

    else:
        for line in lines:
            pass

    for m in monkeys:
        print(m)
    inspections = [m.inspection_count for m in monkeys]
    inspections = sorted(inspections)
    print(
        f"Top two: {inspections[-2:]}, monkey business: {inspections[-2] * inspections[-1]}"
    )
