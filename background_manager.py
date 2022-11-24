class BackgroundManager:
    def __init__(self, backgrounds):
        self.backgrounds = backgrounds

    def update(self, bg_number, new_bg):
        self.backgrounds[bg_number] = new_bg
