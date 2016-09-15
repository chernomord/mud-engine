from nose.tools import *
from dungeon import dungeon


def test_door():
    door_data = {
        'lead_to': 'Hall',
        'description': 'Stairs up to the Hall'
    }
    door = dungeon.Door(door_data)
    assert_equal(door.data, door_data)
    assert_equal(door.read_door()['lead_to'], 'Hall')
