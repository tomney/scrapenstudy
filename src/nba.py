import re

from scrape import get_active_player_urls, get_per_game_stats
from repo import write_stats_to_csv, format_per_game_stats

ROOT_URL = "https://www.basketball-reference.com/"


def process(url=None):
    if not url:
        root_url = ROOT_URL
    active_player_urls = get_active_player_urls(root_url)
    for key in active_player_urls.keys():
        for active_player_url in active_player_urls[key]:
            active_player = re.search("/players/\w/(\w*)", active_player_url).group(1)
            per_game_stats = get_per_game_stats(key, active_player, root_url)
            if len(per_game_stats[0]) > 0:
                formatted_per_game_stats = format_per_game_stats(per_game_stats)
                write_stats_to_csv(active_player, formatted_per_game_stats)

process()
