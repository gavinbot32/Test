class Player(object):
    __player_count = 0
    def __init__(self):
        Player.__player_count += 1
        self.health  = 3
        self.attackdmg = 1
    def __show_player_count__():
        print(Player.__player_count)

    def die(self):
        if self.health <= 0:
            print("the player has died")


    def shoot(self,target,damage):
        target.take_damage(damage)

    def take_damage(self, dmg):
        self.health -= dmg
        self.die()


class Alien(object):
    def __init__(self):
        self.health = 3
        self.attackdmg = 1

    def take_damage(self,dmg):
        self.health -= dmg
        self.die()

    def die(self):
        if self.health <= 0:
            print("the enemy has died")

    def shoot(self,target,damage):
        target.take_damage(damage)

player = Player()
enemy = Alien()
player.shoot(enemy,player.attackdmg)
player.shoot(enemy,player.attackdmg)
player.shoot(enemy,player.attackdmg)
enemy.shoot(player,enemy.attackdmg)
enemy.shoot(player,enemy.attackdmg)
enemy.shoot(player,enemy.attackdmg)