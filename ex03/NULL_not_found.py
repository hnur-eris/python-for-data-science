variables = {
    "Nothing" : None,
    "Garlic": float("NaN"),
    "Zero" :0 ,
    "Empty" :'' ,
    "Fake" : False,
    "Brian": "Brian"
}

df = {
    "NoneType" : "None",
    "float": "nan",
    "int": 0,
    "str": "",
    "bool": "False",
    0 : "Type not Found"
}

def NULL_not_found(object: any) -> int:
     # print(object.__class__)
    data = object.__class__
    data_type = str(data)
    dt = data_type.split("'")[1]
    # print_names(object)
    # print_df(dt)
    # print(f"{print_none(dt)}")
    
    print(f"{(object)} : {print_none(dt)} {data}")
    return 0
    
def print_names(word):
    if word in variables:
        return word

def print_none(w):
    if w in df:
        return df[w]