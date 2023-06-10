class PriorityQueue:
    def __init__(self) -> None:
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0
    
    def insert(self, item, priority):
        self.heap.append((item, priority))
        self._heapify_up(len(self.heap) - 1) # it's a list and we did -1 in order to get the index of the newly added element.
    
    def remove(self):
        if self.is_empty():
            print("The Priority Queue is empty.")

        self._swap(0, len(self.heap) - 1)
        item, priority = self.heap.pop()
        self._heapify_down(0)

        return item

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[index][1] < self.heap[parent][1]:
            self._swap(index,parent)
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if left_child < len(self.heap) and self.heap[left_child][1] < self.heap[index][1]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child][1] < self.heap[index][1]:
            smallest = right_child
        if smallest != index:
            self._swap(smallest,index)
            self._heapify_down(smallest)
        
        #The main goal of this _heapify_down() is to bring back the least priority item to the bottom after it was swap while remove()

    def _swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]