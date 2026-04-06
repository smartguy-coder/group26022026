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

numbers = [1, 3, 3, 4]
print(id(numbers))
numbers[0] = 200  # change elem
print(numbers)
print(id(numbers))

# add values
numbers.append(33)
numbers.append(30001)
print(numbers)
print(id(numbers))

numbers.insert(1, 22)
print(numbers)
print(id(numbers))

# remove data
numbers.remove(3)
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(0)
print(numbers)

is_33_presented_in_numbers = 33 in numbers
print(is_33_presented_in_numbers)
if is_33_presented_in_numbers:
    numbers.remove(33)
print(numbers)

# length of list
elements_in_numbers_count = len(numbers)
print(elements_in_numbers_count)

# sorting
numbers2 = [1, 7, 2, 3]
print(numbers2)
print(id(numbers2))
numbers2.sort(reverse=True)
print(numbers2)
print(id(numbers2))
print(numbers2)

numbers3 = sorted(numbers2)
print(numbers3, 'sorted')
print(numbers2)
print(id(numbers2))
print(id(numbers3))

