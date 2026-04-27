class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      
def sisipkan_vip(head, plat_baru, plat_target):
   #Traverse
   currentNode = head
   while currentNode:
      print(currentNode.data, end=" -> ")
      currentNode = currentNode.next
   print("null")

   if plat_target == 1:
      newNode.next = head
      return newNode

   currentNode = head
   for _ in range(plat_target - 2):
      if currentNode is None:
         break
      currentNode = currentNode.next

   newNode.next = currentNode.next
   currentNode.next = newNode
   return head



node1 = Node("B 1234 ABC")
node2 = Node("D 8888 XYZ")
node3 = Node("A 111 TUV")
node4 = Node("B 2022 EFG")

node1.next = node2
node2.next = node3
node3.next = node4

newNode = Node("F 789 FGH")
node1 = sisipkan_vip(node1, newNode, 2)

sisipkan_vip(node1, newNode, 2)