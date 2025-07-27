# problem : 1695. Maximum Erasure Value
- https://leetcode.com/problems/maximum-erasure-value/description/?envType=daily-question&envId=2025-06-13

```txt
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).



Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].

Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
```

# answer

## al
- 양의 정수 nums 배열이 주어지면, 연속적인 subarray를 지울 수 있고, subarray 의 값은 유일해야 한다.
- 삭제한 subarray의 모든 요소의 합을 score 라고 할 때 하나의 subarray만 삭제해서 최대 score 를 리턴하는 문제

- subarray 에 포함되어 있는 값인지(key), 어느 인덱스(value)에 존재하는지를 저장하는 dict 자료형 sub_arr 를 사용
- subarray 의 시작과 끝 인덱스를 start, end 로 정하고 end 를 증가시켜 가면서 조건 확인
- subarray 에 포함되어 있지 않는 값이면 sub_arr에 값 추가, score 에 값 추가, max_score 확인
- subarray 에 포함된 값이면 기존 값의 위치 다음으로 시작 위치 조정, score 값 조정, 삭제된 sub_arr 값 조정을 진행
```python
# Runtime 255ms Beats 25.99% / Memory 29.84MB Beats 5.81%

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = nums[0]
        score = nums[0]
        start = end = 0
        sub_arr = {nums[0]: 0} # sub_arr[value] = index
        psum = [0] * len(nums)

        for i in range(1, len(nums)):
            psum[i] = psum[i - 1] + nums[i - 1] # psum[i] = sum(nums[0:i])

            end = i
            t = nums[end]
            if t not in sub_arr.keys():
                score += t
                max_score = max(max_score, score)
                sub_arr[t] = i
            else:
                new_start = sub_arr[t] + 1 # next index
                score = score - (psum[new_start] - psum[start]) + t
                #max_score = max(max_score, score)
                for j in range(start, new_start):
                    del sub_arr[nums[j]]
                start = new_start
                sub_arr[t] = i # index update
            #print(f'i = {i}, sub_arr = {sub_arr}, t = {t}, start = {start}, end = {end}, nums = {nums}')

        return max_score
```


## peter
- 
```python
```


## charles
- window move : Runtime 1742 ms Beats 7.53%
```python
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sm = 0
        mem = set()
        sumMem = 0
        pos = {}
        start = 0
        # print("nums:",nums)
        for i,v in enumerate(nums):
            if v not in mem:
                mem.add(v)
                sumMem += v
                pos[v] = i
            else :
                # print("i:",i,"v:",v,"sm:",sm,"sum(mem):",sum(mem),"start:",start,"pos[v]:",pos[v],mem,end=" ")
                # sm = max(sm , sum(mem))
                sm = max(sm,sumMem)
                while start < pos[v]:
                    mem.remove(nums[start])
                    sumMem -= nums[start]
                    start += 1
                
                start = pos[v] + 1
                pos[v] = i
                # print(nums[start:i+1])
        # sm = max(sm , sum(mem))    
        sm = max(sm,sumMem)
        return sm
```
