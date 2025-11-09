# problem : 3217. Delete Nodes From Linked List Present in Array
- https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/

```txt
You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.



Example 1:

Input: nums = [1,2,3], head = [1,2,3,4,5]

Output: [4,5]

Explanation:
Remove the nodes with values 1, 2, and 3.

Example 2:

Input: nums = [1], head = [1,2,1,2,1,2]

Output: [2,2,2]

Explanation:
Remove the nodes with value 1.

Example 3:

Input: nums = [5], head = [1,2,3,4]

Output: [1,2,3,4]

Explanation:
No node has value 5.



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
All elements in nums are unique.
The number of nodes in the given list is in the range [1, 10^5].
1 <= Node.val <= 10^5
The input is generated such that there is at least one node in the linked list that has a value not present in nums.
```

# answer

## al
- nums.length <= 10^5 = O(N)
- nodes.length <= 10^5 = O(M)
- O(N) = 10^5

```python
# case 1
# node 마다 in (O(N)) 을 이용해서 nums list 에 포함되는지 찾는 방법 시간 복잡도 O(N^2)
# Time Limit Exceeded 576 / 582 testcases passed

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p.val in nums:
            p = p.next
        start_head = p
        while p:
            if p.next and p.next.val in nums:
                p.next = p.next.next
            else:
                p = p.next
        return start_head

# case 2
# list node 값이 nums 에 존재하는지 찾을 때 2진 탐색(O(long N))을 사용하는 방법, nums 정렬에 O(NlogN)
# list node 마다 수행하기 때문에 총 시간 복잡도 O(NlogN)
# Runtime 183ms Beats 5.04%

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums.sort()
        len_nums = len(nums)
        p = head

        i = bisect.bisect_left(nums, p.val)
        while i < len_nums and nums[i] == p.val:
            p = p.next
            i = bisect.bisect_left(nums, p.val)
        start_head = p

        while p:
            if p.next:
                i = bisect.bisect_left(nums, p.next.val)
                if i < len_nums and nums[i] == p.next.val:
                    p.next = p.next.next
                    continue
            p = p.next

        return start_head

# case 3
# nums list 를 set 자료구조(hash table)로 변경 후 in 으로 존재 유무를 찾으면 O(1)
# node list 마다 in 을 수행하기 때문에 총 시간 복잡도 O(N)
# Runtime 49ms Beats 90.05%

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        nums_set = set(nums)
        while p.val in nums_set:
            p = p.next
        start_head = p
        while p:
            if p.next and p.next.val in nums_set:
                p.next = p.next.next
            else:
                p = p.next
        return start_head

# case 4
# dict 자료구조도 hash table로 만들어져 있는데 적용하면?
# Runtime 79ms Beats 16.98%

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        nums_dict = dict(zip(nums, [0]*len(nums)))
        while p.val in nums_dict:
            p = p.next
        start_head = p
        while p:
            if p.next and p.next.val in nums_dict:
                p.next = p.next.next
            else:
                p = p.next
        return start_head
```


## peter
-
```python
```


## charles
- data있는지 확인하기 위한 것에서 nums의 list에서 찾으면 timeout
- dictionary로 변경하고 찾으니 760 ms
- set으로 변경하고 찾으니 63 ms
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        d = set(nums)
        while head:
            if head.val in d:
                head = head.next
            else:
                break
        node = head.next
        prev = head
        while node:
            if node.val in d:
                prev.next = node.next
                node = node.next
            else:
                prev = node
                node = node.next
                
        return head
```

