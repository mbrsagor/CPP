prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name please?: "
name = input(prompt)
print(f"\nHello, {name}! how are you?")

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
