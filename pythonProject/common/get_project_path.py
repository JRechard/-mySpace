import os


def get_path():
    path = os.path.split(os.path.dirname(__file__))[0]
    return path
