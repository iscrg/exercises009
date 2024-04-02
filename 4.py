class User:
    """
    The class is a model of user of website.
    """
    def __init__(
            self,
            id: int,
            nick_name: str,
            first_name: str,
            last_name: str = None,
            middle_name: str = None,
            gender: bool = None
    ):
        """
        :param gender: True - man, False - woman.
        """
        self.__id = id
        self.__nick_name = nick_name
        self.__first_name = first_name
        self.__last_name = last_name
        self.__middle_name = middle_name
        self.__gender = gender

    def update(self, **kwargs):
        """
        Method allows you to update user data.
        :param kwargs: id, nick_name, first_name, last_name, middle_name, gender.
        :return: None
        """
        for key, value in kwargs.items():
            if hasattr(self, "__" + key):
                setattr(self, "__" + key, value)

    def __str__(self):
        """
        :return: All user data.
        """
        return (f'id: {self.__id};\n'
                f'nick_name: {self.__nick_name};\n'
                f'first_name: {self.__first_name};\n'
                f'last_name: {self.__last_name};\n'
                f'middle_name: {self.__middle_name};\n'
                f'gender: {self.__gender};\n')


me = User(
    id=1,
    nick_name='i_scrg',
    first_name='Ivan',
)
me.update(
    last_name='Popov',
    middle_name='Sergeevich',
    gender=True
)
print(me.__str__())
