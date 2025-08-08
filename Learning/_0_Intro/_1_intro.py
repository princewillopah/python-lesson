name = input("Enter your name: ")
print(f"Hello, {name}!")
with open("greeting.txt", "w") as file:
    file.write(f"Greeted {name}")