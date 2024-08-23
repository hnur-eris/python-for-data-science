no_names = {
    "NoneType": "Nothing",
    "float": "Cheese",
    "int": "Zero",
    "str": "Empty",
    "bool": "Fake"
}

def NULL_not_found(object: any) -> int:

    class_name = object.__class__.__name__
    if object != "Brian":
        print(f"{print_names(class_name)}: {object} {object.__class__}")
        return 0
    else:
        print(f"Type not found")
        return 1

def print_names(class_name: str) -> str:
    return no_names.get(class_name)

# NULL_not_found("merhaba")