from nose.tools import *
from door import Door

def test_door():
    door_data = {
        'lead_to': 'Hall',
        'description': 'Stairs up to the Hall'
    }
    door = Door(door_data)
    assert_equal(door.data, door_data)
    assert_equal(door.read_door()['lead_to'], 'Hall')

