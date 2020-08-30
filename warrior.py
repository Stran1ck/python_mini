class Warrior:
    health = 100

    def setname(self, n):
        self.name = n

    def getname(self):
        try:
            return self.name
        except:
            print("No name")

    def kick(self, unit):
        unit.health -= 20
        print(str(self.getname()) + ' атаковал.')
        print('У ' + unit.getname() + ' осталось ' + str(unit.health) + ' жизни.')
        if unit.health <= 0:
            print(self.getname() + ' победил')
            return 0


unit_1 = Warrior()
unit_2 = Warrior()

unit_1.setname(input('Введите имя первого бойца:  '))
unit_2.setname(input('Введите имя второго бойца:  '))

while True:
    a = 1
    c = input('Введи имя атакующего бойца:   ')
    if c == unit_1.getname():
        a = unit_1.kick(unit_2)

    elif c == unit_2.getname():
        a = unit_2.kick(unit_1)
    else:
        print('Хреново набрано имя')
    if a == 0:
        break
