# import sklearn
import pandas

from repo import get_player_per_game_stats


def process():
    pandas.read_csv(get_player_per_game_stats("abrinal01"))
    print "good boy greg"

process()