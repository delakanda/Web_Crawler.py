import Config.websites_config as cfg
from Networking import Http
from HTMLUtil import LinkExtractor, Identifiers
from CommonUtil import StringUtil
from termcolor import colored, cprint


def crawl_linear(search_string=None):

    website_stream = ""
    website_links = []
    website_page_links = []
    search_results = []

    crawl_sites = cfg.websites

    for website in crawl_sites:

        cprint("Accessing website : " + website + " for links ...", "blue")
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
                    cprint("Accessing sub route : " + route, "blue")
                    print("")

                elif Identifiers.is_external_route(link):
                    route = link
                    cprint("Accessing route : " + route, "blue")
                    print("")

                route_stream = Http.make_request(route)

                if search_string is not None:

                    if search_string in str(route_stream):
                        cprint(" '" + search_string + "' found in " + route, "green")
                        print("")
                        search_results.append(route)


