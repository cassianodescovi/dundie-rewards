"""Core module of dundie"""


def load(filepath):
    """Loads data from filepaht to the database"""
    try:
        with open(filepath) as file_:
            return [line.strip() for line in file_.readlines()]
    except FileNotFoundError as e:
        print(f"File not found {e}")
