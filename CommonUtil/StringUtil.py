

def filter_web_address(web_address):

    if 'http' not in web_address:
        website_address = "http://" + web_address
    else:
        website_address = web_address

    return website_address


def filter_links(links):

    filter_symbols = ['#']
    filtered_links = []

    for link in links:

        if len(link) == 1 and '/' == link:
            continue

        for filter_symbol in filter_symbols:
            if filter_symbol not in link:
                filtered_links.append(link.replace(" ", ""))

    return remove_duplicates(filtered_links)


def remove_duplicates(l):
    return list(set(l))
