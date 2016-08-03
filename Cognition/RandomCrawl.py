import Config.websites_config as cfg
from Networking import Http
from HTMLUtil import LinkExtractor, Identifiers
from CommonUtil import StringUtil
from termcolor import colored, cprint
from CommonUtil import StringUtil
from Cognition import DeepCrawl
import random


def crawl(search_string=None, argv_website=None):

    if argv_website is None:
        starting_website = cfg.websites[0]
    else:
        starting_website = argv_website[0]

    search_results = []

    print("")
    cprint("Getting links on "+starting_website+"...", "blue")
    print("")

    filtered_website_links = LinkExtractor.get_links(starting_website, starting_website)

    print("")
    cprint("Done", "blue")
    print("")

    while True:

        print("")
        cprint("Getting Random Link...", "blue")
        print("")

        if len(filtered_website_links) > 0:

            next_link = random.choice(filtered_website_links)

            cprint("Selected : "+next_link, "blue")
            cprint("Accessing...", "blue")
            print("")

            random_link_stream = Http.make_request(next_link)

            if search_string is not None:

                if search_string in str(random_link_stream):
                    cprint(" '" + search_string + "' found in " + next_link, "green")
                    print("")
                    search_results.append(next_link)

        else:

            print("")
            cprint("Re-selecting Random... ", "magenta")
            print("")

            re_link = LinkExtractor.get_links(starting_website, starting_website)
            next_link = random.choice(re_link)

        filtered_website_links = LinkExtractor.get_links(next_link, starting_website)