import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0


def push(self, item, priority):
    heapq.heappush(self._quue, (-property, self._index. item))


def pop(self):
    return heapq.heappushpop(self._queue)[-1]



class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)



q = PriorityQueue()
q.push(Item('foo'), 1)        
print(q)    
