import requests
from lxml import html

SEASON = ""


def get_active_player_urls(root_url):
    all_player_urls = {}
    # for letter in string.ascii_lowercase:
    for letter in ['a']:
        url = root_url + 'players/' + letter
        page = requests.get(url)
        tree = html.fromstring(page.content)
        player_urls = tree.xpath('//table[@id="players"]/tbody//tr/th/strong/a/@href')
        all_player_urls[letter] = player_urls
    return all_player_urls


def get_per_game_stats(key, active_player, root_url):
    url = root_url + 'players/' + key + "/" + active_player + "/gamelog/2018/"
    page = requests.get(url)
    tree = html.fromstring(page.content)
    stat_field_elements = tree.xpath('//div[@id="all_pgl_basic"]//descendant::thead[1]//th')
    stat_fields = [stat_field_element.text.encode('ascii', 'replace') for stat_field_element in stat_field_elements]
    no_of_games = len(tree.xpath('//div[@id="all_pgl_basic"]//tbody//tr'))
    all_game_stats = []
    all_game_stats.append(stat_fields)
    for game_no in range(1, no_of_games):
        game_stats = tree.xpath('//div[@id="all_pgl_basic"]//tbody//descendant::tr[' + str(game_no) + ']//child::text()')
        all_game_stats.append(game_stats)
    return all_game_stats
