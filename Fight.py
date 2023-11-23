import random
import matplotlib.pyplot as plt
class Sword():
    def __init__(self):
        self.dmg = 8

class Magic_sword():
    def __init__(self):
        self.dmg = random.randint(6, 13)


class Fighter(Sword, Magic_sword):
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
        self.hp = 60
        if weapon == 'sword':
            self.atk = Sword().dmg
        if weapon == 'magic sword':
            self.atk = Magic_sword().dmg

    def hp_waste(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
    def dmg(self, new_hp):
        self.hp = new_hp

    def info(self):
        info= (f'{self.name} HP: {self.hp}')
        print(info)


    def alive(self):
        return self.hp > 0

fighter1 = Fighter(name="Yasuo", weapon="sword")
fighter2 = Fighter(name="Yone", weapon="magic sword")

def fight(Fighter1, Fighter2):
    n = 1
    passive = 0
    while Fighter1.alive() and Fighter2.alive():
        if passive != 4:
            new_hp = Fighter1.hp - Fighter2.atk
            Fighter1.dmg(new_hp)
        else:
            print(f'{Fighter1.name} dodged')
        new_hp = Fighter2.hp + int(0.15 * fighter2.atk)
        Fighter2.dmg(new_hp)
        new_hp = Fighter2.hp - Fighter1.atk
        Fighter2.dmg(new_hp)
        if passive == 4:
            passive = -1
        passive+=1
        if n == 1:
            if Fighter1.hp < 60:
                print(f'{Fighter1.name} use shield')
                new_hp = 60
                Fighter1.dmg(new_hp)
                n-=1
        Fighter1.info()
        Fighter2.info()

        if Fighter1.alive():
            print(f'{Fighter1.name} win!')
            score[0] +=1
        elif Fighter2.alive():
            print(f'{Fighter2.name} win!')
            score[1] += 1
        else:
            print(f'Draw')


score = [0,0]
100 * fight(fighter1, fighter2)
labels = ["Yasuo wins", "Yone wins"]
plt.pie(score, labels=labels, autopct='%1.1f%%')
plt.title("Distribution of wins")
plt.show()