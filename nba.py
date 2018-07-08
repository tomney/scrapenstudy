from lxml import html
import requests
import re
import csv

ROOT_URL = "https://www.basketball-reference.com/"
SEASON = ""


def get_active_player_urls():
    all_player_urls = {}
    # for letter in string.ascii_lowercase:
    for letter in ['a']:
        url = ROOT_URL + 'players/' + letter
        page = requests.get(url)
        tree = html.fromstring(page.content)
        player_urls = tree.xpath('//table[@id="players"]/tbody//tr/th/strong/a/@href')
        all_player_urls[letter] = player_urls
    return all_player_urls


def get_per_game_stats(key, active_player):
    url = ROOT_URL + 'players/' + key + "/" + active_player + "/gamelog/2018/"
    page = requests.get(url)
    tree = html.fromstring(page.content)
    stat_field_elements = tree.xpath('//div[@id="all_pgl_basic"]//descendant::thead[1]//th')
    print("Parsing stat field list")
    stat_fields = [stat_field_element.text.encode('ascii', 'replace') for stat_field_element in stat_field_elements]
    no_of_games = len(tree.xpath('//div[@id="all_pgl_basic"]//tbody//tr'))
    all_game_stats = []
    all_game_stats.append(stat_fields)
    for game_no in range(1, no_of_games):
        print("Parsing game stats")
        game_stats = tree.xpath('//div[@id="all_pgl_basic"]//tbody//descendant::tr[' + str(game_no) + ']//child::text()')
        all_game_stats.append(game_stats)
    return all_game_stats


def write_stats_to_csv(active_player, formatted_per_game_stats):
    filename = active_player + ".csv"
    file = open(filename, "w+")
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


def process():
    active_player_urls = get_active_player_urls()
    for key in active_player_urls.keys():
        for active_player_url in active_player_urls[key]:
            active_player = re.search("/players/\w/(\w*)", active_player_url).group(1)
            per_game_stats = get_per_game_stats(key, active_player)
            formatted_per_game_stats = format_game_stats_in_unicode(per_game_stats)
            write_stats_to_csv(active_player, formatted_per_game_stats)

process()