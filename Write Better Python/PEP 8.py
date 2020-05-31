import sys

print(sys.version)
print(sys.executable)


def greet(whoToGreet):
    greeting = 'Hello. {}'.format(whoToGreet)
    return greeting



print(greet('World'))
print(greet('Corey'))