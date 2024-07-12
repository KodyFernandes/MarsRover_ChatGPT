from .plateau import Plateau


class Rover:
    def __init__(self, x, y, heading, plateau):
        self.x = x
        self.y = y
        self.heading = heading
        self.plateau = plateau
        self.plateau.add_rover(self.x, self.y)

    def execute_commands(self, commands):
        for command in commands:
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            elif command == 'M':
                self.move()
            else:
                raise ValueError("Invalid command")

    def turn_left(self):
        directions = 'NESW'
        self.heading = directions[(directions.index(self.heading) - 1) % 4]

    def turn_right(self):
        directions = 'NESW'
        self.heading = directions[(directions.index(self.heading) + 1) % 4]

    def move(self):
        new_x, new_y = self.x, self.y
        if self.heading == 'N':
            new_y += 1
        elif self.heading == 'E':
            new_x += 1
        elif self.heading == 'S':
            new_y -= 1
        elif self.heading == 'W':
            new_x -= 1

        if 0 <= new_x <= self.plateau.width and 0 <= new_y <= self.plateau.height and not self.plateau.is_position_occupied(
                new_x, new_y):
            self.plateau.update_position(self.x, self.y, new_x, new_y)
            self.x, self.y = new_x, new_y

    def current_position(self):
        return f"{self.x} {self.y} {self.heading}"
