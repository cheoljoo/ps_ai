# problem : 3186. Maximum Total Damage With Spell Casting
- https://leetcode.com/problems/maximum-total-damage-with-spell-casting/?envType=problem-list-v2&envId=pu0cgtyc

```txt
A magician has various spells.

You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.

It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.

Each spell can be cast only once.

Return the maximum possible total damage that a magician can cast.


Example 1:
Input: power = [1,1,3,4]
Output: 6

Explanation:
The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.


Example 2:
Input: power = [7,1,6,6]
Output: 13

Explanation:
The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.


Constraints:

1 <= power.length <= 10^5
1 <= power[i] <= 10^9
```

# answer

## al
-
```python
```


## peter
- 
```python
```


## charles
- Runtime 563 ms Beats 49.44%
- NlogN
```python
# 1,2,3,4,5,6,7,8  이 여러개가 있다고하면  [숫자,횟수] 를 숫자로 sort하여 가지고 있으면 된다.
# N 이 있으면 N의 값을 포함할때 => N*횟수 , N+3의최대값
# N을 포함하지 않을때 => N+1의 최대값 (바로 전까지의 최대값)
# N+3의 최대값 => bisect.bisect_right(sortedPower, num+2) 의 index가 들어갈 위치에 있는 것이 num+3 의 값이 됨.
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        powerCounter = Counter(power)
        reverseSortedPower = sorted(powerCounter,reverse=True)
        sortedPower = list(reversed(reverseSortedPower))
        # print(sortedPower)
        # print(reverseSortedPower)
        dpMax = {}
        prevMax = 0
        for num in reverseSortedPower:
            count = powerCounter[num]
            # print(bisect.bisect_right(sortedPower, num+2), num*count , dpMax.get(num+3,prevMax) , dpMax.get(num+2,prevMax) , dpMax.get(num+1,prevMax))
            index = bisect.bisect_right(sortedPower, num+2)
            if index >= len(sortedPower):
                whenSelected = 0
            else:
                whenSelected = dpMax[sortedPower[index]]
            dpMax[num] = max(num*count + whenSelected , prevMax)
            prevMax = dpMax[num]
            # print('dpMax',dpMax)
        return prevMax

```
