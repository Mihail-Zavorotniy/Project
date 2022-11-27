import pygame


class Keyboard:
    def __init__(self):
        self.key_pressed = {'quit': [False, False],
                            'q': [False, False],
                            'w': [False, False],
                            'e': [False, False],
                            'a': [False, False],
                            's': [False, False],
                            'd': [False, False]
                            }

    def update(self):
        for k in self.key_pressed.keys():
            self.key_pressed[k][0] = self.key_pressed[k][1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.key_pressed['quit'][1] = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.key_pressed['q'][1] = True
                if event.key == pygame.K_w:
                    self.key_pressed['w'][1] = True
                if event.key == pygame.K_e:
                    self.key_pressed['e'][1] = True
                if event.key == pygame.K_a:
                    self.key_pressed['a'][1] = True
                if event.key == pygame.K_s:
                    self.key_pressed['s'][1] = True
                if event.key == pygame.K_d:
                    self.key_pressed['d'][1] = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    self.key_pressed['q'][1] = False
                if event.key == pygame.K_w:
                    self.key_pressed['w'][1] = False
                if event.key == pygame.K_e:
                    self.key_pressed['e'][1] = False
                if event.key == pygame.K_a:
                    self.key_pressed['a'][1] = False
                if event.key == pygame.K_s:
                    self.key_pressed['s'][1] = False
                if event.key == pygame.K_d:
                    self.key_pressed['d'][1] = False

keyboard = Keyboard()
