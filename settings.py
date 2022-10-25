class Settings:
    """Stores all settings for Alien Invasion"""
    def __init__(self):
        """Game Setting"""
        #Screen
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (37, 150, 190)
        #Ship setting
        self.ship_speed = 1.5