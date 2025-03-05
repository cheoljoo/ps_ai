# problem : 2375. Construct Smallest Number From DI String
- https://leetcode.com/problems/construct-smallest-number-from-di-string/description

```txt
You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].

Return the lexicographically smallest possible string num that meets the conditions.


Example 1:

Input: pattern = "IIIDIDDD"
Output: "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.

Example 2:

Input: pattern = "DDD"
Output: "4321"
Explanation:
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.
 

Constraints:

1 <= pattern.length <= 8
pattern consists of only the letters 'I' and 'D'.
```

# answer

## al
- DFS 를 사용, 작은 값부터 사용하여 조건을 만족하는 값을 찾았다.
- possible_n 배열에 1 ~ 9 값을 순서대로 저장 후 사용한 숫자는 0으로 초기화
- 다음 숫자를 찾기 위해 pattern 의 값에 따라 값의 범위를 지정([start:end])하고, 작은 값 부터 선택 후, dfs() 호출하여 과정 반복
- 조건을 만족하는 값이 없을 경우 사용했던 값을 복원 후 다음 값을 시도하는 방식
```python
# Runtime 0ms Beats 100% / Memory 17.77 MB Beats 59.56% / Time approximately 1h
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def dfs(pattern, possible_n, out, i):
            if len(pattern) < len(out):
                return True

            start = 0
            end = 9
            if i > 0:
                if pattern[i - 1] == 'I':
                    start = int(out[-1])
                else:
                    end = int(out[-1]) - 1

            for n in possible_n[start:end]:
                if n == 0:
                    continue
                out.append(str(n))
                possible_n[n - 1] = 0
                if dfs(pattern, possible_n, out, i + 1):
                    return True
                out.pop()
                possible_n[n - 1] = n

            return False

        possible_n = [ i + 1 for i in range(9) ]
        out = []

        dfs(pattern, possible_n, out, 0)

        return ''.join(out)
```


## peter
- 
```python
```


## charles
- Runtime 0 ms Beats 100.00% / Memory 17.69 MB Beats 85.08%
- ```python
  class Solution:
      def smallestNumber(self, pattern: str) -> str:
          startNumber = 1
          # startNumber는 제일 앞의 D의 갯수 + 1 개 입니다.
          for ch in pattern:
              if ch == 'I':
                  break
              else:
                  startNumber += 1
          isCatchD = False
          dCount = 0
          D = [0] * len(pattern)
          for index,ch in enumerate(reversed(pattern)):
              if ch == 'D':
                  dCount += 1
              else :
                  D[len(pattern)-1-index] = dCount
                  dCount = 0
          # print('startNumber',startNumber)
          # print('D',D)
          
          # D : 뒤에 얼마나 D가 있는지
          # 'D'를 만나면 1개씩 죽이면 되고 , 
          # 'I'를 만나면 전의 제일 큰 수에 D[] + 1 을 더한다.
          if startNumber < 1:
              startNumber = 1
          ans = str(startNumber)
          num = startNumber
          mx = startNumber
          for index,ch in enumerate(pattern):
              if ch == 'D':
                  num -= 1
                  ans += str(num)
              else:
                  num = mx + D[index] + 1
                  ans += str(num)
                  mx = num
          return ans
  ```
