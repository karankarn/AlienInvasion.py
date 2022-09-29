class Settings():
    def __init__(self):
        """Initialize the games static settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #Ship Settings

        self.ship_limit = 3
        #Bullet Settings

        self.bullet_width = 10
        self.bullet_height = 10
        self.bullet_color = 0,0,0
        self.bullets_allowed = 3
        #Alien Settings
        self.fleet_drop_speed = 10
        #How quickly the game speeds up
        self.speedup_scale = 1.1
        #how quickly the alien point value increases
        self.score_scale = 1.5
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet direction +1 = right and -1 = left
        self.fleet_direction = 1
        self.alien_points = 50


    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points*self.score_scale)
        print(self.alien_points)