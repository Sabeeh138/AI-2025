class FirefightingRobot:
    def __init__(self):
        self.grid = {
            'a': 'safe', 'b': 'safe', 'c': 'fire',
            'd': 'safe', 'e': 'fire', 'f': 'safe',
            'g': 'safe', 'h': 'safe', 'j': 'fire'
        }
        self.path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
        self.position = 'a'

    def display_environment(self):
        grid_display = ''
        rooms = list(self.grid.keys())
        for i in range(0, 9, 3):
            for j in range(3):
                room = rooms[i + j]
                status = '🔥' if self.grid[room] == 'fire' else ' '
                grid_display += f'[{status}]'
            grid_display += '\n'
        print(grid_display)

    def move_and_extinguish(self):
        for room in self.path:
            self.position = room
            print(f'Moving to room {room.upper()}')
            if self.grid[room] == 'fire':
                print(f'Fire detected in room {room.upper()}! Extinguishing fire...')
                self.grid[room] = 'safe'
            else:
                print(f'Room {room.upper()} is safe.')
            self.display_environment()

    def final_status(self):
        print('Final status of all rooms:')
        self.display_environment()

robot = FirefightingRobot()
robot.move_and_extinguish()
robot.final_status()
