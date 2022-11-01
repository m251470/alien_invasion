class Settings:
    """Stores all settings for Alien Invasion"""
    def __init__(self):
        """Game Setting"""
        #Screen
        self.bg_color = (0, 0, 255)
        #Ship setting
        self.ship_speed = 1.5
        #Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3