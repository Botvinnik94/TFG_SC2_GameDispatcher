import time
import requests
from GameService.GameManager import game_from_match, play_game

class Controller:
    """This class is the controller class for the REST API handlers. The methods are the exposed services"""

    def __init__(self, repository, tournament_manager, game_player):
        self.repository = repository
        self.tournament_manager = tournament_manager
        self.game_player = game_player

    def tournament_initializer(self):
        """Gets all open tournaments from the database and initializes the ones whose starting day is today"""

        tournaments = self.repository.get_tournaments("open")
        now = int(round(time.time() * 1000))
        tournaments_to_initialize = list(filter(lambda t: now > int(t["startingDate"]), tournaments))
        for tournament in tournaments_to_initialize:
            self.tournament_manager.initialize_tournament(tournament["id"])
        return len(tournaments_to_initialize)

    def match_initializer(self):
        """Gets all pending matches from the database and starts them"""

        matches = self.repository.get_matches("pending")
        for match in matches:
            self.tournament_manager.start_match(match)
        return len(matches)

    def match_player(self, match_id):
        """Gets the match to be played from the database and invokes the procedure to play it. Returns immediately"""

        match = self.repository.get_match(match_id)
        if match["status"] == "ongoing":
            game = game_from_match(match)
            play_game.delay(match, game)
            return match_id
        else:
            return None