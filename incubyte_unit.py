import unittest
from incubyte import navigate_spacecraft

x = int(input("Enter initial x-coordinate: "))
y = int(input("Enter initial y-coordinate: "))
z = int(input("Enter initial z-coordinate: "))
initial_direction = input("Enter initial direction (N, S, E, W, Up, Down): ")

# Take user input for commands (e.g., "f r u b l")
commands = input("Enter commands: ").split()

# Calculate the final position and direction
final_position, final_direction = navigate_spacecraft((x, y, z), initial_direction, commands)

# Print the final position and direction
print(f"Final Position: {final_position}")
print(f"Final Direction: {final_direction}")


