class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.list_queue = []

    def put(self, elem):
        self.list_queue.insert(0, elem)

    def get(self):
        if self.isempty():
            raise QueueError("Queue empty")
        return self.list_queue.pop()

    def isempty(self):
        return len(self.list_queue) == 0


class SuperQueue(Queue):
    def isempty(self):
        return len(self.list_queue) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
