import random
from enums.attribute_enum import AttributeType

def roll_3d6():
    return sum(random.randint(1, 6) for _ in range(3))

def roll_4d6_drop_lowest():
    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)

def generate_classic():
    return {attr.value: roll_3d6() for attr in AttributeType}

def generate_adventurous():
    return [roll_3d6() for _ in range(6)]

def generate_heroic():
    return [roll_4d6_drop_lowest() for _ in range(6)]