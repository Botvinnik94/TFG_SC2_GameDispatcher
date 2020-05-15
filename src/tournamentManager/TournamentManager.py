from abc import ABC, abstractmethod
import requests
import yaml
import json

with open('variables.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

class AbstractTournamentManager(ABC):

    @abstractmethod
    def initialize_tournament(self, tournament_id):
        pass

    @abstractmethod
    def start_match(self, match):
        pass

    @abstractmethod
    def report_match(self, match):
        pass


class HttpTournamentManager(AbstractTournamentManager):

    def initialize_tournament(self, tournament_id):
        url = config["HTTP_TOURNAMENT_MANAGER_ENDPOINT"] + tournament_id + "/initialize"
        response = requests.put(url)
        if response.status_code >= 400:
            raise Exception(str(response.status_code) + " Error in connection with Tournament Manager HTTP endpoint: " + response.reason)
        else:
            return response

    def start_match(self, match):
        url = config["HTTP_TOURNAMENT_MANAGER_ENDPOINT"] + match["tournamentId"] + "/startMatch"
        response = requests.put(url, data=dict(roundIndex=match["indexId"]["roundIndex"], matchIndex=match["indexId"]["matchIndex"]))
        if response.status_code >= 400:
            raise Exception(str(response.status_code) + " Error in connection with Tournament Manager HTTP endpoint: " + response.reason)
        else:
            return response

    def report_match(self, match, game):
        url = config["HTTP_TOURNAMENT_MANAGER_ENDPOINT"] + match["tournamentId"] + "/reportMatch"
        #reportObject = dict(winner=game["winner"], map=game["map"], replayURL=game["replayURL"])
        response = requests.put(url, json=dict(roundIndex=match["indexId"]["roundIndex"], matchIndex=match["indexId"]["matchIndex"], reportObject=dict(winner=game["winner"], map=game["map"], replayURL=game["replayURL"])))
        if response.status_code >= 400:
            raise Exception(str(response.status_code) + " Error in connection with Tournament Manager HTTP endpoint: " + response.reason)
        else:
            return response