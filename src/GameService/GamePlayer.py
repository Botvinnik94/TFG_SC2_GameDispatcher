from abc import ABC, abstractmethod

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
        pass