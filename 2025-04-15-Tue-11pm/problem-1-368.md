# problem : 368. Largest Divisible Subset
- https://leetcode.com/problems/largest-divisible-subset/description/?envType=daily-question&envId=2025-04-06

- Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
  - answer[i] % answer[j] == 0, or
  - answer[j] % answer[i] == 0
- If there are multiple solutions, return any of them.

 

- Example 1:
  - Input: nums = [1,2,3]
  - Output: [1,2]
  - Explanation: [1,3] is also accepted.

- Example 2:
  - Input: nums = [1,2,4,8]
  - Output: [1,2,4,8]
 

- Constraints:
  - 1 <= nums.length <= 1000
  - 1 <= nums[i] <= 2 * 109
  - All the integers in nums are unique.


# answer

## al
- nums 를 정렬해서 큰 값을 작은 값으로 나눈 나머지가 0인지 확인한다. (작은 값을 큰 값으로 나누면 나머지가 0일 수 없다.)
- dp[i] 배열에 정렬된 nums 의 i번째 값을 최대 값으로 갖는 부분집합의 최대 원소 개수를 저장한다.
- pre_idx[i] 배열은 정렬된 nums 의 i번째 값을 나누어 떨어지게 만드는 부분집합의 최대 원소 개수에서 가장 큰 값의 index를 저장한다.
- dp[i] 의 값은 dp[pre_idx[i]] + 1 로 정의할 수 있다.
- for i 는 nums[i] 를 나눌 대상으로 잡는 기준 인덱스, for j 는 nums[j] 로 나눌 원소의 기준 인덱스, j 는 i 보다 작은 값으로 역순으로 계산
- 최대 원소 개수를 갖는 값의 인덱스를 max_idx 에 저장
- max_idx 를 시작으로 nums[max_idx] 를 통해 원소 값을 추적, pre_idx[max_idx] 를 통해 nums[max_idx] 이전의 최대 값을 갖는 인덱스를 알 수 있다.

```python
# Runtime 183 ms Beats 72.64% / Memory 18.12MB Beats 39.41%
# reference : https://leetcode.com/problems/largest-divisible-subset/solutions/684677/3-steps-c-python-java-dp-pen-paper-diagram/?envType=problem-list-v2&envId=pu0cgtyc

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n        # dp[i] : 정렬된 nums 의 i번째 값으로 끝나는 부분집합의 최대 원소 개수를 저장하는 배열
        pre_idx = [-1] * n  # pre_idx[i] : 정렬된 nums 의 i번째 값을 나누어 떨어지게 만드는 부분집합 중 가장 큰 값의 인덱스를 저장하는 배열
        max_idx = 0
        max_cnt = 0
        result = []

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1  # 최대 원소 개수 갱신
                        pre_idx[i] = j     # nums[i] 보다 작은 최대 원소의 index 저장

            if max_cnt < dp[i]:
                max_cnt = dp[i]
                max_idx = i

        while max_idx != -1:
            result.append(nums[max_idx])
            max_idx = pre_idx[max_idx]

        return result

##################################################################

# Time Limit Exceeded 47/49 testcases passed

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        max_len = 0
        res = []
        tmp = []

        def find_multiple(n):
            l = []
            for i in range(bisect.bisect(nums, n), len(nums)):
                if nums[i] % n == 0:
                    l.append(nums[i])
            return l

        def solv(list_num):
            nonlocal max_len
            nonlocal res
            nonlocal tmp

            for n in list_num:
                tmp.append(n)
                if max_len < len(tmp):
                    max_len = len(tmp)
                    res = tmp[:]
                l = find_multiple(n)
                solv(l)
                tmp.pop()

        solv(nums)
        return res

```


## peter
- 
```python
```


## charles
```python
```
