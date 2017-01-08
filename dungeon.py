from textwrap import fill
from room import Room
from color import color


class Dungeon(object):

    def __init__(self, data):
        self.rooms = {}
        self.entry = data['entry']
        self.exit = data['exit']
        for room_key, room in data['rooms'].items():
            self.rooms[room_key] = Room(**room, name=room_key)
        self.current_loc = data['entry']

        self._game_over = False

    def read_current_room(self):
        return self.rooms[self.current_loc].read_room()

    def check_door(self, looking_for, doors):
        for room_key in doors.keys():
            if room_key.lower() == looking_for.lower():
                return room_key
        return False

    def execute_command(self, command):
        if self.check_door(command, self.read_current_room()['doors']):
            self.current_loc = self.check_door(command, self.read_current_room()['doors'])
        elif command == '$exit':
            self._game_over = True
        else:
            print('There is no such destination, ' + color.PURPLE + command + color.END)

    def is_game_over(self):
        return (self.current_loc == self.exit) or self._game_over

    def run(self):
        while not self.is_game_over():
            print("\n"*100)
            print('=========')
            current_room = self.read_current_room()
            print(fill(current_room['description'], 75))
            if 'doors' not in current_room:
                print('THE END')
                break

            print('You see the doors:')
            for key, door in current_room['doors'].items():
                target = door.read_door()['lead_to']
                descr = door.read_door()['description']
                item = '- ' + color.CYAN + target + color.END + ': ' + descr
                print(fill(item, 75))
            choice = input('Where to go? > ')
            # Проверяем есть ли дверь с введенным именем case insensitive
            self.execute_command(choice)

        print("\n" * 100)
        print(color.RED + color.BOLD + self.rooms[self.exit].read_room()['description'] + color.END)
