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
- 중복을 제거한 dmg 배열 dmg_list를 오름차순 정렬
- power를 Counter 로 변환하여 dmg_list[i] 값의 개수는 cnt[dmg_list[i]] 로 사용
- i번째 index까지 고려했을 때 총 데미지의 최대값을 m[i] 로 정의

- 1) i번째 값을 사용하지 않으면, m[i] = m[i-1]
- 2) i번째 값을 사용하고, m[i-1]에서 사용한 단일 최대 dmg < dmg_list[i] - 2 이면, m[i] = m[i-1] + (dmg_list[i] * cnt[i])
- 3) i번째 값을 사용하고, m[i-1]에서 사용한 단일 최대 dmg >= dmg_list[i] - 2 이면, dmg_list[k] < dmg_list[i] - 2 인 인덱스 k를 찾고 m[i] = m[k] + (dmg_list[i] * cnt[i])

- m[i] 를 계산할 때
조건(m[i-1] 에서 사용한 단일 dmg의 최대값 < dmg_list[i] - 2) 을 만족하지 못하면, 1)과 3) 중 큰 값을 m[i] 로 사용
조건을 만족하면 m[i-1] 에서 현재 dmg 총합을 추가

- m[i] 를 계산하기 위해서 이전에 사용한 최대 단일 dmg를 저장하여 비교할 필요가 있음
- max_single_dmg[i]를 m[i] 계산에 사용한 최대 단일 dmg 로 정의

```python
# Runtime 336ms Beats 97.29%

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        cnt = Counter(power)

        # 중복을 제거하고 오름차순으로 정렬된 상태의 dmg_list
        dmg_list = list(cnt.keys())
        # i번째 index까지 고려했을 때 총 데미지의 최대값을 m[i] 로 정의
        m = [0] * len(dmg_list)
        # 조건(m[i-1] 에서 사용한 단일 dmg의 최대값 < dmg_list[i] - 2)을 비교할 때 사용
        # m[i] 계산에 사용한 최대 단일 dmg 를 max_single_dmg[i] 로 정의
        max_single_dmg = [0] * len(dmg_list)

        m[0] = dmg_list[0] * cnt[dmg_list[0]]
        max_single_dmg[0] = dmg_list[0]

        for i in range(1, len(dmg_list)):
            if max_single_dmg[i-1] < dmg_list[i] - 2:
                m[i] = m[i-1] + (dmg_list[i] * cnt[dmg_list[i]])
                max_single_dmg[i] = dmg_list[i]
            else:
                last_max = 0
                if 2 <= i and dmg_list[i-2] < dmg_list[i] - 2:
                    last_max = m[i-2]
                elif 3 <= i and dmg_list[i-3] < dmg_list[i] - 2:
                    last_max = m[i-3]

                new_max = last_max + (dmg_list[i] * cnt[dmg_list[i]])
                if m[i-1] < new_max:
                    m[i] = new_max
                    max_single_dmg[i] = dmg_list[i]
                else:
                    m[i] = m[i-1]
                    max_single_dmg[i] = max_single_dmg[i-1]

        return m[-1]
```


## peter
- 
For each value a in the sorted array power:

If a−1 or a−2 do not exist, take a and move to the next.

Otherwise, choose between two paths:
	1️. Take a, exclude its related values (a−1, a−2), then continue with the next allowed value.
	2️. Skip a and move on.
	Take the path that gives the maximum total sum.


----

task: find maximum summation value from sorted array "power"

start
    set current_idx = 0
    set max_sum = 0
    prepare memo or record for each step

loop while current_idx < len(power)
    current_value = power[current_idx]

    # check if related (a-1, a-2) values exist in array
    related_exist = check(power, current_value - 1) or check(power, current_value - 2)

    if NOT related_exist:
        take current_value into sum
        goto next one
    else:
        # two possible branches
        branch_1: choose current_value
            → exclude any (a-1, a-2) values
            → goto next allowed index
            → compute sum_1
        branch_2: skip current_value
            → goto next index
            → compute sum_2

        choose max(sum_1, sum_2)
        store as best for this position
    end if
end loop

return maximum recorded sum
end



----


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


