from pathlib import Path

# Get root directory
def get_root_dir() -> Path:
    return Path(__file__).resolve().parent.parent

# Get data directory
def get_data():
    return get_root_dir() / 'data'
