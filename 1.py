class Dog:
    """
    The class is a dog model.
    """
    def __init__(self, name, breed=None):
        self.name = name
        self.breed = breed

    def say(self):
        """
        Method allows to say 'Гав!'.
        :return: None
        """
        print('Гав!')


my_dog = Dog('Арнольд')
my_dog.say()
