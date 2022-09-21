from webscaping.url_individual import *


async def get_ow_number(url):
    try:
        """All the Required Pattern related to Phone_number based on the url provided
        and check the pattern associated with it."""
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=6)) as session:
            async with session.get(url, ssl=True) as requs:
                soup = BeautifulSoup(await requs.text(), 'html.parser')
            await session.close()
            phone_pattern = [r"\d{3}\W\d{3}\W\d{4}/\d{4}", r"\(\d{3}\) \d{3}-\d{4}",
                             r"\d{3}\W\d{3}\W\d{4}|\d{1}-\d{3}-\d{3}-\d{4}"]
            store_phone_number = []
            for i in range(len(phone_pattern)):
                if re.findall(phone_pattern[i], str(soup)):
                    store_phone_number.append(list(set(re.findall(phone_pattern[i], str(soup)))))
            await asyncio.sleep(0.5)
            return store_phone_number
    except Exception as e:
        await asyncio.sleep(0.5)
        return e


async def get_number_list(numbers_list):
    """Get the individul number provided in the payload
    and filter all the Spacial Character from the single number the
    and give a raw string of only containing number."""
    numbers_ = "".join(reversed(" ".join(reversed(numbers_list)).replace(" ", "")[0:10]))
    try:
        filter_number = re.findall(r"[0-9]+", numbers_)
        await asyncio.sleep(0.0)
        return " ".join(filter_number).replace(" ", "")
    except Exception as e:
        await asyncio.sleep(0.0)
        return e


def url_with_number(url):
    try:
        url_list = []
        store_ow_number = []
        for i in [i for i in
                  [None if re.findall(r"facebook|instagram", i) else i for i in asyncio.run(get_all_urls(url))]
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
        return json.dumps(str(res))
    except Exception:
        return "Url with number has an issue"

