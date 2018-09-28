from collections import deque

def create():
    q = deque()
    q.appendleft(1)
    q.appendleft(2)
    oneMore(q)
    return q

def oneMore(q):
    q.appendleft(3)


print(create())


