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

    def read_current_room(self):
        return self.rooms[self.current_loc].read_room()

    def run(self):
        while self.current_loc != self.exit:
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
            if choice in current_room['doors']:
                self.current_loc = choice
            else:
                print('There is no such destination, ' + color.PURPLE + choice + color.END)
        print("\n" * 100)
        print(color.RED + color.BOLD + self.rooms[self.exit].read_room()['description'] + color.END)
