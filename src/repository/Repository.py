from abc import ABC, abstractmethod
import requests

class AbstractRepository(ABC):

    @abstractmethod
    def get_tournaments(self, status):
        pass

    @abstractmethod
    def get_matches(self, status):
        pass


class HttpRepository(AbstractRepository):

    def get_tournaments(self, status):
        url = "http://localhost:5001/sc2-arena/us-central1/api"
        r = requests.get(url, params={ "status": status})
        return r.json()

    def get_matches(self, status):
        url = "http://localhost:5001/sc2-arena/us-central1/api/matches"
        r = requests.get(url, params={"status": status})
        return r.json()