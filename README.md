# Overview of TRiBot Forum Bumper (TFB)
To be ran continuously, will log in to the specified forum account (in data/credentials file), and bump the specified threads. TRiBot has a 4 hour interval between forum bumps.

### Architecture
- Language: [Python](https://www.python.org/)
- Libraries / Modules:
    - [cloudflare-scrape](https://github.com/Anorov/cloudflare-scrape)
    - [pyotp](https://github.com/pyotp/pyotp)
    - [lxml](http://lxml.de/)
    - [Requests](http://docs.python-requests.org/en/master/)
    - [PyExecJS](https://pypi.python.org/pypi/PyExecJS)
    - [Node.js](https://nodejs.org/en/)

### Basic Logic Flow
1. Startup routine
    - Load forum credentials from file
2. Main cycle
    - Load forum threads to bump from file (loaded every cycle in case a change is made between cycles)
    - Log in to [TRiBot](http://www.tribot.org) forums
    - Bump each specified thread
        - Navigate to thread's page
        - Utilize bump feature
    - Sleep for specified cycle time (bump interval)
    
### Deployment
1. Install Python
2. Install cfscrape module
3. Install lxml module
4. Install Requests module
5. Install PyExecJS module
6. Install pyotp module
7. Install Node.js
8. Run!

### Usage
1. Create a file "credentials" in the project/data/ directory with the contents:
    - tribot username
    - tribot password
    - 2fa secret key
2. Create a file "threads" in the project/data/ folder with the link to each thread you want to bump. One thread per line!
    - http://www.tribot.org/forums/thread_one
    - http://www.tribot.org/forums/thread_two
    
