from abc import ABC, abstractmethod
from GameService.worker.celeryApp import app
from tournamentManager.TournamentManager import HttpTournamentManager
from GameService.GamePlayer import MockGamePlayer

tournament_manager = HttpTournamentManager()
storage_service = None
game_player = MockGamePlayer()

@app.task
def play_game(match, game):
    storage_service.get(game["participant1"]["script"])
    storage_service.get(game["participant2"]["script"])
    response = game_player.play(game["participant1"], game["participant2"], game["map"])
    replay_url = storage_service.put(response["replay"])
    game["winner"] = response["result"]
    game["replayURL"] = replay_url
    tournament_manager.report_match(match, game)
    # TODO: delete scripts from filesystem

def game_from_match(match):
    game = {
        "participant1": match["players"][0],
        "participant2": match["players"][1],
        "winner": -1,
        "map": "placeholder",
        "replayURL": "placeholder"
    }
    return game