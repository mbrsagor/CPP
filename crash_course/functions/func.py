def greet_user(username):
    print(f"Hello {username.title()}!")


greet_user("mbr sagor")


def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')


def get_formatted_name(first_name, last_name, middle_name=None):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


get_name = get_formatted_name('mbr', 'sagor')
print(get_name)


def build_person(first_name, last_name):
    person = {'first_name': first_name, 'last_name': last_name}
    return person


person_name = build_person('mbr', 'sagor')
print(person_name)

# Using a Function with a while Loop
while True:
    f_name = input("First name: ")
    l_name = input("Last name: ")

    make_full_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {make_full_name.title()}")
