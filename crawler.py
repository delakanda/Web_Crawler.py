#!/usr/bin/python3.5

from Cognition import DeepCrawl
from CommonUtil import StringUtil
from termcolor import colored, cprint
import sys

website = []
search_string = None

if len(sys.argv) > 1:

    if any("--website" in arg for arg in sys.argv) or any("--search" in arg for arg in sys.argv):

        for indx, val in enumerate(sys.argv):

            # skip the script name
            if indx == 0:
                continue

            if '--website' in val:
                website.append(StringUtil.get_argument_value(val))
            else:
                website = None

            if '--search' in val:
                search_string = StringUtil.get_argument_value(val)
            else:
                search_string = None

        DeepCrawl.crawl(search_string,website)

    else:
        cprint("Argument error", "red")
        cprint("Specify website as : --website=[website] and/or search word as --search=[search_word]")

# else:
    # DeepCrawl.crawl()
