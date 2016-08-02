import Config.websites_config as cfg
from Networking import Http
from HTMLUtil import LinkExtractor, Identifiers
from CommonUtil import StringUtil


def crawl_linear(search_string=None):

    website_stream = ""
    website_links = []
    website_page_links = []
    search_results = []

    crawl_sites = cfg.websites

    for website in crawl_sites:

        print("Accessing website : " + website + " for links")
        print("")
        website_stream = Http.make_request(website)

        if website_stream is not None:
            website_links = LinkExtractor.extract_anchor_links(website_stream)

            for link in website_links:
                website_page_links.append(LinkExtractor.extract_attribute(link, 'href'))

                filtered_website_links = StringUtil.filter_links(website_page_links)

            for link in filtered_website_links:

                if Identifiers.is_internal_route(link):
                    route = website + link

                    print("Accessing sub route : " + route)
                    print("")
                    route_stream = Http.make_request(route)

                    if search_string is not None:

                        if search_string in str(route_stream):

                            print(" '" + search_string + "' found in " + route)
                            print("")
                            search_results.append(route)


