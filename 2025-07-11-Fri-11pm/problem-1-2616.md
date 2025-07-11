# problem : 2616. Minimize the Maximum Difference of Pairs
- https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/?envType=daily-question&envId=2025-06-13

```txt
You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.


Example 1:

Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5.
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.

Example 2:

Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= p <= (nums.length)/2
```

# answer

## al
- 저는 문제를 잘못 이해한 듯합니다.
- 예제 1번의 설명에서 차이가 최소가 되는 p개의 쌍 중에서 최대값을 찾았음
- 그래서 차이값이 최소가 되는 쌍을 순서대로 p개 고르면 p번째 차이값이 최대가 되므로 그렇게 문제를 접근했는데 테스트 케이스 후반부에 더 작은 값이 정답이네요??
```python
# Wrong Answer 1343 / 1582 testcases passed
# nums = [1,1,0,3], p = 2
# Expected : 2
# But Output : 3
'''
nums = [0, 1, 1, 3]
diff = [1, 0, 2, 1000000001]
min_idx = 1
next pair(i) = 2
clear!!
nums = [0, -1, -1, 3]
diff = [1, 1000000001, 1000000001, 1000000001]
next pair(j) = 3
update diff!!!
diff = [3, 1000000001, 1000000001, 1000000001]
'''
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()
        diff = [ nums[i + 1] - nums[i] for i in range(len(nums) - 1) ]
        diff.append(10 ** 9 + 1)

        for cnt in range(p):
            min_idx = diff.index(min(diff))
            if cnt == p - 1:
                break

            # find pair
            for i in range(min_idx + 1, len(nums)):
                if nums[i] >= 0:
                    break

            # clear pair value
            nums[min_idx] = nums[i] = -1
            diff[min_idx] = diff[i] = 10 ** 9 + 1

            # find next value
            j = i + 1
            for j in range(i + 1, len(nums)):
                if nums[j] >= 0:
                    break

            if min_idx > 0:
                # find prev value
                for k in range(min_idx - 1, -1, -1):
                    if nums[k] >= 0:
                        break
                # update diff
                if j < len(nums) and nums[j] >= 0:
                    diff[k] = nums[j] - nums[k]
                else:
                    # clear
                    diff[k] = 10 ** 9 + 1

        return diff[min_idx]
```


## peter
- 
```python
```


## charles
- 제가 제일 싫어하는 문제 유형이네요.. 저는 도저히 못 품.
- index가 겹쳐도 되는 경우
  - ```python
    class Solution:
        def minimizeMax(self, nums: List[int], p: int) -> int:
            # 2개의 값의 차이가 가장 작은 p 개를 골라서 , 그중에 가장 큰 값은?
            # 10**5 이므로 N^2을 하면 안될 것으로 보인다.
            # 일단 sort를 하여 각 요소에서 가장 작은 값들을 구한다. 언제까지 구할 것인가?
            # 가장 작은 값을 구하는 것이므로 [1,2,2,4]라고 할때
            # 1. 우선 p개의 diff를 채운다.   2. p개의 diff중 제일 큰 값보다 크면 그 뒤는 당연히 더 크므로 stop
            nums.sort()
            hq = []  # max heapq
            mx = nums[-1]
            if p == 0:
                return 0
            # print(nums)
            for i in range(len(nums)):
                for n in range(i+1,len(nums)):
                    diff = abs(nums[i] - nums[n])
                    if len(hq) < p:
                        heappush(hq,-diff)
                        # mx = max(mx,diff)
                    elif (-hq[0]) > (diff):   # 제일 큰 값보다 작으면
                        heappop(hq)
                        heappush(hq,-diff)
                    else:  # 제일 큰 값보다 크거나 같으면 stop
                        break
                    # print(i,n,nums[i],nums[n],diff,hq)
            return min(hq) * -1
    ```
- index가 겹치지 않아야 하는 경우에 대한 해답 (copy)
  - ```python
    def minimizeMax(nums, p):
        nums.sort()
    
        def can_form_pairs(max_diff):
            count = 0
            i = 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= max_diff:
                    count += 1
                    i += 2  # 두 개의 인덱스를 사용했으므로 건너뜀
                else:
                    i += 1
            return count >= p
    
        left, right = 0, nums[-1] - nums[0]
        answer = right
    
        while left <= right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
    
        return answer
    ```
