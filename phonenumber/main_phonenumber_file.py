from webscaping.url_individual import *


async def get_ow_number(url):
    try:
        """All the Required Pattern related to Phone_number based on the url provided
        and check the pattern associated with it."""
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=6)) as session:
            async with session.get(url, ssl=True) as requs:
                soup = BeautifulSoup(await requs.text(), 'html.parser')
            await session.close()
            numbersextraction = re.findall(r"\(\d{3}\)|\d{3}-\d{4}|\d{3} \d{4}|\d{3}-\d{3}-\d{4}|\d{3}\W\d{4}"
                                           r"\W\d{11}|\d{3}\W\d{3}\W\d{4}", str(soup))
            phone_pattern = [r"\d{3}\W\d{3}\W\d{4}/\d{4}",
                             r"\d{3}\W\d{3}\W\d{4}|\d{1}-\d{3}-\d{3}-\d{4}"]
            get_first_number = re.findall(r"\(\d{3}\)", str(soup))
            numbersextraction3 = re.findall(r"\d{3}\W\d{3}\W\d{4}", str(soup))
            store_phone_number = []
            if re.findall(r"\(\d{3}\)", str(soup)):
                if len(numbersextraction3) >= 1:
                    return [numbersextraction3]
                else:
                    get_index_number = numbersextraction.index(get_first_number[0])
                    await asyncio.sleep(0.5)
                    return [numbersextraction[get_index_number] + " " + numbersextraction[get_index_number + 1]]
            for i in range(len(phone_pattern)):
                if re.findall(phone_pattern[i], str(soup)):
                    store_phone_number.append(list(set(re.findall(phone_pattern[i], str(soup)))))
            return store_phone_number
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
    for i in [i for i in [None if re.findall(r"facebook|instagram", i) else i for i in asyncio.run(get_all_urls(url))]
              if i is not None]:
        print(i)
        store_number = asyncio.run(get_ow_number(i))
        url_list.append(i)
        store_ow_number.append(store_number)
    res = {}
    for key in url_list:
        for value in store_ow_number:
            res[key] = value[0]
            store_ow_number.remove(value)
            break
    return json.dumps(str(res))

