# problem : 1975. Maximum Matrix Sum
- https://leetcode.com/problems/maximum-matrix-sum/description/

---
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.


Example 1:

![ex1](https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex1.png)

Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
 Multiply the 2 elements in the first row by -1.
 Multiply the 2 elements in the first column by -1.

Example 2:

![ex2](https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex2.png)

Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
Multiply the 2 last elements in the second row by -1.


Constraints:
```
n == matrix.length == matrix[i].length
2 <= n <= 250
-10^5 <= matrix[i][j] <= 10^5
```
---

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
- math.inf로 데두리를 둠으로써 영억을 check할 필요가 없도록 만들어준다.   0 <= r < R 과 같이
- 처음 생각은 각 칸에서 오른쪽과 밑의 칸을 본다. 자신을 포함한 3칸을 보게 될때 , 음수의 갯수에 따라 다르게 처리를 해야 한다. 음수가 짝수개이면 짝수개의 음수를 모두 양수로 바꿔주면 된다.
  - 변경된 것이 없을때까지 loop를 동작시킨다.
- [[-1,1][1,-1]] 과 같은 것을 처리하기 위해서 , 4방향을 모두 본다. 이것도 변경된 것이 없을때까지 loop돌며서 찾아준다.
- 이렇게 했을때 답이 틀렸을뿐만 아니라,  중간에 matrix값들이 변하는 것을 보니 음수가 멀리 떨어져있더라도 2개의 음수만이 있다고하면 최종으로는 [[-1,1,1],[1,1,1],[1,1,-1]] -> [[1,-1,1],[1,1,1],[1,1,-1]] -> [[1,1,-1],[1,1,1],[1,1,-1]] -> [[1,1,1],[1,1,-1],[1,1,-1]] -> [[1,1,1],[1,1,-1],[1,1,-1]] -> [[1,1,1],[1,1,1],[1,1,1]] 와 같이 모두 양수로 변환할수 있다.
- 결론로는 음수의 수가 짝수이면 모두 더하면 되고 , 음수가 1개가 있다면 절대값이 제일 작은수 1개를 음수가 되는 matrix로 변환이 가능하다는 것이다.
```python
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        R = len(matrix)
        C = len(matrix[0])
        minusCount = 0
        minAbs = math.inf
        sm = 0
        for r in range(R):
            for c in range(C):
                v = matrix[r][c]
                if v < 0:
                    minusCount += 1
                absV = abs(v)
                minAbs = min(absV,minAbs)
                sm += absV
        if minusCount % 2 == 0:
            return sm
        return sm - (2*minAbs)

        


        # (3,3) 위치일때 양수이면 4개 주변의 수가 짝수의 음수가 있으면 모두 양수로
        # 홀수의 음수가 있으면 제일 큰 2개를 양수로 변환 , 남은 1개는 다음 loop에서 처리
        # 음수이면 1개가 음수이므로 홀수이면 모두 음수로 변환
        dir = [[0,1],[1,0]]  # ,[-1,0],[0,-1]]
        dirAll = [[0,1],[1,0],[-1,0],[0,-1],[0,0]]
        R = len(matrix)
        C = len(matrix[0])
        newMatrix = []
        newMatrix.append( [math.inf] * (C+2) )
        for r in range(R):
            newMatrix.append( [math.inf] + matrix[r] + [math.inf] )
        newMatrix.append( [math.inf] * (C+2) )
        matrix = newMatrix
        # print(matrix)
        flag = 1
        cnt = 1
        while flag:
            flag = 0
            # print(cnt,":",matrix)
            cnt += 1
            for r in range(1,R+1):
                for c in range(1,C+1):
                    minusDirAllCount = 0
                    for dr,dc in dirAll:
                        if matrix[r+dr][c+dc] < 0:
                            minusDirAllCount += 1
                    if minusDirAllCount == 2 or minusDirAllCount == 4:
                        for dr,dc in dirAll:
                            if matrix[r+dr][c+dc] < 0:
                                matrix[r+dr][c+dc] *= -1
                                flag = 1
                        # print('M',matrix[r][c],minusDirAllCount,matrix)
                    minusCount = 0
                    mn = math.inf
                    mnr = -1
                    mnc = -1
                    if matrix[r][c] >= 0:  # 오른쪽과 아래 2개만 보므로 minusCount 0 , 1 , 2만 가능  -> 볼때 전후좌우 4방향을 다 봐야 한다. 
                        for dr,dc in dir:
                            if matrix[r+dr][c+dc] < 0:
                                minusCount += 1
                        if minusCount == 2 or minusCount == 4:
                            for dr,dc in dir:
                                if matrix[r+dr][c+dc] < 0:
                                    matrix[r+dr][c+dc] *= -1
                                    flag = 1
                        elif minusCount == 1:
                            # 오른쪽과 밑의 것 중에 1개가 minus이다. 이 minus 값이 원래값보다 절대값이 크면 변경
                            if matrix[r][c] + matrix[r][c+1] < 0:
                                matrix[r][c] *= -1
                                matrix[r][c+1] *= -1
                                flag = 1
                            elif matrix[r][c] + matrix[r+1][c] < 0:
                                matrix[r][c] *= -1
                                matrix[r+1][c] *= -1
                                flag = 1
                        # minusCount 0은 변경 무
                    else:
                        minusCount += 1
                        for dr,dc in dir:
                            if 0 <= r+dr < R and 0<= c+dc < C and matrix[r+dr][c+dc] < 0:
                                minusCount += 1
                                if matrix[r+dr][c+dc] < mn:
                                    mn = matrix[r+dr][c+dc]
                                    mnr = r+dr
                                    mnc = c+dc
                        if minusCount == 3 :
                            if matrix[r][c+1] < matrix[r+1][c]:
                                matrix[r][c] *= -1
                                matrix[r][c+1] *= -1
                                flag = 1
                            else :
                                matrix[r][c] *= -1
                                matrix[r+1][c] *= -1
                                flag = 1
                        elif minusCount == 2 :
                            if matrix[r][c+1] < 0:
                                matrix[r][c] *= -1
                                matrix[r][c+1] *= -1
                                flag = 1
                            elif matrix[r+1][c] < 0:
                                matrix[r][c] *= -1
                                matrix[r+1][c] *= -1
                                flag = 1
                        elif minusCount == 1:
                            # 오른쪽과 밑의 것 중에 1개가 minus이다. 이 minus 값이 원래값보다 절대값이 크면 변경
                            if matrix[r+1][c] < matrix[r][c+1]:
                                if matrix[r][c] + matrix[r+1][c] < 0:
                                    matrix[r][c] *= -1
                                    matrix[r+1][c] *= -1
                                    flag = 1
                            else:
                                if matrix[r][c] + matrix[r][c+1] < 0:
                                    matrix[r][c] *= -1
                                    matrix[r][c+1] *= -1
                                    flag = 1
                        # minusCount 0은 변경 무
        print(matrix)
        sm = 0
        for r in range(1,R+1):
            for c in range(1,C+1):
                sm += matrix[r][c]
        return sm
```

