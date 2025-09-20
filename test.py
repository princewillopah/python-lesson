


def funcDob(dob):
    return 2025 - dob

def funcName(name):
    return name.lower().capitalize()

# name_array = ["James","smItH","TaYo","jude","AKUDO"]

# for name in name_array:
#     print(func(name))
#     # print(name)

n = input("Enter your name: ")
age = int(input("Enter your year of birth: "))

print(f"Hello {funcName(n)}, you are {funcDob(age)} years old.")

def test():
    print("This is a test function")
    naame = "James"
    # dob = 1981
    print(f"Hello {funcName(naame)}, you are {funcDob(1981)} years old.")

test()