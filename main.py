'some string 1'
"some string 2"
"""big string"""

name = 'Alex'
surname = 'Clinton'
# імя = "kjfdghgvhf"   bad idea
my_favorite_city = "Одеса - <>"
print(my_favorite_city)

link_poem = "http://litopys.org.ua/shevchenko/shev205.htm"
big_string = """
Мені тринадцятий минало.
Я пас ягнята за селом.
Чи то так сонечко сіяло,
Чи так мені чого було?
Мені так любо, любо стало,
Неначе в Бога......
Уже прокликали до паю,
А я собі у бур’яні
Молюся Богу... І не знаю,
Чого маленькому мені
Тойді так приязно молилось,
Чого так весело було.
Господнє небо, і село,
Ягня, здається, веселилось!
І сонце гріло, не пекло!
"""

print(big_string)

# identification of the object
print(id(big_string))

print(ord("D"))
print(ord("Ї"))
print(chr(1031))

unicode_cow = "🐮"
print(ord(unicode_cow))
unicode_cow2 = "\U0001F42E"

print(unicode_cow)
print(unicode_cow2)
