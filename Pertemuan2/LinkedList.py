class Node:
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.next = pointer

class Linkedlist:
   def __init__(self):
        self.head = None

   def insert_at_first(self, data):
    node = Node(data,self.head)
    self.head = node

   def insert_at_last(self, data):
      if self.head is None:
         self.head = Node(data)
      else:
         node_sekarang = self.head
         while node_sekarang.next: 
             node_sekarang = node_sekarang.next

         node = Node(data)
         node_sekarang.next = node

   def insert_at(self, index, data):
      if index < 0 or index > self.length() - 1:
         print("index tidak valid")
      elif index == 0:
         self.insert_at_first(data)
      else:
         urutan = 0
         node_sekarang = self.head

         while urutan < index - 1:
            urutan += 1
            node_sekarang = node_sekarang.next 

         node = Node(data, node_sekarang.next)
         node_sekarang.next = node
   

   def print(self):
    if self.head is None:
       print("data kosong")
    else:
       text_print = ''
       node_sekarang = self.head

       while node_sekarang:
          text_print += str(node_sekarang.data) + "->"
          node_sekarang = node_sekarang.next

       print(text_print)

   def length(self):
      urutan = 0
      data_sekarang = self.head

      while data_sekarang:
         data_sekarang = data_sekarang.next
         urutan += 1

      return urutan

LL = Linkedlist()

# insert
LL.insert_at_first("jeruk")
LL.insert_at_first("mangga")
LL.insert_at_first("manggis")
LL.insert_at_last("apel")
LL.insert_at(2, "anggur")

#print
LL.print() 
print(LL.length())
