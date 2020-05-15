from abc import ABC, abstractmethod
from random import randint
from time import sleep

class AbstractGamePlayer(ABC):

    @abstractmethod
    def play(self, game):
        pass


class StarcraftGamePlayer(AbstractGamePlayer):

    def play(self, game):
        # TODO: execute SC2 game
        pass

class MockGamePlayer(AbstractGamePlayer):

    def play(self, game):
        winner = randint(0, 1)
        game["winner"] = winner
        game["map"] = "mockMap"
        game["replayURL"] = "mockReplay"
        sleep(20)
        return game