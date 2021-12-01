class singlyLinkedListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class singleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, data):
        node = singlyLinkedListNode(data)

        if not self.head:
            self.head = node
            self.head.data = data
        else:
            self.tail.next = node

        self.tail = node
        return self.head


def reverse_list(list):
    curr = list.head
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    list.head = prev
    return list


def print_linked_list(list):
    if list.head == None:
        print("List is empty")
    else:
        curr = list.head
        while curr:
            print(curr.data)
            curr = curr.next


if __name__ == '__main__':
    llist_count = int(input())
    llist = singleLinkedList()
    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    print("list before: ")
    print_linked_list(llist)
    print("list after: ")
    reverse_list(llist)
    print_linked_list(llist)
