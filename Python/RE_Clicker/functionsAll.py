#############################################################
#
#   functionsAll.py is used to regroup all gameplay functions
#
#############################################################

from classAll import Player, Enemy
import random

#############################################################

def show_player(player):
    """ Return a simple summary of the player """
    return f"{player.name} | XP: {player.xp} | Level: {player.level}"

#############################################################

def create_random_enemy():
    pool = [
        Enemy("Slime1", 100, xp_reward=20),
        Enemy("Slime2", 150, xp_reward=30),
        Enemy("Slime3", 200, xp_reward=40),
    ]
    return random.choice(pool)

def attack_enemy_with_player(player, enemy):
    dmg = player.attack_power()
    enemy.take_damage(dmg)
    if enemy.is_dead():
        return dmg, True, enemy.xp_reward
    return dmg, False, 0

def enemy_status(enemy):
    status = "Dead" if enemy.dead else "Alive"
    return f"{enemy.name} | HP: {enemy.hp} | {status}"

#############################################################