import time
from loaders import credential_loader, thread_loader

class Bot:

    #forum bumping interval - how long we have to wait between bumps
    CYCLE_TIME = 60 * 60 * 3

    """
    An object that represents the forum bumper
    and all of it's functionality.

    Attributes:
        threads (list containing the thread URLs we're going to bump)
        credentials (tuple containing the user / pass to the TRiBot forums)
    """
    def __init__(self, root_path):
        self.credentials = credential_loader.load(root_path)
        self.threads = thread_loader.load(root_path)

    """
    The main cycle method. Fires up a mechanize
    browser, bumps the required threads, shuts down
    the browser, and sleeps until the next bump time
    """
    def cycle(self):
        print 'cycling'
        time.sleep(self.CYCLE_TIME)

