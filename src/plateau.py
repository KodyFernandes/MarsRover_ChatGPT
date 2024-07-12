class Plateau:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.occupied_positions = {}

    def is_position_occupied(self, x, y):
        return (x, y) in self.occupied_positions

    def update_position(self, old_x, old_y, new_x, new_y):
        if (old_x, old_y) in self.occupied_positions:
            del self.occupied_positions[(old_x, old_y)]
        self.occupied_positions[(new_x, new_y)] = True

    def add_rover(self, x, y):
        self.occupied_positions[(x, y)] = True

    def remove_rover(self, x, y):
        if (x, y) in self.occupied_positions:
            del self.occupied_positions[(x, y)]