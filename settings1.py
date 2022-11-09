class Settings:
    """Stores all settings for Alien Invasion"""
    def __init__(self):
        """Game Setting"""
        #Screen
        self.bg_color = (0, 0, 255)
        #Ship setting
        self.ship_speed = 1.5
        #Bullet Settings
        self.bullet_speed = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5
        #Alien settings
        self.star_speed = .05
        self.fleet_drop_speed = .05
        # fleet direction of 1 represents: -1 represents left
        self.fleet_direction = -1