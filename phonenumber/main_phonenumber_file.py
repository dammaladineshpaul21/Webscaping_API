import asyncio

from webscaping.url_individual import *


# async def phone_number_string(url):
#     """Get the URL from the payload and extracts are the number
#     and make's it into a string."""
#     try:
#         async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=6)) as session:
#             async with session.get(url, ssl=True) as requs:
#                 soup = BeautifulSoup(await requs.text(), 'html.parser' or 'lxml')
#             await session.close()
#             number_extraction = [i for i in
#                                  list(map(lambda x: x if len(x) > 1 else None, re.findall(r"[0-9]+", str(soup).replace(" ", "")))) \
#                                  if i is not None]
#             # number_extraction2 = re.findall(r"\(\d{3}\)|\d{3}-\d{4}|\d{3} \d{4}|\d{3}-\d{3}-\d{4}|\d{3}\W\d{4}",
#             #                                 str(soup))
#             await asyncio.sleep(0.05)
#             return number_extraction
#     except Exception as e:
#         await asyncio.sleep(0.5)
#         return e
#

async def get_ow_number(url):
    try:
        """All the Required Pattern related to Phone_number based on the url provided
        and check the pattern associated with it."""
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=6)) as session:
            async with session.get(url, ssl=True) as requs:
                soup = BeautifulSoup(await requs.text(), 'html.parser')
            await session.close()
            numbersextraction = re.findall(r"\(\d{3}\)|\d{3}-\d{4}|\d{3} \d{4}|\d{3}-\d{3}-\d{4}|\d{3}\W\d{4}"
                                           r"\W\d{11}|\d{3}\W\d{3}\W\d{4}",
                                           str(soup))
            numbersextraction2 = re.findall(r"\(\d{3}\)|\d{3}-\d{4}|\d{3} \d{4}|\d{3}-\d{3}-\d{4}", str(soup))
            numbersextraction3 = re.findall(r"\d{3}\W\d{3}\W\d{4}", str(soup))
            get_first_number = re.findall(r"\(\d{3}\)", str(soup))
            if re.findall(r"\d{3}-\d{3}-\d{4}|\d{3}-\d{3}-\d{4}/\d{4}", str(soup)):
                await asyncio.sleep(0.5)
                return re.findall(r"\d{3}-\d{3}-\d{4}|\d{3}-\d{3}-\d{4}/\d{4}", str(soup))
            elif re.findall(r"\(\d{3}\)", str(soup)):
                if len(numbersextraction3) >= 1:
                    return numbersextraction3
                else:
                    get_index_number = numbersextraction.index(get_first_number[0])
                    await asyncio.sleep(0.5)
                    return numbersextraction[get_index_number] + " " + numbersextraction[get_index_number + 1]
            elif re.findall(r"\W\d{11}", str(soup)):
                store_number = []
                await asyncio.sleep(0.5)
                for i in re.findall(r"\W\d{11}", str(soup)):
                    if str(i).startswith("+"):
                        store_number.append(i)
                return store_number
            elif re.findall(r"\d{3}-\d{3}-\d{4}/\d{4}", str(soup)):
                await asyncio.sleep(0.5)
                return re.findall(r"\d{3}-\d{3}-\d{4}/\d{4}", str(soup))
            else:
                await asyncio.sleep(0.5)
                return None
    except Exception as e:
        await asyncio.sleep(0.5)
        return e


async def get_number_list(numbers_list):
    """Get the individul number provided in the payload
    and filter all the Spacial Character from the single number the
    and give a raw string of only containing number."""
    try:
        filter_number = re.findall(r"[0-9]+", numbers_list)
        await asyncio.sleep(0.0)
        return " ".join(filter_number).replace(" ", "")
    except Exception as e:
        await asyncio.sleep(0.0)
        return e


def url_with_number(url):
    url_list = []
    store_ow_number = []
    for i in asyncio.run(get_all_urls(url)):
        store_number = set(asyncio.run(get_ow_number(i)))
        url_list.append(i)
        store_ow_number.append(store_number)
    res = {}
    for key in url_list:
        for value in store_ow_number:
            res[key] = value
            store_ow_number.remove(value)
            break
    return json.dumps(str(res))

