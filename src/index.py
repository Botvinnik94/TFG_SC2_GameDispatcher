import json

from Controller import Controller
from flask import Flask, request
from repository.Repository import HttpRepository
from tournamentManager.TournamentManager import HttpTournamentManager

app = Flask(__name__)
controller = Controller(HttpRepository(), HttpTournamentManager())

@app.route("/check-tournaments")
def check_tournaments():
    controller.tournament_initializer()
    return "OK"

if __name__ == '__main__':
    app.run(debug=True)