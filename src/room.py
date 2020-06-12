# Implement a class to hold room information. This should have name and
# description attributes.


class Room:

    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        if items is None:
            self.items = []
        else:
            self.items = items

    def __str__(self):
        return f'{self.name}'

    def print_description(self):
        return f'{self.description}'

    def add_item(self, items):
        self.items.append(items)

    def remove_item(self, item):
        self.items.pop(item)
    #
    # def print_items(self):
    #     index = 1
    #     if len(self.items) > 0:
    #         print(self.name)
    #     for item in self.items:
    #         print(f'\t {index}. {item}')
    #         index += 1
    #     print('\n')
