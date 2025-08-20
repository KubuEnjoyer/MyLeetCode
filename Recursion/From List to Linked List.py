class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def compileLinkedList( nodes: list):
    head = ListNode()
    k = len(nodes)
    if k == 1:
        head.val = nodes[0]
        head.next = None
        return head
    else:
        head.next = CompileLinkedList(nodes[1:])
        head.val = nodes[0]
        return head

list_of_nodes = [1,2,6,3,4,5,6]
linked_list = CompileLinkedList(list_of_nodes)