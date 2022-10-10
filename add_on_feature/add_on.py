import re
from webscaping_file.url_individual import get_all_urls
from phonenumber.main_phonenumber_file import get_ow_number
import asyncio
from numba import njit
from name.api_name import Payload


class Add_on(Payload):

    def post(self):
        try:
            url_list = []
            store_ow_number = []
            for i in [i for i in
                      [None if re.findall(r"facebook|instagram", i) else i for i in get_all_urls(self.data.get("url"))]
                      if i is not None]:
                store_number = asyncio.run(get_ow_number(i))
                url_list.append(i)
                store_ow_number.append(store_number)
            res = {}
            for key in url_list:
                for value in store_ow_number:
                    if len(value) == 0:
                        pass
                    else:
                        res[key] = value[0]
                        store_ow_number.remove(value)
            return dict(url_with_numbers=res)
        except Exception as e:
            return f"Url with number has an issue {e}"


url_with_number_njit = njit()(Add_on.post)
