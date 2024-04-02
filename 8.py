class MorseMsg:
    def __init__(self):
        self.__ru = {
            '.-': 'А',
            '-...': 'Б',
            '.--': 'В',
            '--.': 'Г',
            '-..': 'Д',
            '.': 'Е',
            '...-': 'Ж',
            '--..': 'З',
            '..': 'И',
            '.---': 'Й',
            '-.-': 'К',
            '.-..': 'Л',
            '--': 'М',
            '-.': 'Н',
            '---': 'О',
            '.--.': 'П',
            '.-.': 'Р',
            '...': 'С',
            '-': 'Т',
            '..-': 'У',
            '..-.': 'Ф',
            '....': 'Х',
            '-.-.': 'Ц',
            '---.': 'Ч',
            '----': 'Ш',
            '--.-': 'Щ',
            '.--.-.': 'Ъ',
            '-.--': 'Ы',
            '-..-': 'Ь',
            '...-...': 'Э',
            '..--': 'Ю',
            '.-.-': 'Я'
        }

        self.__en = {
            '.-': 'A',
            '-...': 'B',
            '-.-.': 'C',
            '-..': 'D',
            '.': 'E',
            '..-.': 'F',
            '--.': 'G',
            '....': 'H',
            '..': 'I',
            '.---': 'J',
            '-.-': 'K',
            '.-..': 'L',
            '--': 'M',
            '-.': 'N',
            '---': 'O',
            '.--.': 'P',
            '--.-': 'Q',
            '.-.': 'R',
            '...': 'S',
            '-': 'T',
            '..-': 'U',
            '...-': 'V',
            '.--': 'W',
            '-..-': 'X',
            '-.--': 'Y',
            '--..': 'Z'
        }

        self.__ru_vowels = ['А', 'Е', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']
        self.__ru_consonants = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К',
                              'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф',
                              'Х', 'Ц', 'Ч', 'Ш', 'Щ']

        self.__en_vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
        self.__en_consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J',
                               'K', 'L', 'M', 'N', 'P', 'Q', 'R',
                               'S', 'T', 'V', 'W', 'X', 'Z']

    def eng_decode(self, text: str):
        """
        Decodes from Morse code into English.
        :param text: Morse text.
        :return: English text.
        """
        text = text.split(' ')
        res = []
        for word in text:
            res.append(self.__en[word])
        return res

    def rus_decode(self, text: str):
        """
        Decodes from Morse code into English.
        :param text: Morse text.
        :return: Russian text.
        """
        text = text.split(' ')
        res = []
        for word in text:
            res.append(self.__ru[word])
        return res

    def get_vowels(self, lang: str):
        """
        :param lang: 'ru' or 'en'
        :return: Vowels
        """
        if lang == 'en':
            return self.__en_vowels
        if lang == 'ru':
            return self.__ru_vowels

    def get_consonants(self, lang: str):
        """
        :param lang: 'en' or 'ru'
        :return: Consonants
        """
        if lang == 'en':
            return self.__en_consonants
        if lang == 'ru':
            return self.__ru_consonants


mrs = MorseMsg()
print(mrs.eng_decode('.- -... -.-.'))
print(mrs.rus_decode('.- -... -.-.'))
print(mrs.get_vowels('ru'))
print(mrs.get_consonants('en'))
