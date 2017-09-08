import random


class Sturgeon:

    score = 0
    health = 20
    satiation = 1

    def getScore(self):
        return self.score

    def getHealth(self):
        return self.health

    def getSatiation(self):
        return self.satiation

    def takeDangerDamage(self):
        print("You took damage from a predator")
        self.health -= 10

    def takeSatiationDamage(self):
        print("You are starving.")
        self.health -= 1

    def incrementHealth(self):
        if self.health < 30:
            print("You feel healthier.")
            self.health += 1

    def incrementScore(self):
        self.score += 1

    def changeSatiation(self, amnt):
        self.satiation += amnt

    def calculateHealth(self, d):
        r = random.random()
        if r < d:
            self.takeDangerDamage()
        if self.getSatiation() < 0.5:
            self.takeSatiationDamage()
        elif self.getSatiation() >= 1:
            self.incrementHealth()

#-----------------------------------------------------------------------------------

danger = 0
food = 0.10


def makeMove(s: Sturgeon):
    global danger, food
    x = 0
    while x not in ["1", "2", "3"]:
        if danger >= 0.8:
            print("There are a lot of predators around.")
        if food <= 0.07:
            print("You are having a hard time finding food...")
        x = input("Choose an action\n1) Find food\n2) Move towards food\n3) Move away from predators\n")
    dangerRandom = random.random()
    foodRandom = random.random()
    if x == "1":
        s.changeSatiation(food)
    else:
        s.changeSatiation(-0.07)
    if x == "2":
        if foodRandom > 0.3:
            food += 0.2
        else:
            food += 0.05
    else:
        if foodRandom < 0.6:
            food -= 0.1
    if x == "3":
        if dangerRandom > 0.3:
            danger -= 0.15
        else:
            danger -= 0.05
    else:
        if dangerRandom < 0.6:
            danger += 0.05
    print()
    s.calculateHealth(danger)


def main():
    print("Welcome to Sturgeon Simulator\nYou are a sturgeon\nDon't die\n")
    mySturgeon = Sturgeon()
    while mySturgeon.getHealth() > 0:
        makeMove(mySturgeon)
        mySturgeon.incrementScore()
    print("Your sturgeon died./nScore is " + str(mySturgeon.getScore()))
    input("Thank you for playing")


main()
