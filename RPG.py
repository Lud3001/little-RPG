from random import choice , randint # randint выбирает случайное число от наименьшего до наибольшего в диапазоне, которое я задаю
race = ['elf', 'dwarf', 'human']
dict_race = {race[0]: {'health' : 1 , 'damage' : 1},
            race[1] : {'health' : 5 , 'damage' : 1},
            race[2] : {'health' : 1 , 'damage' : 1}}
jobs = [('archer' , 1, 1) , ('knite' , 1, 1)]
dict_jobs = {}
for i in jobs:
    dict_jobs[i[0]] = {'health' : i[1] , 'damage' : i[2]}
dict_monster = {'vampire' : {'health' : 3 , 'damage' : 1},
                'zombie' : {'health' : 1 , 'damage' : 1},
                'clown' : {'health' : 2 , 'damage' : 1}}
weapon = ['sword' , 'katana' , 'fire ball']
boost = {'vampire' : {'boost_potion' : 3 , 'shield' : 1} , # shield - +1 health 
        'zombie' : {'vitamins': 1, 'poisoned slime' : 1} , # slime -- +1 damage 
        'clown' : {'healthy_lollypop' : 2 , 'scary nose' : 1}} # scary nose --- +1 damage 

class Character():
    def __init__(self , name , health , damage):
        self.name = name
        self.health = health
        self.level = 1
        self.damage = damage
    def __del__(self):
        pass

class Main_character(Character):
    bag = []
    def __init__(self, name , health , damage):
        super().__init__(name, health , damage) # эта конструкция позволяет подтянуть все параметры и методы из родительского класса
        self.exp = 0 # exp = experience
    def characteristics(name , race , job):
        health = 0
        damage = 0
        while True:
            if race in dict_race:
                for i in dict_race:
                    if i == race:
                        health = dict_race[i]['health']
                        damage = dict_race[i]['damage']
                        break
                break
            else:
                print('error, input "elf" , "dwarf" , or "human"')
                race = input()
        while True:
            if job in dict_jobs:
                for i in dict_jobs:
                    if i == job:
                        health += dict_jobs[i]['health']
                        damage += dict_jobs[i]['damage']
                        break
                break
            else:
                print('error, input another job')
                job = input()
                
        return Main_character(name , health , damage)
    def behavior(self , enemy):
        damage_range = {'missed' : 0,
                        'damage': self.damage,
                        'double_damage': self.damage*2}
        fight = randint(0,9)
        if fight == 0:
            enemy.health -= 0
        elif 1 <= fight <=8:
            enemy.health -= damage_range['damage']
        else:
            enemy.health -= damage_range['double_damage']
       


        



class Monster(Character):
    def __init__(self, name , health , damage):
        super().__init__(name, health , damage)
        self.name = name # name = race
        self.health = health
        self.damage = damage
    def characteristics():
        race = choice(list(dict_monster.keys()))
        health = dict_monster[race]['health']
        damage = dict_monster[race]['damage']
        return Monster(race , health , damage)
    def beahvior_monster (self, character):
        damage_range = {'missed' : 0,
                        'damage': self.damage,
                        'double_damage': self.damage*2}
        hit_back = randint(0,12)
        if hit_back == 0:
            character.health -= 0
        elif 1 <= hit_back < 12:
            character.health -= damage_range['damage']
        else:
            character.health -= damage_range['double_damage']
    
def battle():
    global hero , enemy
    if hero.health > 0:
        hero.behavior(enemy)
    elif hero.health <= 0:
        print('game over') 
        quit()   # эта функция закрывает консольное окно, то есть программа завершает свое выполнение
    if enemy.health > 0:
        enemy.beahvior_monster(hero)
    elif enemy.health <= 0:
        print('you win')



    
character_name = input('name: ')
character_race = input('race: ')
character_job = input('job: ')
character_weapon = input('choose your weapon: sword, katana or fire ball ')
Main_character.bag.append(character_weapon)
hero = Main_character.characteristics(character_name, character_race, character_job)
print(hero.health , hero.damage)
enemy = Monster.characteristics()
print(enemy.health , enemy.name , enemy.damage)
print(Main_character.bag)
start = input('would you like to start the game? input "yes" or "no"')
if start == 'yes':
    while True:
        print(f'your enemy is {enemy.name} \nit has {enemy.health} of health \nit has {enemy.damage} of damage')
        print(f'\nyou have {hero.health} of health \nyou have {hero.damage} of damage')
        battle()





