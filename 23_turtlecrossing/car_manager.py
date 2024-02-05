from car import Car


class CarManager:
    def __init__(self):
        self.car_list = []

    def spawn_car(self):
        new_car = Car()
        self.car_list.append(new_car)

    def move_cars(self):
        for item in self.car_list:
            item.move()

    def detect_collision(self, player):
        for item in self.car_list:
            if item.detect_collision(player):
                return True
        return False

