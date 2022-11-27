from copy import copy


class BackgroundManager:
    def __init__(self, backgrounds):
        self.backgrounds = backgrounds

    def update(self, bg_number, new_bg):
        self.backgrounds[bg_number] = new_bg

    def draw_scenery(self, bg_number, player):
        self.backgrounds[bg_number].draw()
        objects_to_draw = copy(self.backgrounds[bg_number].objects)
        player_drawn = False
        for obj in objects_to_draw:
            if obj.y + obj.sprite.get_height() < player.hitbox_y + player.hitbox_height/2 or player_drawn:
                obj.draw()
            else:
                player.draw()
                obj.draw()
                player_drawn = True
        if not player_drawn:
            player.draw()
