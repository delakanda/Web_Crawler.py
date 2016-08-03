

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

        if link is not None:

            if len(link) == 1 and '/' == link:
                continue

            for filter_symbol in filter_symbols:
                if filter_symbol not in link:
                    filtered_links.append(link.replace(" ", ""))

    return remove_duplicates(filtered_links)


def remove_duplicates(l):
    return list(set(l))


def get_argument_value(raw_arg):
    split_val = raw_arg.split("=")

    if len(split_val) > 1:
        return split_val[1]
    else:
        return None