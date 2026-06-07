class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2copy= {None:None}
        curr= head
        while curr:
            copy= Node(curr.val)
            old2copy[curr]= copy
            curr=curr.next
        curr=head
        while curr:
            copy=old2copy[curr]
            copy.next=old2copy[curr.next]
            copy.random=old2copy[curr.random]
            curr=curr.next
        return old2copy[head]