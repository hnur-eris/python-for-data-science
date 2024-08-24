import sys
ac = sys.argv

try:
    if len(ac) == 1:
        exit(0) 

    assert len(ac) <= 3, "more than one argument is provided"
    data = sys.argv[1]
    assert data.lstrip("-").isdigit(), "argument is not an integer"
    number = int(data)
    print("I'm Even.") if number % 2 == 0 else print("I'm Odd.")

    
except AssertionError as msg:
    print(f"AssertionError: {msg}")
#acaba newline eklesem mi

