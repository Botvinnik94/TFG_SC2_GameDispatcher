from abc import ABC, abstractmethod
import requests
import yaml

with open('config.yaml') as f:
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
        return requests.put(url)

    def start_match(self, match):
        pass

    def report_match(self, match):
        pass