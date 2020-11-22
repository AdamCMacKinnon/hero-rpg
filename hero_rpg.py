
# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee



class Character:
    def __init__(self,health,power):
        self.health = health
        self.power = power
    def attack(self, enemy):
        enemy.health -= self.power
    def alive(self ,health):
        if health > 0:
            return True
        else:
            False
    def print_status(self, health):
        if __class__ == Hero:
            print(f'You have {self.health} health and {self.power} power left!')
        else:
            print(f'Your enemy has {self.health} health and {self.power} left!')


class Hero(Character):
    def hero (self,health,power,gold):
        self.health = health
        self.power = power
        self.gold = gold
    def hero_status(self, health):
        print(f"You have {self.health} health and {self.power} power.")
    def hero_gold(self, gold):
        self.gold += 20
        print(f'you currently have {self.gold} peices of gold!')
    # def critical_hit(self,power):
    #     if (random.randint(1,5) == 5):
    #         self.power * 2
    #     print('You landed a critical hit!')
    



class Enemy(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def attack(self, hero):
        hero.health -= self.power
    def enemy_status(self, health):
        print(f'The enemy has {self.health} health and {self.power} power left!')

class Orc(Enemy): #'Goblin'
    def __init__(self):
        super().__init__(name='Orc', health=15, power = 3)
    def attack(self, hero):
        hero.health -= self.power
        print(f'The Orc slashes at you!')

class Zombie(Enemy):
    def __init__(self):
        super().__init__(name='Zombie', health=10, power = 2)
    def alive(self, health):
        return True
    def attack(self, hero):
        hero.health -= self.power
        print(f'The Zombie lunges forward for a bite!')

class Wraith(Enemy): #'Shadow'
    def __init__(self):
        super().__init__(name='Wraith', health=1, power = 4)
    def attack(self, hero):
        hero.health -= self.power
        print('The Wraith creeps toward you and strikes!')
    def alive(self, health):
        if(random.randint(1,10) <= 9):
            return True
        else:
            return False

class Mage(Enemy): # 'Medic'
    def __init__(self):
        super().__init__(name='Mage', health=15, power = 3)
    def attack(self, hero):
        hero.health -= self.power
        print('The Mage casts a destruction spell!')
    def recharge(self, health):
        if random.randint(1,10 <= 8):
            self.health + 2
            print('The Mage uses Regenerate to reclaim 2 health!')
        else:
            return False



def store():
    weapon = 50
    potion = 20
    
    
    
    print('Welcome to the Market.')
    print('1.) WEAPONS')
    print('2.) POTIONS')
    print('3.) EXIT MARKET')
    inventory = input()
    if inventory == '1':
        raw_input = input(f'do you want to purchase the legendary SWORD OF 1000 TRUTHS for {weapon}? TYPE YES OR NO' )
        if raw_input == 'yes':
            print('you have acquired the SWORD OF 1000 TRUTHS! Your power is raised by double!')
        else:
            print('ok!')
            store()
    if inventory == '2':
        raw_input = input(f'do you want to purchase the helpful POTION OF THE HEALER for {potion}? TYPE YES OR NO ')
        if raw_input == 'yes':
            print('you have acquired the POTION OF THE HEALER!  10 health is added!')
        else:
            print('ok!')
            store()
        for x in zip(potion):
            print('--------------------')
            print(x)
    if inventory == '3':
        print('Come back when you want to spend!')
        main()
    



def intro():
        print(f'''
            -------||*************************
                        QUEST 
            *************************||-------
                        OF
            -------||*************************
                        HEROES
            *************************||-------
            ''')  

def main():
    print('what would you like to do?')
    print('1.) Explore')
    print('2.) Visit the Market.')
    print('3.) Go to the bar for some Ale!')
    print('4.) Leave this realm!')
    raw_input = input()
    if raw_input == '1':
        print('Wander the lands as you see fit!')
        battle()
    elif raw_input == '2':
        print('See what\'s for sale!')
        store()
    elif raw_input == '3':
        print(f'''
                You get too drunk and pass out!
                
        ''')
        
        main()
    elif raw_input == '4':
        print('Be gone, coward!!')
    
        

import random



def battle():
    wraith= Wraith()
    orc = Orc()
    zombie = Zombie()
    mage = Mage()
    enemyList = [wraith, zombie, orc, mage]

    enemy = random.choice(enemyList)
    hero = Hero(25,5)
    # enemy = enemy()
    


    while enemy.alive(enemy.health) and hero.alive(hero.health):
    
        

        
        print(f'''
                A RUSTLING IN THE BUSHES!
                PREPARE TO FIGHT!!
                A {enemy.name} EMERGES!
                '''
        )   
        hero.hero_status(hero.health)
        enemy.enemy_status(enemy.health)

        print("What do you want to do?")
        print("1. fight!")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(enemy)
            print(f"You do {hero.power} damage to the enemy.")
            if enemy.health <= 0:
                print("You have vanquished your enemy!.")
                print( '''
                ----------------------------
                ''')
                
                print(f'The townspeople are so grateful for your ridding of this menace \n they reward you with 20 gold!')
                
        elif raw_input == "2":
            print(f'you freeze in terror!')
        elif raw_input == "3":
            print("Fly! Coward!")
            main()
            break
        else:
            print("Invalid input {}".format(raw_input))
        if enemy.health > 0:
            #goblin attacks hero
            enemy.attack(hero)
            print("{} damage was done!".format(enemy.power))
            if hero.health <= 0:
                print("You are dead.")
    return main()            


intro()
main()


