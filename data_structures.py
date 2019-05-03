from collections import deque
queue = deque(['Mehdi', 'Mel', 'Kelvin', 'Jeff'])
queue.append('Mooji')
print(queue)

print(queue.popleft())
print(queue.pop())

squares = []
for x in range(10):
  squares.append(x**2)

print(squares)