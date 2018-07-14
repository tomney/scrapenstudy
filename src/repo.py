import os
import csv


def write_stats_to_csv(active_player, formatted_per_game_stats):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = active_player + ".csv"
    file = open(os.path.join(dir_path, "storage", filename), "w+")
    writer = csv.writer(file)
    writer.writerows(formatted_per_game_stats)
    file.close()


def format_game_stats_in_unicode(per_game_stats):
    formatted_per_game_stats = []
    for game_stats in per_game_stats:
        formatted_game_stats = []
        for stat in game_stats:
            formatted_stat = u"".join(stat).encode('utf-8').strip()
            formatted_game_stats.append(formatted_stat)
        formatted_per_game_stats.append(formatted_game_stats)
    return formatted_per_game_stats
