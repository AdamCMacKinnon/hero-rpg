#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Hero:
    def __init__(self,health,power):
        self.health = health
        self.power = power
    def attack(self, enemy):
        enemy.health -= self.power
    def alive(self, health):
        if health > 0:
            return True
        else:
            False
    def print_status(self, health):
        


class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self, hero):
        hero.health -= self.power
    def alive(self, health):
        if health > 0:
            return True
        else:
            False


def main():
    hero = Hero(10,5)
    goblin = Goblin(6,2)
    

    while goblin.alive(goblin.health) and hero.alive(hero.health):
        print(f"You have {hero.health} health and {hero.power} power.".format(hero.health, hero.power))
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(goblin)
            print(f"You do {hero.power} damage to the goblin.")
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        if goblin.health > 0:
            #goblin attacks hero
            goblin.attack(hero)
            print("The goblin does {} damage to you.".format(goblin.power))
            if hero.health <= 0:
                print("You are dead.")



main()
