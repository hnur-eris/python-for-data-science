no_names = {
    "NoneType": "Nothing",
    "float": "Cheese",
    "int": "Zero",
    "bool": "Fake",
    "str": "Empty"
}

def NULL_not_found(object: any) -> int:
    null = [None, "", '', float("NaN"), 0, False,"nan"]
    
    if object in null or object != object:
        class_name = object.__class__.__name__            
        print(f"{print_names(class_name)}: {object} {object.__class__}")
        return 0
    else:
        print("Type not Found")  
        return 1

def print_names(class_name: str) -> str:
    return no_names.get(class_name)

#tester.py silmeyi unutma
