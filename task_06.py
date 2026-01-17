class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(players):
    if len(players) != 2:
        raise WrongNumberOfPlayersError('There must be exactly two players')
    
    name1, move1 = players[0]
    name2, move2 = players[1]
    
    move1 = move1.upper()
    move2 = move2.upper()
    
    valid_moves = 'PSR'
    
    if move1 not in valid_moves:
        raise NoSuchStrategyError('Invalid move for player 1')
    if move2 not in valid_moves:
        raise NoSuchStrategyError('Invalid move for player 2')
    
    if move1 == move2:
        return players[0]

    elif (move1 == 'P' and move2 == 'R') or \
         (move1 == 'R' and move2 == 'S') or \
         (move1 == 'S' and move2 == 'P'):
        return players[0]
    else:
        return players[1]
    
try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
except WrongNumberOfPlayersError as ex:
    print('WrongNumberOfPlayersError')
try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))
except NoSuchStrategyError as ex:
    print('NoSuchStrategyError')
print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))