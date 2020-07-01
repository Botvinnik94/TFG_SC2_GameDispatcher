from abc import ABC, abstractmethod
import requests
import yaml

with open('variables.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

class AbstractRepository(ABC):
    """This class represents an abstract database"""

    @abstractmethod
    def get_tournaments(self, status):
        """Get all tournaments from the database that are in a certain status"""
        pass

    @abstractmethod
    def get_matches(self, status):
        """Get all matches from the database that are in a certain status"""
        pass

    @abstractmethod
    def get_match(self, id):
        """Get a match from the database given its id"""
        pass


class HttpRepository(AbstractRepository):
    """This class represents a database accessed through HTTP endpoints"""

    def get_tournaments(self, status):
        """Get all tournaments from the database that are in a certain status"""
        url = config["HTTP_REPOSITORY_ENDPOINT"]
        r = requests.get(url, params={ "status": status })
        return r.json()

    def get_matches(self, status):
        """Get all matches from the database that are in a certain status"""
        url = config["HTTP_REPOSITORY_ENDPOINT"] + "matches"
        r = requests.get(url, params={ "status": status })
        return r.json()

    def get_match(self, match_id):
        """Get a match from the database given its id"""
        url = config["HTTP_REPOSITORY_ENDPOINT"] + "matches/" + match_id
        r = requests.get(url)
        return r.json()
