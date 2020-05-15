from abc import ABC, abstractmethod
from GameService.worker.celeryApp import app
from tournamentManager.TournamentManager import HttpTournamentManager
from GameService.GamePlayer import MockGamePlayer

tournament_manager = HttpTournamentManager()
game_player = MockGamePlayer()

@app.task
def play_game(match, game):
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