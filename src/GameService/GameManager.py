from abc import ABC, abstractmethod
from GameService.worker.celeryApp import app
from tournamentManager.TournamentManager import HttpTournamentManager
from GameService.GamePlayer import StarcraftGamePlayer
from random import randint
import os

import storageService.FirebaseStorageService as storage_service

tournament_manager = HttpTournamentManager()
game_player = StarcraftGamePlayer()

maps = [
    "PortAleksanderLE",
    "AutomatonLE",
    "CeruleanFallLE",
    "ParaSiteLE",
    "StasisLE",
    "BlueshiftLE",
    "KairosJunctionLE"
]

@app.task
def play_game(match, game):
    """
        Complete logic for playing a game given its match.
        Gets the scripts from the storage service, plays the game
        and reports the result
    """

    # Get scripts from storage service
    storage_service.get('GameService/' + game["participant1"]["name"] + '.py', game["participant1"]["script"])
    storage_service.get('GameService/' + game["participant2"]["name"] + '.py', game["participant2"]["script"])

    # Play the game using those scripts
    response = game_player.play(game["participant1"], game["participant2"], game["map"])

    # Upload replay from the game to the storage service
    replay_url = storage_service.put(response["replay"], 'replays/' + response["replay"])

    # Report the match to the tournament manager
    game["winner"] = response["result"]
    game["replayURL"] = replay_url
    tournament_manager.report_match(match, game)

    # Remove scripts & replay from the filesystem
    os.remove(response["replay"])
    os.remove('GameService/' + game["participant1"]["name"] + '.py')
    os.remove('GameService/' + game["participant2"]["name"] + '.py')


def game_from_match(match):
    """Returns a new instance of a game for the match passed"""
    game = {
        "participant1": match["players"][0],
        "participant2": match["players"][1],
        "winner": -1,
        "map": maps[randint(0, len(maps) - 1)],
        "replayURL": "placeholder"
    }
    return game