import os
import json
import time
import unicodedata
import re


def _slugify(value: str) -> str:
    """Return an ASCII-only slugified version of *value*.

    This is used to create safe filenames from character names.
    """
    if not value:
        return "character"
    value = str(value)
    value = unicodedata.normalize('NFKD', value)
    value = value.encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\n\w\- ]', '', value).strip().lower()
    value = re.sub(r'[-\s]+', '_', value)
    return value or 'character'


def save_character_to_json(character, folder: str = 'saves') -> str:
    """Save a Character instance to a JSON file.

    The function converts the top-level object with .__dict__ and also
    converts nested `race` and `classe` objects to their own __dict__ so
    the resulting JSON is serializable.

    Returns the path to the saved file.
    """
    os.makedirs(folder, exist_ok=True)
    timestamp = int(time.time())
    safe_name = _slugify(getattr(character, 'name', f'character_{timestamp}'))
    filename = f"character_{safe_name}_{timestamp}.json"
    filepath = os.path.join(folder, filename)

    # Prepare a serializable dict from the Character instance
    data = {}
    try:
        data = character.__dict__.copy()
    except Exception:
        # Fallback: try to build minimal representation
        data = {
            'name': getattr(character, 'name', None),
            'attributes': getattr(character, 'attributes', None),
            'hit_points': getattr(character, 'hit_points', None)
        }

    # Replace nested objects with their __dict__ or simple names
    race_obj = getattr(character, 'race', None)
    classe_obj = getattr(character, 'classe', None)

    if race_obj is not None:
        try:
            data['race'] = race_obj.__dict__.copy()
        except Exception:
            data['race'] = {'name': getattr(race_obj, 'name', str(race_obj))}

    if classe_obj is not None:
        try:
            data['classe'] = classe_obj.__dict__.copy()
        except Exception:
            data['classe'] = {'name': getattr(classe_obj, 'name', str(classe_obj))}

    # Write JSON file
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return filepath
