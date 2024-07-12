from .rover import Rover, Plateau


def process_input(input_data):
    lines = input_data.strip().split('\n')
    plateau_dimensions = lines[0].split()
    plateau = Plateau(int(plateau_dimensions[0]), int(plateau_dimensions[1]))
    results = []

    i = 1
    while i < len(lines):
        position = lines[i].split()
        commands = lines[i + 1]
        rover = Rover(int(position[0]), int(position[1]), position[2], plateau)
        rover.execute_commands(commands)
        results.append(rover.current_position())
        i += 2

    return results


def main():
    import sys
    input_data = sys.stdin.read()
    output = process_input(input_data)
    print("Output:")
    for line in output:
        print(line)


if __name__ == "__main__":
    main()
