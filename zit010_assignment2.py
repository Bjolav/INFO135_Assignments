#task1:
list = [1700, 2020, 1800, 1600, 1900]
counter = 0
for item in range(len(list)):
    if counter == 3:
        print(list)
        break
    selection = item
    for j in range(item + 1, len(list)):
        if list[selection] > list[j]:
            selection = j
    holder = list[item]
    list[item] = list[selection]
    list[selection] = holder
    counter += 1
print("Answer to Task 1 is b")

#task2:
my_tuple = (3,6,12,24,48)

def multiply_it(tuple):
    sum = 1
    try:
        for item in tuple:
            sum = sum * item
        return sum
    except Exception as e:
            print(f"A {e} error has ocurred")

print(f"The answer to task 2 is {multiply_it(my_tuple)}")

#task3:
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def reverse_list(list):
    result = []
    stack = Stack()
    for item in list:
        stack.push(item)
    while stack.is_empty() is False:
        result.append(stack.pop())
    print(f"The list reversed becomes {result}")

mylist = [1, 2, 3, 4, 5]
reverse_list(mylist)