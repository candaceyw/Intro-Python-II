class Item:
    def __init__(self, name, description, ):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}, {self.description}'

    def pickup(self, ):
        print('You picked up {self.name}')

    def drop(self, ):
        print('You dropped up {self.name}')


class RandomItem(Item):
    pass
