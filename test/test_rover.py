import unittest
from src.rover import Rover
from src.plateau import Plateau

class TestMarsRover(unittest.TestCase):
    def test_rover_basic_movements(self):
        plateau = Plateau(5, 5)
        rover = Rover(1, 2, 'N', plateau)
        commands = "LMLMLMLMM"
        rover.execute_commands(commands)
        self.assertEqual(rover.current_position(), "1 3 N")

    def test_rover_reaches_plateau_boundary(self):
        plateau = Plateau(5, 5)
        rover = Rover(1, 5, 'N', plateau)
        commands = "MMM"
        rover.execute_commands(commands)
        self.assertEqual(rover.current_position(), "1 5 N")  # Should not move beyond boundary

    def test_rover_no_commands(self):
        plateau = Plateau(5, 5)
        rover = Rover(2, 2, 'N', plateau)
        commands = ""
        rover.execute_commands(commands)
        self.assertEqual(rover.current_position(), "2 2 N")  # Should remain in the same place

    def test_rover_invalid_commands(self):
        plateau = Plateau(5, 5)
        rover = Rover(3, 3, 'E', plateau)
        commands = "MXRMM"
        with self.assertRaises(ValueError):
            rover.execute_commands(commands)  # Expecting a ValueError due to 'X'

    def test_multiple_rovers_sequentially(self):
        plateau = Plateau(5, 5)
        rover1 = Rover(1, 2, 'N', plateau)
        rover1_commands = "LMLMLMLMM"
        rover1.execute_commands(rover1_commands)
        self.assertEqual(rover1.current_position(), "1 3 N")

        rover2 = Rover(3, 3, 'E', plateau)
        rover2_commands = "MMRMMRMRRM"
        rover2.execute_commands(rover2_commands)
        self.assertEqual(rover2.current_position(), "5 1 E")

    def test_rover_edge_wrap(self):
        plateau = Plateau(5, 5)
        rover = Rover(0, 0, 'W', plateau)
        commands = "MMMMRMMMM"
        rover.execute_commands(commands)
        self.assertEqual(rover.current_position(), "0 4 N")  # Should not move off the plateau

    def test_rover_non_zero_start(self):
        plateau = Plateau(5, 5)
        rover = Rover(0, 0, 'S', plateau)
        commands = "MMM"
        rover.execute_commands(commands)
        self.assertEqual(rover.current_position(), "0 0 S")  # Should not move off the plateau

    def test_rovers_at_edges_with_movement_commands(self):
        plateau = Plateau(5, 5)
        edge_rovers = [
            (0, 5, 'W', "M"),
            (5, 0, 'E', "M"),
            (0, 0, 'S', "M"),
            (5, 5, 'N', "M")
        ]
        for x, y, heading, commands in edge_rovers:
            rover = Rover(x, y, heading, plateau)
            rover.execute_commands(commands)
            self.assertEqual(rover.current_position(), f"{x} {y} {heading}")  # Should not move off the plateau

if __name__ == '__main__':
    unittest.main()
