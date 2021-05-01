"""Powerups and random events"""

from random import randint

class Effects:
    """contains methods and variables used for effects"""
    def __init__(self):
        self.powerups = {}
        self.timer = 0
        self.powerups["BOINGBOING"] = False
        self.powerups["INDESTRUCTIBILITY"] = False
        self.powerups["REVERSE"] = False
        self.active = ""

    def countdown(self):
        """Runs timer and deactivates powerups"""
        if self.timer > 0:
            self.timer -= 1
            if self.timer == 0:
                for key in self.powerups:
                    self.powerups[key] = False
                    self.active = ""

    def random_powerup(self):
        """Activates random powerup"""
        randomizer = randint(0,2)
        for key in self.powerups:
            if randomizer == 0:
                self.powerups[key] = True
                self.timer = 1000
                self.active = key
            randomizer -= 1

    #def get_active_powerup(self):
    #    """returns name of active powerup"""
    #    for key, value in self.powerups.items():
    ##        if value:
    #            return key
    #    return ""
