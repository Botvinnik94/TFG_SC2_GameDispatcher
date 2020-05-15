from abc import ABC, abstractmethod
from worker.celeryApp import app

class GameManager:

    def __init__(self, tournament_manager, game_player):
        self.tournament_manager = tournament_manager
        self.game_player = game_player

    def game_from_match(self, match):
        game = {
            "participant1": match["players"][0],
            "participant2": match["players"][1],
            "winner": -1,
            "map": "placeholder",
            "replayURL": "placeholder"
        }
        return game

    @app.task
    def play_game(self, match, game):
        result = self.game_player.play(game)
        self.tournament_manager.report_match(match, result)
        pass