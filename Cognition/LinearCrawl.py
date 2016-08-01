import Config.websites_config as cfg
from Networking import Http
from HTMLUtil import LinkExtractor, Identifiers
from CommonUtil import StringUtil

def crawl_linear():

    website_stream = ""
    website_links = []
    website_page_links = []

    crawlSites = cfg.websites

    for website in cfg.websites:

        website_stream = Http.make_request(website)

        if website_stream is not None:
            website_links = LinkExtractor.extract_anchor_links(website_stream)

            for link in website_links:
                website_page_links.append(LinkExtractor.extract_attribute(link, 'href'))

                filtered_website_links = StringUtil.filter_links(website_page_links)

            for link in filtered_website_links:

                if Identifiers.is_internal_route(link):
                    route = website + link
                    print(route)
            # # print("Accessing " + website + StringUtil.filter_web_address(page))

