name = [
    {
        "(en-us/st)": "Signature Home Furniture"
    },
    {
        "(en-ca/st)": "Signature Home Furniture"
    },
    {
        "(en-th/st)": "Signature Home Furniture"
    },
    {
        "(en/st)": "Signature Home Furniture"
    },
    {
        "(global/st)": "Signature Home Furniture"
    }
]

get_v = [i for i in name][0]
print(get_v.get("(en-ca/st)"))
