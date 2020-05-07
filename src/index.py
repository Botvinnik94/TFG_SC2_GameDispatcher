import json

from Controller import Controller
from flask import Flask, request, Response
from repository.Repository import HttpRepository
from tournamentManager.TournamentManager import HttpTournamentManager
from GameService.GamePlayer import MockGamePlayer
from GameService.GameManager import GameManager

app = Flask(__name__)

repository = HttpRepository()
tournament_manager = HttpTournamentManager()
game_player = MockGamePlayer()
game_manager = GameManager(tournament_manager, game_player)

controller = Controller(repository, tournament_manager, game_manager)

@app.route("/check-tournaments", methods=["PUT"])
def check_tournaments():
    initialized_tournaments = controller.tournament_initializer()
    return Response(str(initialized_tournaments), 200)

@app.route("/check-matches", methods=["PUT"])
def check_matches():
    matches_started = controller.match_initializer()
    return Response(str(matches_started), 200)