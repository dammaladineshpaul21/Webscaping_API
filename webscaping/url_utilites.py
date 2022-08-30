import numpy as np
from webscaping.urls import URLs_info

urls_object = URLs_info("../resources_file/poi1_details.json")


def scape_url():
    get_urls1 = urls_object.get_date_file_values()
    store_modified_urls = []
    for i in urls_object.get_all_urls():
        if i.startswith("/"):
            get_full_url = str(get_urls1)+str(i[1::])
            store_modified_urls.append(get_full_url)
        else:
            pass
    return store_modified_urls

