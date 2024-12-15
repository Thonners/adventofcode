import shutil
from pathlib import Path
import sys
import importlib

filename = {"prod": "input.txt", "test": "test.txt"}

def get_input(day: int, year: int = 2024) -> None:
    url = f"https://adventofcode.com/{year}/day/{day}/input"


def solve(day: int, part: int):

    solution_file = Path(f"{day:02d}", "solution.py")
    if not solution_file.exists():
        template_file = "template.py"
        shutil.copy(template_file, solution_file)
        print(f"Created {solution_file.name} from the template")

    day_solver = importlib.import_module(f"{day:02d}.solution").solve

    for file_type in filename.keys():
        input_path = Path(f"{day:02d}", filename[file_type])
        if input_path.exists():
            with open(input_path, "r") as file:
                lines = [line.strip() for line in file.readlines()]
                result = day_solver(lines, part, file_type)
                print(f"Result for '{file_type}' part {part} = {result}")


if __name__ == "__main__":
    try:
        day = int(sys.argv[1])
        part = 1 if len(sys.argv) < 3 else int(sys.argv[2])
        solve(day, part)
    except KeyboardInterrupt as e:
        print("Keyboard interrupt received.")
