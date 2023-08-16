def navigate_spacecraft(initial_position, initial_direction, commands):
    x, y, z = initial_position
    directions = ['N', 'E', 'S', 'W', 'Up', 'Down']
    direction = initial_direction

    for cmd in commands:
        if cmd == 'f':
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1
            elif direction == 'Up':
                z += 1
            elif direction == 'Down':
                z -= 1
        elif cmd == 'b':
            if direction == 'N':
                y -= 1
            elif direction == 'S':
                y += 1
            elif direction == 'E':
                x -= 1
            elif direction == 'W':
                x += 1
            elif direction == 'Up':
                z -= 1
            elif direction == 'Down':
                z += 1
        elif cmd == 'r':
            direction = directions[(directions.index(direction)+1) % 4]
        elif cmd == 'l':
            direction = directions[(directions.index(direction)) % 4]
        elif cmd == 'u':
            if direction in ['N', 'S', 'E', 'W']:
                direction = 'Up'
            elif direction in ['Up', 'Down']:
                pass
        elif cmd == 'd':
            if direction in ['Up', 'Down']:
                direction = 'N'
            elif direction in ['N', 'S', 'E', 'W']:
                pass
    
    return (x, y, z), direction



