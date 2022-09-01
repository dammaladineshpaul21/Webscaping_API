import pandas as pd


def call_number_pat(get_nu):
    phone_number = get_nu
    if len(phone_number) >= 11:
        get_phonecode = phone_number[0:2], phone_number[0:3], phone_number[0:4], phone_number[0:5]
        read_data = pd.read_json("../resources_file/phone_number.json")
        get_Data = pd.DataFrame(read_data, columns=['dial_code'])
        get_r = [i for i in list(map(lambda x: x if x in get_Data.to_numpy() else None, get_phonecode)) if
                 i is not None]
        return get_r
    else:
        if len(phone_number) >= 11:
            return phone_number[1::]
        else:
            return "Missing Number"

