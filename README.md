# Overview of TRiBot Forum Bumper (TFB)
To be ran continuously, will log in to the specified forum account (in data/credentials file), and bump the specified threads as soon as they can. TRiBot has a 3 hour interval between forum bumps.

### Architecture
- Language: [Python](https://www.python.org/)
- Libraries:
    - [Mechanize](http://mechanize.readthedocs.io/en/latest/index.html)

### Basic Logic Flow
1. Startup routine
    - Load forum credentials from file
    - Load forum threads to bump from file
2. Main cycle
    - Fire up Mechanize browser
    - Log in to TRiBot forums
    - Bump each specified thread
        - Navigate to thread's page
        - Utilize bump feature
    - Shut down Mechanize browser
    - Sleep for specified cycle time (bump interval)
    
### Deployment
(Coming soon)

### Usage
(Coming soon)
