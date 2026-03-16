import messages

first_name = "Alex"
second_name = "Clinton"

# fullname = first_name + second_name
fullname = first_name + " " + second_name
fullname2 = f"{first_name} {second_name}"
welcome_message = "Welcome, Mr. " + fullname

welcome_message_f_string = f"Welcome, Mr. {fullname}!"
welcome_from_template = messages.MSG_WELCOME_MISTER.format(fullname=fullname)
print(welcome_from_template)

print(fullname)
print(first_name)
print(welcome_message)
print(welcome_message_f_string)
