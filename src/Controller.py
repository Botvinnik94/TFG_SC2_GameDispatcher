import time
import requests

class Controller:

    def __init__(self, repository, tournament_manager, game_manager):
        self.repository = repository
        self.tournament_manager = tournament_manager
        self.game_manager = game_manager

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

    def match_player(self):
        matches = self.repository.get_matches("ongoing")
        for match in matches:
            game = self.game_manager.game_from_match()
            task = self.game_manager.play_game.delay(match, game)
            match["taskId"] = task.id
        return len(matches)