from lxml import html
import requests
import csv


def get_number_of_result_pages():
    return 4

def get_page_of_running_backs(page_number):
    page = "http://www.nfl.com/players/search?category=position&playerType=current&conference=ALL&d-447263-p={}&filter=runningback".format(page_number)
    return page


def get_running_back_urls(page):
    page = requests.get(page)
    tree = html.fromstring(page.content)
    running_backs = tree.xpath('//div[@id="searchResultsLargeTable"]/div[@id="searchResults"]//table[@class="data-table1"]/tbody//tr/td[3]//a/@href')
    return running_backs

def write_list_to_csv(filename, list):
    file = open(filename, "w+")
    writer = csv.writer(file)
    writer.writerow(list)
    file.close()

def process():
    number_of_pages = get_number_of_result_pages()
    running_back_urls = []
    for page_number in range(1,number_of_pages+1):
        page = get_page_of_running_backs(page_number)
        running_back_urls += get_running_back_urls(page)
    write_list_to_csv("running_backs.csv", running_back_urls)

process()