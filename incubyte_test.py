import unittest
from incubyte import navigate_spacecraft

class SpacecraftTestCase(unittest.TestCase):

    def test_spacecraft_navigation(self):
        # Test case 1
        initial_position_1 = (0, 0, 0)
        initial_direction_1 = 'N'
        commands_1 = ['f', 'r', 'u', 'b', 'l']
        result = navigate_spacecraft(initial_position_1, initial_direction_1, commands_1)
        self.assertEqual(result, ((0, 1, -1), 'N'))
    
    def test_spacecraft_navigation1(self):
        # Test case 2
        initial_position_2 = (1, -1, 2)
        initial_direction_2 = 'Up'
        commands_2 = ['f', 'r', 'u', 'b', 'l', 'd', 'l']
        result1 = navigate_spacecraft(initial_position_2, initial_direction_2, commands_2)
        self.assertEqual(result1, ((1, -1, 2), 'N'))
    
    def test_spacecraft_navigation2(self):
        # Test case 3
        initial_position_3 = (10, 5, -3)
        initial_direction_3 = 'E'
        commands_3 = ['f', 'b', 'r', 'l', 'u', 'd']
        result2 = navigate_spacecraft(initial_position_3, initial_direction_3, commands_3)
        self.assertEqual(result2, ((10, 5, -3), 'N'))

    def test_spacecraft_navigation3(self):
        # Test case 4
        initial_position_4 = (2, 4, 9)
        initial_direction_4 = 'Down'
        commands_4 = ['f', 'r', 'l', 'u', 'b', 'f','d','b','f']
        result3 = navigate_spacecraft(initial_position_4, initial_direction_4, commands_4)
        self.assertEqual(result3, ((2, 4, 8), 'N'))

if __name__ == '__main__':
    unittest.main()
