from bs4 import BeautifulSoup


def extract_anchor_links(html_stream):

    anchor_links = []

    soup = BeautifulSoup(html_stream, 'html.parser')

    anchor_links = soup.find_all('a')

    return anchor_links


def extract_attribute(link, attribute):
    return link.get(attribute)
