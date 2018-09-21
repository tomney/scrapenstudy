import requests
from lxml import html

from repo import write_stats_to_csv

ROOT_URL = "https://www.fantasypros.com/nfl/rankings/consensus-cheatsheets.php"


def process():
    stats = _get_stats()
    write_stats_to_csv("fantasy_rankings", stats)


def _get_stats():
    page = requests.get(ROOT_URL)
    tree = html.fromstring(page.content)
    names = tree.xpath('//div[@id="rankings-table-wrapper"]//tbody//tr//td[@class="player-label"]//span[@class="full-name"]//child::text()')
    positions = tree.xpath('//div[@id="rankings-table-wrapper"]//tbody//tr//td[4]//child::text()')
    # byes = tree.xpath('//div[@id="rankings-table-wrapper"]//tbody//tr//td[5]//child::text()')
    positions.pop(0) #first entry is a dummy
    # byes.pop(0) #first entry is a dummy
    stats = []
    for i in range(0, len(names)-1):
        stat = [names[i], positions[i]]
        stat = _format_stat(stat)
        stats.append(stat)
    return stats


def _format_stat(stat):
    formatted_stat = []
    for stat_part in stat:
        formatted_stat_part = u"".join(stat_part).encode('utf-8').strip()
        formatted_stat.append(formatted_stat_part)
    return formatted_stat


process()

