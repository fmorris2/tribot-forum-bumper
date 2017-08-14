FILE_PATH = '/data/credentials'

def load(root_path):
    lines = open(root_path + FILE_PATH).read().splitlines()
    return lines[0], lines[1]