'''
def greet(name):
    print(f"Hello, {name}")
    
greet("Shumani")

def add(a, b):
    return a + b

result = add(2, 5)
print(result)
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
    def greet(name, greetings="hello"):
        print(f"{greetings}, {name}")
        
    
    greet("bob", "Good morning")    