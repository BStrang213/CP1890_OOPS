from dataclasses import dataclass

ROSHAMBO = ("rock", "paper", "scissors")


@dataclass
class player:
    name = ""
    player_choice

    def generateRoshambo(self):
        self.roshambo = ROSHAMBO[0]

    def play(self):
        print("place holder")


@dataclass
class Bart(player):
    name = "Bart"


@dataclass
class Lisa(player):
    name = "Lisa"
