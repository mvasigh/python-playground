from collections import deque
from math import pi
import json

queue = deque(["Mehdi", "Mel", "Kelvin", "Jeff"])
queue.append("Mooji")
print(queue)

print(queue.popleft())
print(queue.pop())

squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)

squares_map = list(map(lambda x: x ** 2, range(10)))
print("Using the map and lamba method", squares_map)

squares_short = [x ** 2 for x in range(10)]
print("Using the shortcut", squares_short)

# sweet list comprehension example
combined_list = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combined_list)

print([str(round(pi, i)) for i in range(1, 6)])

# tuple packing
t = "hello", "world", "universe"
print(t)

# tuple unpacking
msg1, msg2, msg3 = t
print(msg1, msg2, msg3)

# multiple variable assignment is just a combintation of
# tuple packing and sequence unpacking
# unpacking works with lists too, like destructuring in JS
man, cat = ["Mehdi", "Mooji"]
print(man, cat)

# this is how you create json string, i.e. JSON.stringify
json_string = json.dumps({"hello": "world"})
print(json_string)