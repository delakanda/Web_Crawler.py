import httplib2
from CommonUtil import StringUtil
from termcolor import colored, cprint


def make_request(website_address):

    website_address = StringUtil.filter_web_address(website_address)

    http = httplib2.Http()

    try:
        status, response = http.request(website_address)

        return response
    except:
        cprint("Error accessing site : " + website_address,'red')
        print("")
        return None