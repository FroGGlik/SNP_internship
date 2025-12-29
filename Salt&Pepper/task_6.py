class WrongNumberOfPlayersError(Exception):
    'Исключение, возникающее при неправильном количестве игроков'
    pass


class NoSuchStrategyError(Exception):
    'Исключение, возникающее при неправильном ходе игрока(-ов)'
    pass


class Psr():
    players = []

    def __init__(self, name):
        self.name = name
        self.player = []

        Psr.players.append(self)

    def add_player(self, len_player):
        if not Psr.is_valid_len_player():
            raise ValueError('Lenght list of player not valid')
        else:
            self.players.append(len_player)

    @staticmethod
    def is_valid_len_player(len_player):
        return len(len_player) == 2
    
    @staticmethod
    def is_valid_move_player(move):
        return move in 'PSRpsr'
    
    @classmethod
    def rps_game_winner(cls, players):
        if len(players) != 2:
            raise WrongNumberOfPlayersError('Lenght list of players should be 2')

        player1, player2 = players
        name1, move1 = player1
        name2, move2 = player2

        if not cls.is_valid_move_player(move1):
            raise NoSuchStrategyError('Move not valid')
        if not cls.is_valid_move_player(move2):
            raise NoSuchStrategyError('Move not valid')
        
        if move1 == move2:
            return 'Draw'
        
        elif ((move1 == 'P' or move1 == 'p') and (move2 == 'R' or move2 == 'r')) or ((move1 == 'S' or move1 == 's') and (move2 == 'P' or move2 == 'p')) or ((move1 == 'R' or move1 == 'r') and (move2 == 'S' or move2 == 's')):
            return f'{name1} {move1}'
        
        else:
            return f'{name2} {move2}'

try:
    print(Psr.rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
except WrongNumberOfPlayersError:
    print('Могут быть только два участника')

try:
    print(Psr.rps_game_winner([['player1', 'P'], ['player2', 'A']]))
except NoSuchStrategyError:
    print('Из возможных команд, доступны только PSR')

print(Psr.rps_game_winner([['player1', 'P'], ['player2', 'S']]))
print(Psr.rps_game_winner([['player1', 'p'], ['player2', 'r']]))
print(Psr.rps_game_winner([['player1', 'P'], ['player2', 'P']]))