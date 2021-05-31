class Player:
    def __init__(self, x=0, y=0, w=60, h=71, speed=5, name='player'):
        self.name = name

        self.speed = speed

        self.x = 0
        self.y = 0

        self.center_x = x + (w // 2)
        self.center_y = y + (h // 2)

        self.w = w
        self.h = h

        self.pos_left = False
        self.pos_right = False

        self.is_dead = True

    def refresh_center_pos(self):
        self.center_x = self.x + (self.w // 2)
        self.center_y = self.y + (self.h // 2)
