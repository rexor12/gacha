from typing import Any


def get_or_add(dictionary: dict, key, value):
    existing_value = dictionary.get(key, None)
    if not existing_value:
        dictionary[key] = existing_value = value
    return existing_value