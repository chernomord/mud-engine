from door import Door

class Room(object):

    def __init__(self, description, name, doors=None):
        self.doors = {}
        self.name = name
        self.description = description
        if doors:
            for key, door in doors.items():
                self.doors[key] = Door(door)

    def read_room(self):
        return {
            'description': self.description,
            'doors': self.doors
        }
