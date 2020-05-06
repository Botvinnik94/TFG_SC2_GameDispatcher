from abc import ABC, abstractmethod
import requests

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
        url = "http://localhost:5001/sc2-arena/us-central1/private/" + tournament_id + "/initialize"
        return requests.put(url)

    def start_match(self, match):
        pass

    def report_match(self, match):
        pass