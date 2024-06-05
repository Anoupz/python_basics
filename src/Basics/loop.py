age: int = 20

if age > 18:
    print("You are an adult")
else:
    print("You are a minor")


result = "You are an adult" if age > 18 else "You are a minor"

print(f"Using a shorter syntax {result}")


text: str = "Hello World"

for i in range(3):
    print(f"{i}: {text}")

people: list[str] = ["Max", "Tom", "John"]

for person in people:
    print(person)
