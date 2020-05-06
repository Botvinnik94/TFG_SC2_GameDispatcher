import time
import requests

class Controller:

    def __init__(self, repository, tournament_manager):
        self.repository = repository
        self.tournament_manager = tournament_manager

    def tournament_initializer(self):
        tournaments = self.repository.get_tournaments("open")
        now = int(round(time.time() * 1000))
        tournaments_to_initialize = list(filter(lambda t: now > int(t["startingDate"]), tournaments))
        for tournament in tournaments_to_initialize:
            self.tournament_manager.initialize_tournament(tournament["id"])
        return len(tournaments_to_initialize)
    
    def match_initializer(self):
        matches = self.repository.get_matches("pending")
        for match in matches:
            # TODO: send to task queue here
            self.tournament_manager.start_match(match)
        return len(matches)