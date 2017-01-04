from dungeon import Dungeon

dungeon_data = {
    'entry': 'Hall',
    'exit': 'END',
    'rooms': {
        'Hall': {
            'description': 'You enter the hall',
            'doors': {
                'Cellar': {
                    'lead_to': 'Cellar',
                    'description': 'Trapdoor to some kind of castle basement'
                },
                'Passage': {
                    'lead_to': 'Passage',
                    'description': 'Dark and gloomy pass into the Corridor'
                }
            }
        },
        'Cellar': {
            'description': 'You walk down the stairs and the trapdoor shuts above your head. It is so dark here that you can\'t see anything.',
            'doors': {
                'Hall': {
                    'lead_to': 'Hall',
                    'description': 'Stairs up to the Hall'
                }
            }
        },
        'Passage': {
            'description': 'You enter dark and narrow passage leading somewhere deeper into the Castle. There\'are boockshelf alonside the door and the armor stand in the corner',
            'doors': {
                'Hall': {
                    'lead_to': 'Hall',
                    'description': 'Doorway to the Hall'
                },
                'Inner garden': {
                    'lead_to': 'Inner garden',
                    'description': 'Dark doorway. Wind silently blows from it\' direction and you can hear some strange eery sounds going from that direction...'
                }
            }
        },
        'Inner garden': {
            'description': 'It is the end. The night, the dark, the stars and full bright glowing moon and the sounds of night and it\'s wildlife.',
            'doors': {
                'Passage': {
                    'lead_to': 'Passage',
                    'description': 'Rush back to the safety of the Castle'
                },
                'END': {
                    'lead_to': 'END',
                    'description': 'Embrace the Moon and the howling of the beasts!'
                }
            }
        },
        'END': {
            'description': 'You became one with the Night...'
        }
    }
}

Dungeon(dungeon_data).run()
