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

    def lost(self):
        """
        Method allows you to reset quantity of sheeps.
        :return: None
        """
        self.__sheeps = 0

    def get_count_sheeps(self):
        """
        :return: Quantity of sheeps.
        """
        return self.__sheeps


me = NotSleeping('Ivan')
me.add_sheep()
print(me.get_count_sheeps())
me.lost()
print(me.get_count_sheeps())
