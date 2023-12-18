from re import sub


def title_to_slug(string):
    return sub(r"[-]+", "-", sub(r"[^a-z0-9|-]", "", string.lower().replace(" ", "-")))