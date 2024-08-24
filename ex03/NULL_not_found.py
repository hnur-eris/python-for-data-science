no_names = {
    "NoneType": "Nothing",
    "float": "Cheese",
    "int": "Zero",
    "bool": "Fake",
    "str": "Empty"
}

def NULL_not_found(object: any) -> int:
    null = [None, "", '', float("NaN"), 0, False ]
    if object in null:
        class_name = object.__class__.__name__
        if class_name in no_names:
            print(f"{print_names(class_name)}: {object} {object.__class__}")
            return 0
    else:
        print("Type not Found")  
        return 1

def print_names(class_name: str) -> str:
    return no_names.get(class_name)

#float kısmında type not found basıyo
#bunun haricinde doğru çalışıyo
#tester.py silmeyi unutma
