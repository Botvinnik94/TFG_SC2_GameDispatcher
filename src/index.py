import json

from Controller import Controller
from flask import Flask, request, Response
from repository.Repository import HttpRepository
from tournamentManager.TournamentManager import HttpTournamentManager

app = Flask(__name__)
controller = Controller(HttpRepository(), HttpTournamentManager())

@app.route("/check-tournaments")
def check_tournaments():
    initialized_tournaments = controller.tournament_initializer()
    return Response(str(len(initialized_tournaments)), 200)