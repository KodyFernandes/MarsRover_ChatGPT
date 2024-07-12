from .plateau import Plateau


class Rover:
    def __init__(self, x, y, heading, plateau):
        self.x = x
        self.y = y
        self.heading = heading
        self.plateau = plateau

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
        if self.heading == 'N' and self.y < self.plateau.height:
            self.y += 1
        elif self.heading == 'E' and self.x < self.plateau.width:
            self.x += 1
        elif self.heading == 'S' and self.y > 0:
            self.y -= 1
        elif self.heading == 'W' and self.x > 0:
            self.x -= 1

    def current_position(self):
        return f"{self.x} {self.y} {self.heading}"
