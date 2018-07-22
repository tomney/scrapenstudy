import os
import csv


PLAYER_ABSENCE_TYPES = [
    "Did Not Play",
    "Inactive",
    "Not With Team",
    "Player Suspended",
    "Did Not Dress"
]


def write_stats_to_csv(active_player, formatted_per_game_stats):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = active_player + ".csv"
    file = open(os.path.join(dir_path, "storage", filename), "w+")
    writer = csv.writer(file)
    writer.writerows(formatted_per_game_stats)
    file.close()


def format_per_game_stats(per_game_stats):
    formatted_per_game_stats = []
    for game_stats in per_game_stats:
        if is_header(game_stats):
            continue
        formatted_game_stats = format_game_stats(game_stats)
        formatted_per_game_stats.append(formatted_game_stats)
    return formatted_per_game_stats


def is_header(game_stats):
    first_entry = game_stats[0]
    try:
        int(first_entry)
    except ValueError:
        return True
    return False


def format_game_stats(game_stats):
    formatted_game_stats = []
    for game_stat in game_stats:
        formatted_game_stat = format_game_stat(game_stat)
        # formatted_game_stat is formatted as a list to deal with player absences
        formatted_game_stats.extend(formatted_game_stat)
    return formatted_game_stats


def format_game_stat(game_stat):
    formatted_stat = u"".join(game_stat).encode('utf-8').strip()
    if formatted_stat in PLAYER_ABSENCE_TYPES:
        formatted_stats = handle_player_absence()
        return formatted_stats
    return [formatted_stat]


def handle_player_absence():
    """return list of empty strings for stats in a game where a player was absent"""
    return [u"" for _ in range(0, 21)]


def get_player_per_game_stats(player_id):
    filename = player_id + ".csv"
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), "storage", filename)
