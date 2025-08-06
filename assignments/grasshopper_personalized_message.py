

def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"

if __name__ == "__main__":
    print(greet("Alice", "Alice"))   
    print(greet("Bob", "Alice"))     
