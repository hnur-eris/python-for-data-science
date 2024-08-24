def all_thing_is_obj(object: any) -> int:
    o_types = ["list", "tuple", "set", "dict", "str"]
    
    data = object.__class__
    dt = object.__class__.__name__
    if dt in o_types:
        print(f"{dt.capitalize()} : {data}") if dt.capitalize() != "Str"  else print(f"{object} is in the kitchen : {data}")
    else:
        print(f"Type not found")
    return 42
#tester.py dosyası silinmeli

# all_thing_is_obj("merhaba")