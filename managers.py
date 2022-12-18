from copy import copy


class BackgroundManager:

    '''класс BackgroungManager
    backgrounds - список всех бэкграундов в игре
    current_bg - бэкграунд локации, в которой надожится персонаж
    '''
    def __init__(self, backgrounds, current_bg_number):
        '''Конструктор'''
        self.backgrounds = backgrounds
        self.current_bg = backgrounds[current_bg_number]

    def update(self, new_bg_number):
        '''Изменение бэкграунда'''
        self.current_bg = self.backgrounds[new_bg_number]

    def draw_scenery(self, player):
        '''Отрисовка бэкграунда и объектов в комнате'''
        self.current_bg.draw()
        objects_to_draw = copy(self.current_bg.all_objects)
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
