alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# Update dictionary
alien_0['color'] = 'pink'
print(alien_0)

# Add new item
alien_0['height'] = 6.8
print(alien_0)

# Determine how far to move the alien based on its current speed.
alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
if alien_1['speed'] == 'show':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_1['x_position'] = alien_1['x_position'] + x_increment
print(f"New position: {alien_1['x_position']}")

# Delete key, pair from dictionary
del alien_0['height']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = favorite_languages['jen'].upper()
print(language)

"""
Here the `get` function 1st argument print dictionary data 
if not found by default second argument return default value
"""
language = favorite_languages.get('ohi', 'Not found about that')
print(language)

print('\n')

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, val in user_0.items():
    print(f"Key: {key}")
    print(f"value: {val}")

for name, language in favorite_languages.items():
    print(f"{name.title()}s favorite language is {language.title()}")

print('\n')

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
