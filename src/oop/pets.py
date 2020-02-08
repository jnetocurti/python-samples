class Pets():

    def __init__(self, *args):
        self.__pets = [a for a in args]

    def __iter__(self):
        return self.__pets.__iter__()

    def __next__(self):
        try:
            return self.__pets.pop()
        except IndexError:
            pass
