#RPG GAME 1
class Character: 
  def __init__(self, health, power):
    self.name = 'Heo'
    self.health = health
    self.power = power

  def status(self):
   if self.health > 0: 
      return True
   return False

  def print_status(self):
    print('You have %d health and %d power.' % (self.health, self.power))

class Hero(Character):
  def attack(self, enemy):
    enemy.health -= self.power
    print('You do %d damamge to the Goblin.' % self.power)

  def print_status(self):
    print('You have %d health and %d power.' % (self.health, self.power))

class Goblin(Character):
  def attack(self, swordsman):
    swordsman.health -= self.power
    print('The goblin does %d damage to you.' % self.power)

  def print_status(self): 
    print('You have %d health and %d power.' % (self.health, self.power))

def begin():
  swordsman = Hero(10, 5)
  enemy = Goblin(6, 2)

  while enemy.status() and swordsman.status():
    def print_status(self):
    def print_status(self):