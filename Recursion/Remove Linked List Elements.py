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
        head.next = compileLinkedList(nodes[1:])
        head.val = nodes[0]
        return head

def removeElements(head: ListNode, val: int):
    """
    Funzione ricorsiva che rimuove tutti i nodi di una linked list
    che contengono il valore `val`.

    Logica:
    - Caso base: se la lista è vuota (head = None), ritorna None.
    - Se il nodo corrente ha valore `val`, viene “saltato” e la funzione
      prosegue sul resto della lista, eliminando quindi il nodo.
    - Se il nodo corrente NON ha valore `val`, viene mantenuto e il suo
      puntatore `next` viene aggiornato al risultato della ricorsione
      applicata al resto della lista.
    - Alla fine la lista viene ricostruita senza i nodi indesiderati.
    """
    if head:
        if head.val == val:
            if head.next:
                head.next = removeElements(head.next, val)
                head = head.next
                return head

            else:
                head = None
                return head
        else:
            head.next = removeElements(head.next, val)
            return head
    else:
        return None

list_of_nodes = [1,2,6,6,3,4,5,6]
val = 6
linked_list = compileLinkedList(list_of_nodes)
new_linked_list = removeElements(linked_list,val)
print(new_linked_list)

