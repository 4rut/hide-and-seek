class Player:
    def __init__(self, x=50, y=50, w=60, h=71, speed=5):
        # Скорость
        self.speed = speed
        # Координаты
        self.x = x
        self.y = y
        # Размеры
        self.w = w
        self.h = h
        # В какую сторону смотрит
        self.pos_left = False
        self.pos_right = False
