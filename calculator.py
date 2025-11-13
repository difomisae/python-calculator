def add(a: float, b: float)-> float:
    return a + b

def subtract(a: float, b:float)-> float:
    return a - b

def multiply(a:float , b: float) -> float:
    return a * b

def multiply(a:float,b:float) -> float:
  return a * b

def divide(a:float, b:float)-> float:
    if a == 0:
        print("Error: division by zero.")
        return None
    return a/b

def main():
    print("=== Python Calculator ===")
    while True:
        print("\\n Operations: + - * /")
        op = input("Choose an operation (or 'q' to quit): ")
        if op=='q':
            break
        try:
            a: float = float(input("First number: "))
            b: float = float(input("Second number: "))
        except ValueError:
            print("Invalid numbers.")
            continue

        match op:
            case "+": print("Result: ", add(a,b))
            case "-": print("Result: ", subtract(a,b))
            case "*": print("Result: ", multiply(a,b))
            case "/": print("Result: ", divide(a,b))

if __name__ == "__main__":
        main()
   

