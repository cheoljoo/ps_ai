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
```python
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
