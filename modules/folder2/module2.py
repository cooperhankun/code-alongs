from sys import path

path.append("folder1")

import module1

def say_hello2():
    print(f"{__name__} say hello")

module1.say_hello1()

# want to import say_hello1()

