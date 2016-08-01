import httplib2
from CommonUtil import StringUtil


def make_request(website_address):

    website_address = StringUtil.filter_web_address(website_address)

    http = httplib2.Http()

    try:
        status, response = http.request(website_address)

        return response
    except:
        print("Error accessing site : " + website_address)
        return None