# problem : 2579. Count Total Number of Colored Cells
- https://leetcode.com/problems/count-total-number-of-colored-cells/description/?envType=daily-question&envId=2025-03-05

- There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer n, indicating that you must do the following routine for n minutes:
    - At the first minute, color any arbitrary unit cell blue.
    - Every minute thereafter, color blue every uncolored cell that touches a blue cell.
- Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.

- ![](https://assets.leetcode.com/uploads/2023/01/10/example-copy-2.png)

- Return the number of colored cells at the end of n minutes.

# answer

## al
- 첫번째 풀이 n 이 2 이상일 때 f(n) = f(n - 1) + 4(n - 1) 즉, 이전 결과에 n - 1 을 4번 더 하면 셀이 한겹 추가된다.
- 두번째 풀이 행렬로 보면 중앙의 가장 긴 행의 개수는 2n - 1 이고, 그 위와 아래는 -2 씩 줄어서 1까지 존재한다.
- 즉, 2n - 1 은 한번, 2n - 3 부터 1까지 등차 -2 인 (n - 1)개의 행이 위, 아래 2개씩 존재한다.
- 첫번째 값 1, 마지막 값 2n - 3, 개수 n - 1 인 등차 수열의 합은 (n - 1)(1 + 2n - 3)/2
- 위, 아래 2개씩 존재하므로 (n - 1)(2n - 2)
- 여기에서 가장 긴 중앙의 개수 2n - 1 을 더하면
- 2n - 1 + (n - 1)(2n - 2) = 2(n - 1)^2 + 2n - 1
```python
# Runtime 155 ms Beats 20.22% / Memory 17.87 MB Beats 29.23%
class Solution:
    def coloredCells(self, n: int) -> int:
        res = 1
        for i in range(2, n + 1):
            res = res + 4 * (i - 1)
        return res

# Runtime 0 ms Beats 100% / Memory 17.70 MB Beats 46.19%
class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * (n - 1) ** 2 + 2 * n - 1
```


## peter
- 
```python
```


## charles
- Runtime 0 ms Beats 100.00% /  Memory 17.78 MB Beats 48.12%
```python
class Solution:
    def coloredCells(self, n: int) -> int:
        # 1
        # 1 + 4*1
        # 1 + 4*1 + 4*2
        # 1 + 4*1 + 4*2 + 4*3
        if n == 1:
            return 1
        c = n-1
        return 1+ (c*(c+1) // 2)*4
```
