def add_prefix(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return prefix+result
        return wrapper
    return decorator 


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

# Main program
if __name__ == "__main__":

    numbers = [1, 2, 3, 4, 5]
    incremented_numbers = list(map(lambda x: x + 10, numbers))
    print("Incremented numbers:", incremented_numbers)

    @add_prefix("Hello, ")
    def greet(name):
        return name

    print("Greeting:", greet("Alice"))

    print("Fibonacci sequence:")
    for num in fibonacci(10):
        print(num)

    person = Person("Bob", 30)
    print("Person:", person.name, person.age)