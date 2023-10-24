#import github as gh
from lib.github import gitCommands as gh
import os

def update():
    if gh.check() == True:
        gh.update()
        update()
        os.system("sudo reboot")
    return True



def setup():
    None

def loop():
    None

update()