class Game:
    def __init__(self, teams: dict):
        self.__score = {
            teams['command1']: 0,
            teams['command2']: 0
        }

    def ball_thrown(self, command: str, points: int):
        """
        Method add score to current command.
        :param command: Current command.
        :param points: Count of point.
        :return: None
        """
        self.__score[command] += points

    def get_score(self):
        """
        :return: Score.
        """
        return self.__score

    def get_winner(self):
        """
        :return: Return command with the most large score. If scores are equal, return "Draw!"
        """
        comm = list(self.__score.items())
        if comm[0][1] == comm[1][1]:
            return 'Draw!'
        winner = sorted(self.__score.items(), key=lambda x: x[1], reverse=True)
        return winner[0][0]


teams = {
    'command1': 'biba',
    'command2': 'boba'
}

basketball = Game(teams)
basketball.ball_thrown('biba', 10)
print(basketball.get_score())
print(basketball.get_winner())
