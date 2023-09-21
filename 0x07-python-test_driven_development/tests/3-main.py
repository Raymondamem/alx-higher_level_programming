#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Raymond", "Amem")
say_my_name("Grace", "Amem")
say_my_name("David")
try:
    say_my_name(18, "Amem")
except Exception as e:
    print(e)
