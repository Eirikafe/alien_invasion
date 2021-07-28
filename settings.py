class Settings:

    def __init__(self):
        # settings for the game's window size and background color
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)
        # setting for ship's speed
        self.ship_speed = 1.5
        # settings for bullets
        self.ship_limit = 3
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
