class NotSleeping:
    """
    The class is a model of a human, who falling asleep.
    """
    def __init__(self, name):
        self.name = name
        self.__sheeps = 0

    def add_sheep(self):
        """
        Method allows you to add one sheep.
        :return: None.
        """
        self.__sheeps += 1


me = NotSleeping('Ivan')
me.add_sheep()
