# problem : 3439. Reschedule Meetings for Maximum Free Time I
- https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/description

```txt
You are given an integer eventTime denoting the duration of an event, where the event occurs from time t = 0 to time t = eventTime.

You are also given two integer arrays startTime and endTime, each of length n. These represent the start and end time of n non-overlapping meetings, where the ith meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most k meetings by moving their start time while maintaining the same duration, to maximize the longest continuous period of free time during the event.

The relative order of all the meetings should stay the same and they should remain non-overlapping.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event.


Example 1:

Input: eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]
Output: 2

Explanation:
Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the time [0, 2].

Example 2:

Input: eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]
Output: 6

Explanation:
Reschedule the meeting at [2, 4] to [1, 3], leaving no meetings during the time [3, 9].

Example 3:

Input: eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]
Output: 0

Explanation:
There is no time during the event not occupied by meetings.



Constraints:

1 <= eventTime <= 10^9
n == startTime.length == endTime.length
2 <= n <= 10^5
1 <= k <= n
0 <= startTime[i] < endTime[i] <= eventTime
endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].
```

# answer

## al
-
```python
# Runtime 44ms Beats 76.28%
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # 미팅 사이의 free time 계산, 최종 len(free_time) == n + 1
        n = len(startTime)
        free_time = [ startTime[i] - (endTime[i-1] if i != 0 else 0) for i in range(n) ]
        free_time.append(eventTime - endTime[n-1])

        max_free_time = 0
        # k 개의 미팅 시간을 조정할 수 있으므로, 연속된 k + 1 개의 최대값을 구하면 됨
        s = sum(free_time[0:k+1])
        for i in range(n - k + 1):
            max_free_time = max(max_free_time, s)
            if i < n - k:
                s = s - free_time[i] + free_time[i+k+1]

        return max_free_time
```


## peter
-
```python
```


## charles
- Window를 조정한다.   Runtime 91 ms Beats 20.48%
```python
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        start = 0
        emptyTime = []
        emptyLeftBlock = []
        block = 0
        for i in range(len(startTime)+1):
            if i == 0:
                if 0 < startTime[0]:
                    emptyTime.append(startTime[0])
                    emptyLeftBlock.append(0)
                block = 1
                continue
            if i == len(startTime):
                if endTime[i-1] < eventTime:
                    emptyTime.append(eventTime-endTime[i-1])
                    emptyLeftBlock.append(block)
                continue
            if endTime[i-1] < startTime[i]:
                emptyTime.append(startTime[i]-endTime[i-1])
                emptyLeftBlock.append(block)
                block = 1
                continue
            block += 1
        if not emptyTime:
            return 0
        # print(emptyTime,emptyLeftBlock)
        mx = emptyTime[0]
        start = 0
        end = 0
        block = 0
        for i in range(1,len(emptyTime)):
            if block + emptyLeftBlock[i] <= k:
                end = i
                block += emptyLeftBlock[i]
                mx += emptyTime[i]
            else:
                break
        result = mx
        # print('start index',start,'end index',end , 'block',block,'mx',mx)
        while start < len(emptyTime):
            # print('1start index',start,'end index',end , 'block',block,'mx',mx,'result',result)
            # 이 시점은 end까지는 포함된 것이다. 
            if end+1 < len(emptyTime) and block + emptyLeftBlock[end+1] <= k:
                end += 1
                block += emptyLeftBlock[end]
                mx += emptyTime[end]
                result = max(mx,result)
            else:  # end는 더이상 뒤로 갈수 없는 상황 , start를 조절
                if start+1 >= len(emptyTime):
                    break
                block -= emptyLeftBlock[start+1]
                mx -= emptyTime[start]
                start += 1
            # print('2start index',start,'end index',end , 'block',block,'mx',mx,'result',result)
        return result
```


