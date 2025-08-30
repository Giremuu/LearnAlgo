#############################################################
#
#   classAll.py to repertoriate all class that I use for this project
#
#############################################################

class Player:
    def __init__(self, name, xp):
        self.name = name
        self.xp = xp
        self.level = self.calc_lvl()
    
    def add_xp_amount(self, amount: int):
        self.xp += amount
        self.level = self.calc_lvl()
        return self.xp

    def attack_power(self) -> int:
        base = 5
        scale = 2
        return base + (self.level - 1) * scale
    
    def calc_lvl(self):
        return self.xp // 100 + 1

#############################################################

class Enemy:
    def __init__(self, name, hp, xp_reward=15):
        self.name = name
        self.hp = hp
        self.max_hp = hp    # pour la barre de vie
        self.dead = False
        self.xp_reward = xp_reward

    def take_damage(self, amount: int = 5):
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.dead = True
        return self.hp

    def is_dead(self):
        return self.dead
