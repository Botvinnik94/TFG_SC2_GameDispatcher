from abc import ABC, abstractmethod
import requests
import yaml

with open('variables.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

class AbstractRepository(ABC):

    @abstractmethod
    def get_tournaments(self, status):
        pass

    @abstractmethod
    def get_matches(self, status):
        pass

    @abstractmethod
    def get_match(self, id):
        pass


class HttpRepository(AbstractRepository):

    def get_tournaments(self, status):
        url = config["HTTP_REPOSITORY_ENDPOINT"]
        r = requests.get(url, params={ "status": status })
        return r.json()

    def get_matches(self, status):
        url = config["HTTP_REPOSITORY_ENDPOINT"] + "matches"
        r = requests.get(url, params={ "status": status })
        return r.json()

    def get_match(self, match_id):
        url = config["HTTP_REPOSITORY_ENDPOINT"] + "matches/" + match_id
        r = requests.get(url)
        return r.json()
