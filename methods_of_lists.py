names = ['Anna', "Ivan"]
mixed = [
    1,
    90.901,
    True,
    False,
    "some text",
    ['123', 1232],
]

# get item by index

first_element = mixed[0]
print(first_element)

third_element = mixed[2]
print(third_element)

last_element = mixed[-1]
print(last_element)

last_element_in_last_element = last_element[-1]
print(last_element_in_last_element)

# some_element = mixed[10]

# change lists
string = '123'
print(id(string))
string = string + '1'
print(id(string))

number = 123
print(id(number))
number = number + 1
print(id(number))

numbers = [1, 3, 4]
print(id(numbers))
numbers[0] = 200  # change elem
print(numbers)
print(id(numbers))

# add values
numbers.append(3000)
numbers.append(3000)
print(numbers)
print(id(numbers))