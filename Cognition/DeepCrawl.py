import Config.websites_config as cfg
from Networking import Http
from HTMLUtil import LinkExtractor, Identifiers
from CommonUtil import StringUtil
from termcolor import colored, cprint
from CommonUtil import StringUtil


def crawl(search_string=None):
    root_website = None
    website_dictionary = {}
    link_visit_tracker = []
    search_results = []

    for website in cfg.websites:
        root_website = website

        cprint("Getting initial website links ... ", "blue")
        print("")

        filtered_website_links = get_links(root_website,root_website)

        cprint("Building website link structure ... ", "blue")
        print("")

        for indx, link in enumerate(filtered_website_links):
            website_dictionary[indx] = {
                'main_link': link,
                'sub_links': get_links(link,root_website)
            }

        cprint("Link structure built", "blue")
        print("")

        for root_link in website_dictionary:

            print("")
            cprint("Structure Iteration Commencing...", "blue")
            print("")

            cprint("Accessing Struct for : " + website_dictionary[root_link]['main_link'], "magenta")
            print("")

            for sub_link in website_dictionary[root_link]['sub_links']:

                if sub_link not in link_visit_tracker:

                    cprint("Accessing link : " + sub_link + " ...", "blue")
                    print("")
                    sub_link_stream = Http.make_request(sub_link)

                    if search_string is not None:

                        if search_string in str(sub_link_stream):
                            cprint(" '" + search_string + "' found in " + sub_link, "green")
                            print("")
                            search_results.append(sub_link)

                    link_visit_tracker.append(sub_link)


def get_links(website, root_website):
    global filtered_links
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

            return_links.append(route)

    return return_links