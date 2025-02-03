# problem
- https://leetcode.com/problems/the-number-of-beautiful-subsets/

```txt
You are given an array nums of positive integers and a positive integer k.
A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.
Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.



Example 1:
Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

Example 2:
Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].


Constraints:
    1 <= nums.length <= 20
    1 <= nums[i], k <= 1000
```

# answer

## al
- 모든 부분집합의 개수를 찾고, 두 값의 차이가 k인 짝(pair)을 찾음
  짝이 포함된 부분집합의 개수를 모든 부분집합의 개수에서 빼고,
  중복으로 뺀 부분을 보정해가는 방식으로 풀이를 계획함
- pair 에서 2개를 선택한 보정 뿐만 아니라 모든 경우의 수에 대한 보정이 필요한 것으로 보임
- 계획한 풀이 방법으로 풀 수 있는지 명확하지 않아 중단함

```python
# Wrong Answer 1205/1308 testcases passed


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        pair = []
        cnt_num = len(nums)

        for a, b in list(combinations(nums, 2)):
            if abs(a - b) == k:
                pair.append((a, b))

        #print(pair)
        # all subsets
        cnt = 2 ** cnt_num - 1
        #print(cnt)
        # Remove subsets that satisfy the condition (duplicately)
        cnt -= (2 ** (cnt_num - 2)) * len(pair)
        #print(cnt)

        # Adds duplicates removed
        add_cnt = 0
        for a, b in list(combinations(pair, 2)):
            union = set(a) | set(b)
            cnt += 2 ** (cnt_num - len(union))
            add_cnt += 1

        # Adjust the entire set to be removed only once
        rm_cnt = len(pair)
        if rm_cnt > 0:
            cnt += (rm_cnt - add_cnt - 1)

        return int(cnt)

```


## peter
- 

```python

```


## charles
- idea
  - n의 max가  20개이면 , 2**n = 1M 이다.  이는 모든 가능한 combination이 가능하다는 것이다.
- complexity : O(2^N)
- algorithm :
  - combination을 구해서 각기 subset이 beautiful한지를 check
- alternatives :
  - 모든 것을 check하기에는 시간이 많이 걸리므로 각기 combination을 구할때 이미 beautiful이 아니면 중단함으로 전체 loop수를 줄일수 있다.  Runtime: 2596ms
  - [source code](./2025/the-number-of-beautiful-subsets-2597---medium--python-2.py)
- [ ] recursive 가 아닌 것으로 직접 작성해봐야함.

```python
# Runtime 8401 ms Beats 10.36% / Memory 157.14 MB Beats 9.71%
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        subsets = []
        for i in range(2,len(nums) + 1):
            subsets.extend(itertools.combinations(nums, i))
        # print("Subsets:", subsets)
        ans = len(nums)
        for subset in subsets:
            d = set()
            for item in subset:
                if item - k not in d:
                    d.add(item)
                else:
                    break
            else:
                # for 문에서는 break로 빠지지 않는 것은 for else로 처리되게 된다.
                # print(subset,'ans',ans,'k',k)
                ans += 1
        return ans
        d = {}
        N = len(nums)
        ans = N
        total = 2**N - 1
        for n in nums:
            d[n] = 0
        pairs = {}
        for n in nums:
            if n+k in d:
                pairs[n] = n+k
        print('pairs',pairs)
        P = len(pairs)
        if N <= 2:
            total -= P
        else:
            prev = 0
            pCnt = 0
            for p,v in pairs.items():
                if prev == p:
                    pCnt += 1
                # else:
                #     pCnt += 1
                total -= (2**(N-2-pCnt))
                print('total',total,'pCnt',pCnt,'(2**(N-2-pCnt))',(2**(N-2-pCnt)),prev,p,v)
                prev = v
            # ex1) 2,4,6 , (2,4) , (4,6) , (2,4,6)
            # 처음에는 (2,4) 에서 뒤에 올수 있는 것은 null , 6이 올수 있다.
            # 두번째인 (4,6) 에서는 앞의 null , 2가 올수 있는데 , 이 2는 겹치게 되는 것이다.
            # ex2)  2,4,6,10 이라고 하면
            # 처음의 (2,4) 에 대해서는 6,10으로 만들수 있는 모든 것이 곱해지고
            # 두번째인 (4,6)에 대해서는 2,10으로 된 것이 만들어지나, 2는 첫번째에서 한 것이므로 제외를 해주어얗낟.
            # pairs가 여래 일때 , 첫번째는 빼는 것 없지만, 2번째부터는 앞의 한개씩이 빠지게 되는 것으로 계산을 해주어야 한다. (p)
            #
            # [4,2,5,9,10,3] 일때
            # pairs {2: 3, 3: 4, 4: 5, 9: 10}
            # 앞뒤가 겹치지 않을때는 줄일 필요가 없다.
            #
            # permutation으로 계산을 하면 될 듯...  20! or 2**20 인데 2**20 이 훨씬 작다.
            #
        return total
```
