class Transport:
    def __init__(self, name, type):
        self.name = name
        self.type = type


class Train(Transport):
    def __init__(self, name='Train', type='bullet train'):
        super().__init__(name, type)

    def __str__(self):
        return 'name = {}, type = {}'.format(self.name, self.type)


class Plane(Transport):
    def __init__(self, name='Plane', type='Boing747'):
        super().__init__(name, type)

    def __str__(self):
        return 'name = {}, type = {}'.format(self.name, self.type)


train = Train()
print(train)


plane = Plane()
print(plane)

