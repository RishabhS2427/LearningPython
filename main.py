# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Graph():
    def __init__(self, id):
        self.id = id
        self.id = 80

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    val = Graph(200)
    print(val.id)


# loop while
def loop_while() :
    print('loop while')
    counter = 0
    while counter < 10:
        print(f" {counter}")
        counter += 1

def for_simple_range_loop():
    print('for simple range loop')
    counter = 0
    for item in range(10):
        print(f" {counter}")
        counter += 1

def for_with_enumerate():
    print('for with enumerate')
    name = ["Rishabh", "Sam", "Anuj"]
    for i ,item in enumerate(name):
         print(f" {i} - {item}")

def add (a, b) :
    return (a + b)


def add3 (a, b) :
    c = a + b
    return (c)

def add2(a,b) :
    return sum(a + b)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(add(12, 13))
    print(add3(14, 13))
    loop_while()
    for_simple_range_loop()
    for_with_enumerate()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# val = Graph(200)
# print(val.id)

