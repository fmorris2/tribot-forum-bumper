FILE_PATH = '/data/threads'

def load(root_path):
    return open(root_path + FILE_PATH).read().splitlines()