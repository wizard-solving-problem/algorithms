class List_node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def has_cycle(head):
    if not head and not head.next: return False
    
    slow, fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast: return True
        
    return False