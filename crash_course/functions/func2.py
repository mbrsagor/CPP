def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

    for topic in toppings:
        print(topic)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **userinfo):
    """Build a dictionary containing everything we know about a user."""
    userinfo['first_name'] = first
    userinfo['last_name'] = last
    return userinfo


user_profile = build_profile('mbr', 'Sagor', location='Dhaka-Bangladesh', job_title='Software engineer')
print(user_profile)
for key, val in user_profile.items():
    print(f"{key} : {val}")
