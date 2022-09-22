import json
import pandas as pd
from webscaping_file.url_individual import *


async def error_check(all_urls):
    """Will Execute all the text retived from the ULR"""
    try:
        soup = BeautifulSoup(requests.get(all_urls).text, 'html.parser')
        store_number_info = []
        get_num = re.findall(r"[A-Za-z\w'a-z-&A-Z'a-z]+", str(soup).strip())
        store_number_info.append(get_num)
        comdine_text_value = [j for i in store_number_info for j in i]
        await asyncio.sleep(0.0)
        return comdine_text_value
    except Exception as e:
        return f"URL Connection Error {e}"


async def mixed_name(name, all_text):
    try:
        get_correct_name = []
        for i in range(len(name)):
            if re.findall(str(name[i]).replace(" ", "").lower(), " ".join(all_text)):
                get_correct_name.append(name[i])
            else:
                pass
        await asyncio.sleep(0.0)
        return get_correct_name
    except Exception:
        return dict(error_massage=ValueError)


async def check_spacial_case(name, file_pass):
    try:
        with open(file_pass) as file:
            get_data = json.load(file)
            create_df = pd.DataFrame(get_data, columns=["character", "letter_convertion"])
            make_table = create_df.set_index("character").to_dict()
            get_sp_char = [i for i, k in make_table["letter_convertion"].items()]
            if "&" not in name:
                for val in name.split():
                    get_val = [i for i in [None if re.findall(r"[A-Za-z]", i) else i for i in val] if
                               i is not None]
                    get_final_Re = [i for i in list(itertools.chain(*[list(map(lambda x: x if get_val[i] in x else None,
                                                                               get_sp_char)) for i in
                                                                      range(len(get_val))]))
                                    if i is not None]
                    for i in range(len(get_final_Re)):
                        name = name.replace(name[name.index(get_val[i])],
                                            make_table["letter_convertion"][get_final_Re[i]])
                await asyncio.sleep(0.0)
                return name
            elif "’" in name:
                name = name.replace(name[name.index("’")], make_table["letter_convertion"]["’"])
                await asyncio.sleep(0.0)
                return name
            else:
                name = name.replace(name[name.index("&")], make_table["letter_convertion"]["&"])
                await asyncio.sleep(0.0)
                return name
    except Exception:
        return ValueError


async def site_varification(get_text):
    error_massage = ["HTTP Error 503", "404 forbidden", "404 Not Found", "Error 404 - Page Not Found",
                     "Domain for Sale", "Mod_Security"
                                        "404 Error Pages", "errorCode 1020", "403 Forbidden",
                     "Error Page cannot be displayed", "Domain Not Claimed", "This domain is for sale"]
    try:
        get_result = [i for i in list(map(lambda x: x if re.findall(x, get_text) else None, error_massage)) if
                      i is not None]
        await asyncio.sleep(0.0)
        return get_result
    except Exception:
        return ValueError


def get_all_val(incorrect_val, top_name_incorrect, match, no_match,
                error_code):
    try:
        return dict(Incorrect_val=incorrect_val, top_name_incorrect=top_name_incorrect,
                    match=match, no_match=no_match, error_code=error_code)
    except Exception:
        return AttributeError


def extract_the_copyrights(url):
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    get_name = []
    for tag in soup.findAll(text=re.compile(r'©|copy;')):
        copyrighttexts = tag.parent.text
        get_name.append(copyrighttexts)
    get_name.append(soup.title.string)
    return [get_name[0].strip()]
