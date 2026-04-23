class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 

    def is_empty(self):
        return self.count == 0

    def push(self, url):
        new_node = Node (url)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.count += 1
    
    def pop(self):
        if self.is_empty():
            return 'Riwayat Kosong.'
        popped_node = self.top
        self.top = self.top.next
        self.count -= 1
        return popped_node.url
    
    def peek(self):
        if self.is_empty():
            return None
        return self.top.url

    def size(self):
        return self.count
    
    def traverseAndPrint(self):
        currentNode = self.top
        while currentNode:
            print(currentNode.url, end=" -> ")
            currentNode = currentNode.next
        print()
    
riwayatNavigasi = StackLinkedList()

riwayatNavigasi.push('Google')
riwayatNavigasi.push('Youtube')
riwayatNavigasi.push('Instagram')
riwayatNavigasi.push('Soliter')
riwayatNavigasi.push('Google Classroom')

print("LinkedList: ", end="")
riwayatNavigasi.traverseAndPrint()
print('Pop: ', riwayatNavigasi.pop())
print('Peek: ', riwayatNavigasi.peek())
print("LinkedList after Pop: ", end="")
riwayatNavigasi.traverseAndPrint()
print('isEmpty: ', riwayatNavigasi.is_empty())
print('Size: ', riwayatNavigasi.size())