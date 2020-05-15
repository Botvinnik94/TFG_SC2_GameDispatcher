import time
import requests
from GameService.GameManager import game_from_match, play_game

class Controller:

    def __init__(self, repository, tournament_manager, game_player):
        self.repository = repository
        self.tournament_manager = tournament_manager
        self.game_player = game_player

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
            self.tournament_manager.start_match(match)
        return len(matches)

    def match_player(self, match_id):
        match = self.repository.get_match(match_id)
        if match["status"] == "ongoing":
            game = game_from_match(match)
            play_game.delay(match, game)
            return match_id
        else:
            return None