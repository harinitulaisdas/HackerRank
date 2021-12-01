class singllyLinkedListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class singleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, data):
        node = singllyLinkedListNode(data)

        if not self.head:
            self.head = node
            self.head.data = data
        else:
            self.tail.next = node

        self.tail = node
        return self.head

    def insert_node_at_the_tail(self, data):
        if self.head is None:
            self.head = singllyLinkedListNode(data)
            return self.head

        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = singllyLinkedListNode(data)
        return self.head

    def print_linked_list(self):
        if self.head == None:
            print("List is empty")

        else:
            curr = self.head
            while curr:
                print(curr.data)
                curr = curr.next

    def insert_at_the_head(self,data):
        if self.head is None:
            self.head = singllyLinkedListNode(data)
            return self.head

        node = singllyLinkedListNode(data)
        node.next = self.head
        return node

    def insert_node_at_position(self,data,pos):
        count = 0
        if self.head is None:
            self.head= singllyLinkedListNode(data)
            return self.head
        if pos == 1:
            self.insert_at_the_head(data)
            return
        else:
            curr = self.head
            temp_node = singllyLinkedListNode(data)
            while count!=pos-1 and curr.next!=None:
                count+=1
                curr = curr.next

            temp_node.next = curr.next
            curr.next = temp_node
            return self.head

    def delete_node(self,position):
        count = 0
        curr = self.head
        prev = singllyLinkedListNode
        if self.head is None:
            print("List is empty")
            return self.head
        if position == 0:
            curr = curr.next
            self.head = None
            self.head = curr
            return self.head

        else:
            while curr.next != None:
                if count == position:
                    break
                prev = curr
                curr = curr.next
                count += 1
        prev.next = curr.next
        curr = None
        return self.head

if __name__ == '__main__':
    llist_count = int(input())

    llist = singleLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    print("list  ")
    llist.print_linked_list()

    # print("insert at end")
    # llist_item = int(input())
    # llist.insert_node_at_the_tail(llist_item)
    # llist.print_linked_list()
    #
    # print("insert at the head")
    # llist_item = int(input())
    # llist.insert_at_the_head(llist_item)
    # llist.print_linked_list()

    # print("insert at a position in the list")
    # llist_item = int(input())
    # llist.insert_node_at_position(llist_item,3)
    # llist.print_linked_list()

    print("delete a node")
    pos = int(input())
    llist.delete_node(pos)
    llist.print_linked_list()



