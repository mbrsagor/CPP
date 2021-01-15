requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
else:
    print("They are same")

answer = 17
if answer != 40:
    print("This is not correct answer?? Please  try again.")
else:
    print("This is correct answer! You are welcome.")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
