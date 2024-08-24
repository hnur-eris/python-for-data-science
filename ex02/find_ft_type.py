def all_thing_is_obj(object: any) -> int:
    # print(object.__class__)
    data = object.__class__
    dt = object.__class__.__name__
    if dt == "int":
        print("Type not found")
        return 42

    print(f"{dt.capitalize()} : {data}") if dt.capitalize() != "Str"  else print(f"{object} is in the kitchen : {data}")
    return 42
#tester.py dosyası silinmeli

# all_thing_is_obj("merhaba")