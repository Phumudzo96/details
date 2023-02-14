name = input("Enter your name: ")
age = input("Enter your age: ")
house_number = input("Enter your house number: ")
street_name = input("Enter your street name: ")
sentence = ("This is {} he is {} years old and lives at house number {}  on {} street").format(name, age, house_number, street_name)
print(sentence)

