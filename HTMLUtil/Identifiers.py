

def is_internal_route(link):

    if "http://" in link or "https://" in link:
        return False
    else:
        return True


def is_external_route(link):

    if "http://" in link or "https://" in link:
        return True
    else:
        return False
