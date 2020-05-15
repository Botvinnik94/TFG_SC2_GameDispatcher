from abc import ABC, abstractmethod
from .worker.celeryApp import app

@app.task
def play_game(tournament_manager, game_player, match, game):
    result = game_player.play(game)
    tournament_manager.report_match(match, result)

def game_from_match(match):
    game = {
        "participant1": match["players"][0],
        "participant2": match["players"][1],
        "winner": -1,
        "map": "placeholder",
        "replayURL": "placeholder"
    }
    return game