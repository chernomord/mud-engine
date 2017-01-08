from dungeon import Dungeon
import yaml


with open("dungeon.yaml", 'r') as stream:
    try:
        Dungeon(yaml.load(stream)).run()
    except yaml.YAMLError as exc:
        print(exc)
