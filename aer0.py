class Transport:
    def __init__(self, name, transport_type, model, transport_speed):
        self.name = name
        self.transport_type = transport_type
        self.model = model
        self.transport_speed = transport_speed

    def speed(self, speed):
        self.transport_speed += speed
        return self.transport_speed


class Train(Transport):
    def __init__(self, name='Train', transport_type='bullet train', model='b467', transport_speed=80,
                 number_of_cars=10):
        super().__init__(name, transport_type, model, transport_speed)
        self.number_of_cars = number_of_cars

    def __str__(self):
        return 'name = {}, transport type = {}, mode = {}, transpor tspeed = {}, number of cars = {}' \
            .format(self.name, self.transport_type, self.model, self.transport_speed, self.number_of_cars)

    def change_of_number(self, amount):
        self.number_of_cars += amount
        return self.number_of_cars


class Plane(Transport):
    def __init__(self, name='Plane', transport_type='Passanger', model='747', transport_speed=360, flaps='close'):
        super().__init__(name, transport_type, model, transport_speed)
        self.flaps = flaps

    def __str__(self):
        return 'name = {}, transport type = {}, model = {}, transport speed = {}, flaps = {}' \
            .format(self.name, self.transport_type, self.model, self.transport_speed, self.flaps)


    def aircraft_flaps_position(self):
        if self.flaps == 'close':
            return 'flaps close'
        elif self.flaps == 'open':
            return 'flaps open'



train = Train()
print(train)
train.change_of_number(amount=-2)
print(train)

train.speed(20)
print(train)

plane = Plane()
print(plane)
plane.flaps = 'close'
print(plane.aircraft_flaps_position())