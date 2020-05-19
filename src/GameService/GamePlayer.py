from abc import ABC, abstractmethod
from random import randint
import time
import importlib

import sc2
from sc2 import run_game, maps, Race, Result
from sc2.player import Bot

class AbstractGamePlayer(ABC):

    @abstractmethod
    def play(self, bot1, bot2, sc2_map):
        pass


class StarcraftGamePlayer(AbstractGamePlayer):

    def play(self, bot1, bot2, sc2_map):
        Bot1 = getattr(importlib.import_module(bot1.name, '.'), bot1.name)
        Bot2 = getattr(importlib.import_module(bot2.name, '.'), bot2.name)
        replay_name = bot1.name + bot2.name + str(round(time.time() * 1000))
        result = run_game(maps.get(sc2_map), [
                            Bot(self._select_race(bot1.race), Bot1(), bot1.name),
                            Bot(self._select_race(bot2.race), Bot2(), bot2.name),
                        ], realtime=False, save_replay_as=replay_name)
        return {
            "result": result,
            "replay": replay_name
        }


    def _parse_result(self, result):
        if result is not None:
            if result[0] == Result.Victory:
                return 0
            elif result[1] == Result.Victory:
                return 1
            elif result[0] == result[1] == Result.Tie:
                return "draw"
            else:
                raise Exception("Invalid result, got " + str(result))
        else:
            raise Exception("Result is None")

    def _select_race(self, race):
        if race == 'Terran':
            return Race.Terran
        elif race == 'Protoss':
            return Race.Protoss
        elif race == 'Zerg':
            return Race.Zerg
        else:
            raise Exception("Invalid race: expected 'Terran', 'Protoss' or 'Zerg', got " + str(race))

class MockGamePlayer(AbstractGamePlayer):

    def play(self, bot1, bot2, sc2_map):
        time.sleep(20)
        return {
            "result": randint(0, 1),
            "replay": "mockReplay"
        }