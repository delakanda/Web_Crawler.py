import Config.websites_config as cfg
from Networking import Http
from HTMLUtil import LinkExtractor, Identifiers
from CommonUtil import StringUtil
from termcolor import colored, cprint
from CommonUtil import StringUtil


def crawl(search_string=None, argv_website=None):
    root_website = None
    website_dictionary = {}
    link_visit_tracker = []
    search_results = []

    if argv_website is not None:
        websites_to_iterate = argv_website
    else:
        websites_to_iterate = cfg.websites

    for website in websites_to_iterate:
        root_website = website

        cprint("Getting initial website links ... ", "blue")
        print("")

        filtered_website_links = LinkExtractor.get_links(root_website, root_website)

        cprint("Building website link structure ... ", "blue")
        print("")

        for indx, link in enumerate(filtered_website_links):
            website_dictionary[indx] = {
                'main_link': link,
                'sub_links': LinkExtractor.get_links(link,root_website)
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

        print("")
        cprint("Back from the deep hollow of the internet", "green")
        print("")

        if search_string is not None:
            if len(search_results) > 0:
                print("")
                print("Search results for : " + search_string)
                print("Result found at the following links: ")

                for link in search_results:
                    print(link)
            else:
                print("")
                print("No search results for " + search_string)


