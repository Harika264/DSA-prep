from collections import deque

q = deque()

q.append(10)
q.append(20)
q.append(30)

print("Removed:", q.popleft())
print("Queue:", q)
