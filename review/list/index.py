import keyword

check_key = keyword.iskeyword("python")
print(check_key)

check_key2 = keyword.iskeyword("try")
print(check_key2)

check_key3 = keyword.iskeyword("if")
print(check_key3)

check_key4 = keyword.iskeyword("isInstance")
print(check_key4)

"""
Here, `find` and `index` builthin python method
return: position of `string` index.
"""
text = "I would like to say something about that."
print(text.find("say"))
print(text.rfind("say"))
print(text.index("say"))
print(text.rindex("say"))

