high_income = False
good_credit = True
student = True

if (high_income or good_credit) and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

for number in range(1, 4):
    print("Attempt", number, (number * "."))

for x in range(1, 10):
    for y in range(1, 10):
        print(f"{x} * {y} = {x * y}")
    print("----------")


def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")

    greet_user("John", "Smith")
