import time, cfscrape, lxml.html
from loaders import credential_loader, thread_loader

class Bot:
    #forum bumping interval - how long we have to wait between bumps
    CYCLE_TIME = (60 * 60 * 4) + 1

    LOGIN_URL = 'https://tribot.org/forums/login/'
    USER_AGENT = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'

    """
    An object that represents the forum bumper
    and all of it's functionality.

    Attributes:
        root_path = absolute path to this running program
        threads (list containing the thread URLs we're going to bump)
        credentials (tuple containing the user / pass to the TRiBot forums)
        cfscraper (cfscraper instance)
    """
    def __init__(self, root_path):
        self.root_path = root_path
        self.credentials = credential_loader.load(root_path)

    """
    The main cycle method. Fires up a cfscrape instance, 
    bumps the required threads, and sleeps until the 
    next bump time
    """
    def cycle(self):
        self.threads = thread_loader.load(self.root_path)
        self.create_scraper()
        self.bump_threads()
        time.sleep(self.CYCLE_TIME)

    """
    Creates a new cfscrape instance
    and sets user agent
    """
    def create_scraper(self):
        self.cfscraper = cfscrape.create_scraper()
        self.cfscraper.headers = {'user-agent' : self.USER_AGENT}

    """
    Logs-in to TRiBot forums.
    Navigates to specified threads,
    sending the "bump" action for each
    of them.
    """
    def bump_threads(self):
        if self.login():
            print 'Successfully logged in to TRiBot forums'
            for thread in self.threads:
                self.bump(thread)
            return
        print 'Could not log in to TRiBot forums'

    """
    Navigate to the specific forum thread.
    If the thread is on bump-cooldown, do
    nothing. Otherwise, parse the bump link
    and send a GET request to it
    """
    def bump(self, thread):
        print 'Attempting to bump thread: ' + thread
        thread_page = self.cfscraper.get(thread)
        if self.is_thread_on_cooldown(thread_page.content):
            print 'Thread is currently on bump cooldown!'
        else:
            bump_link = self.parse_bump_link(thread_page.content)
            if bump_link is not None:
                self.cfscraper.get(bump_link)
                print 'Thread has been bumped'

    """
    Given the HTML of a thread page,
    parse the link for the bump action
    """
    def parse_bump_link(self, html):
        root = lxml.html.document_fromstring(html)
        bump_link = root.get_element_by_id('elBumpEnabled')
        return bump_link.get('href')

    """
    Parse the thread page,
    and see if the bump cooldown element
    is active
    """
    def is_thread_on_cooldown(self, html):
        return '<span id="elBumpDisabled' in html

    """
    Returns the mapping of post parameters to values
    for the login request
    """
    def get_post_payload(self, hidden_fields):
        hidden_fields['auth'] = self.credentials[0]
        hidden_fields['password'] = self.credentials[1]
        hidden_fields['google2fa'] = '55555'
        hidden_fields['signin_anonymous_checkbox'] = '1'
        hidden_fields['signin_anonymous'] = '0'
        hidden_fields['remember_me'] = '0'
        return hidden_fields

    """
    Parses hidden form fields from the page source on
    the TRiBot login page
    """
    def parse_form_fields(self, html):
        dict = {}
        root = lxml.html.document_fromstring(html) # you can pass parse() a file-like object or an URL
        for form in root.xpath('//form[@action="https://tribot.org/forums/login/"]'):
            for field in form.getchildren():
                if 'name' in field.keys():
                    dict[field.get('name')] = field.get('value')
        return dict

    """
    Login to TRiBot forums,
    returns whether or not it
    was successful
    """
    def login(self):
        #first, send a git request to get the login page source
        login_page = self.cfscraper.get(self.LOGIN_URL)
        #parse the hidden form fields from the page (related to our session)
        hidden_fields = self.parse_form_fields(login_page.content)
        #POST the login page with the necessary fields
        response = self.cfscraper.post(self.LOGIN_URL, data=self.get_post_payload(hidden_fields))
        return '<title>Sign In - TRiBot Forums' not in response.content
