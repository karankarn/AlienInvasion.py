class GameStats():
    def __init__(self,ai_settings):
        #initialize statistics
        self.ai_settings = ai_settings
        self.reset_stats()
        #start AI in an inactive state
        self.game_active = False
        #high score must never be reset
        self.high_score = 0

    def reset_stats(self):
        #initialize statistics that change during game
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
