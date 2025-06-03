# problem : 2929. Distribute Candies Among Children II
- https://leetcode.com/problems/distribute-candies-among-children-ii/description/?envType=daily-question&envId=2025-06-01

```txt
You are given two positive integers n and limit.
Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.



Example 1:
Input: n = 5, limit = 2
Output: 3
Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).

Example 2:
Input: n = 3, limit = 3
Output: 10
Explanation: There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).


Constraints:
1 <= n <= 10^6
1 <= limit <= 10^6
```

# answer

## al
```python
```


## peter
- 
```python
```


## charles
```python
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # 3명이니 (?,?,?) 에서 같은게 0개 (세개 모두 다름)이면 6 , 1개 같으면(2개는 같음) 3 , 모두 같으면 1
        # limit 를 n//3 부터 limit까지 처리 , limit 1, 2, 3 일때 처리
        # n=8,limit=4이면 , limit 2 -> 불가 , limit 3이면 (3,3,2) , limit 4이면 (4,a,b)  a+b=4가 되어야 한다. 모두 다른 4개 + 1개 같음 1개
        # n=15 , limit=10, limit 5 -> 15%5==3이므로 1개 , limit 6 -> 15%6<3 and (6,a+b=9) a=(6,5)  , limit 7-> 15%7<3 and (7,a+b=8) a=(7,6,5,4)  갯수가 수식으로 표현됨 limit와 같으면 7자가 1쌍 (3), 6,5는 모두 다름 (6), 4는 4자가 1쌍 (3)
        #                  limit 9 -> (9,a+b=6) a=(3,4,5,6)    limit 10 -> (10,a+b=5) a=(3,4,5)
        # O(N)일 것임 , n-limit >= limit 와 n-limit<limit일때 구분

        # if n > 3*limit:    n=1 , limit=3 예 때문에 주석처리
        #     return 0
        if n == 3*limit :
            return 1
        ans = 0
        minLimit = max(n // 3,1)
        maxLimit = min(n,limit)
        for l in range(minLimit,maxLimit+1):
            # print(l)
            if l*3 < n:
                continue
            elif l*3 == n:
                ans += 1
            else:   # minLimit*3 > n
                ab = n - l
                minNum  = (ab+1)//2
                maxNum = min(l,ab)
                count = maxNum - minNum + 1
                ans += count * 6
                # print('ab',ab,'l',l,'ans',ans,'min',minNum, 'max',maxNum)
                if ab % 2 == 0:
                    ans -= 3
                if ab >= l:
                    ans -= 3
            # print(l,ans)

        return ans
```
