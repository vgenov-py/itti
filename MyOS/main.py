from os import system, getcwd, listdir
from myos import MyOS

user = ""

while user != "q":
    test_1 = MyOS()
    if user == "1":
        print(test_1.ls())
    print('''MyOS version 1.0
    1. ls
    2. rm
    Q. mkdir
    ''')
    user = input(": ")
    system("clear")

print("Bye!")