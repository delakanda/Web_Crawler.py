from bs4 import BeautifulSoup
from HTMLUtil import LinkExtractor, Identifiers
from CommonUtil import StringUtil
from Networking import Http

def extract_anchor_links(html_stream):

    anchor_links = []

    soup = BeautifulSoup(html_stream, 'html.parser')

    anchor_links = soup.find_all('a')

    return anchor_links


def extract_attribute(link, attribute):
    return link.get(attribute)


def get_links(website, root_website):

    website_page_links = [];
    website_stream = Http.make_request(website)
    return_links = []

    if website_stream is not None:
        website_links = LinkExtractor.extract_anchor_links(website_stream)

        for link in website_links:
            website_page_links.append(LinkExtractor.extract_attribute(link, 'href'))

        filtered_links = StringUtil.filter_links(website_page_links)

        for link in filtered_links:

            if Identifiers.is_internal_route(link):
                route = root_website + link

            elif Identifiers.is_external_route(link):
                route = link

                if "http" not in route:
                    route = "http:" + route

            return_links.append(route)

    return return_links