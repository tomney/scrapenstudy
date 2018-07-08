from lxml import html
import requests

page = requests.get('http://www.sports-reference.com/cbb/boxscores/index.cgi?month=3&day=11&year=2017')
tree = html.fromstring(page.content)
# match_summary = tree.xpath('//div[@class="game_summary nohover"]/node()')
winners = tree.xpath('//div[@class="game_summary nohover"]//table[@class="teams"]//tbody//tr[@class="winner"]//td[not(@class)]//a[@*]/text()')
losers = tree.xpath('//div[@class="game_summary nohover"]//table[@class="teams"]//tbody//tr[@class="loser"]//td[not(@class)]//a[@*]/text()')
winning_score = tree.xpath('//div[@class="game_summary nohover"]//table[@class="teams"]//tbody//tr[@class="winner"]//td[@class="right"]/text()')
losing_score = tree.xpath('//div[@class="game_summary nohover"]//table[@class="teams"]//tbody//tr[@class="loser"]//td[@class="right"]/text()')
print winners