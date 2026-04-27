class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def tambahKendaraan(head, newNode, position):
  if position == 1:
    newNode.next = head
    return newNode

  currentNode = head
  for _ in range(position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  newNode.next = currentNode.next
  currentNode.next = newNode
  return head

def hapusKendaraan(head, nodeToDelete):
  if head == nodeToDelete:
    return head.next

  currentNode = head
  while currentNode.next and currentNode.next != nodeToDelete:
    currentNode = currentNode.next

  if currentNode.next is None:
    return head

  currentNode.next = currentNode.next.next

  return head

node1 = Node("B 1234 ABC",)
node2 = Node('D 888 XYZ')
node3 = Node('A 111 TUV')
node4 = Node('B 2022 EFG')

node1.next = node2
node2.next = node3
node3.next = node4

#ORI
print("LIST PARKIR AWAL:")
traverseAndPrint(node1)

#TAMBAH
newNode = Node('H 0106 ASDF')
node1 = tambahKendaraan(node1, newNode, 2)

print("\nLIST PARKIR DITAMBAHKAN:")
traverseAndPrint(node1)

#HAPUS
node1 = hapusKendaraan(node1, node4)

print("\nLIST PARKIR YANG DIHAPUS:")
traverseAndPrint(node1)