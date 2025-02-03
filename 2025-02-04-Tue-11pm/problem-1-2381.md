# problem
- https://leetcode.com/problems/shifting-letters-ii/

```txt
You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.


Example 1:
Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".

Example 2:
Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
Output: "catz"
Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".


Constraints:
    1 <= s.length, shifts.length <= 5 * 104
    shifts[i].length == 3
    0 <= starti <= endi < s.length
    0 <= directioni <= 1
    s consists of lowercase English letters.
```

# answer

## al
- shifts 에서 주어진 범위 shift 를 누적, 최종 결과를 s에 적용하여 리턴하도록 구성
- # (1) 과 같이 적용할 index 에 동일한 방향을 더해주는 과정을 수행했을 때 시간 초과 발생
  이 부분을 개선할 방법을 고민하였으나, 적절한 방법을 찾지 못함
- 문제의 Hint 2 를 참고하여 start index 에 방향을 더하고, end + 1 index 에 방향을 빼는 방법 적용
  모두 적용 후 각 index 값을 누적해서 더하면 의도한 데이터를 구성할 수 있음
- 누적한 shift 값을 알파벳 개수로 나눈 나머지를 s의 각 index 에 적용
  rotation 이 필요한지 확인 후 결과 데이터 구성
```python
# Time Limit Exceeded 32/39 testcases passed

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        accumulate_diff = [0] * len(s)
        for start, end, d in shifts:
            if d == 0:
                d = -1
            # (1)
            for i in range(start, end + 1):
                accumulate_diff[i] += d

        #print(accumulate_diff)
        res = []
        alpha_cnt = ord('z') - ord('a') + 1

        for i, c in enumerate(s):
            r = ord(s[i]) + accumulate_diff[i] % alpha_cnt
            if r > ord('z'):
                r -= alpha_cnt
            elif r < ord('a'):
                r += alpha_cnt
            res.append(chr(r))

        #print(res)
        return ''.join(res)


# Runtime 60 ms Beats 58.51% /  Memory 41.31 MB Beats 64.81%

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        accumulate_diff = [0] * len(s)
        for start, end, d in shifts:
            if d == 0:
                d = -1
            accumulate_diff[start] += d
            if end + 1 < len(accumulate_diff):
                accumulate_diff[end + 1] -= d

        for i in range(1, len(accumulate_diff)):
            accumulate_diff[i] += accumulate_diff[i - 1]
        #print(accumulate_diff)

        res = []
        alpha_cnt = ord('z') - ord('a') + 1

        for i, c in enumerate(s):
            r = ord(s[i]) + accumulate_diff[i] % alpha_cnt
            if r > ord('z'):
                r -= alpha_cnt
            elif r < ord('a'):
                r += alpha_cnt
            res.append(chr(r))

        #print(res)
        return ''.join(res)
```


## peter
- 
```python
```


## charles
- first idea
  - brute force
  - use index and set the count in value of index and change character once.
  - get all boundaries (0,15) (5,20) (10,40) -> (0:1,16:-1) (5:1,21:-1) (10:1,41:-1) 로 하여 계산을 한다.
    - 이 의미는 dict로 가지고 있으면 되며 , for i in range(len(s)) 를 할때 각 위치의 값이 dict가 있으면 해당 값을 더해주어 각 index에서 몇번을 left/right shift해야하는지 알수 있게 해주는 것이다.
- brute force : Time Limit Exceeded 32 / 39 testcases passed
  - O(N) Runtime 60 ms Beats 58.18% /  Memory 41.24 MB Beats 86.06%
- complexity : O(N)
- algorithm :
  - pins 는 각 index에서 값이 증가하거나 감소하는 것이다. forward  기준으로보면 start는 당연히 증가를 하는 것이고, end까지는 유지 되다가 , end+1 부터 증가되었던 부분이 감소하게 되는 것이므로 end+1로 하였다. end는 len(s)까지 올수 있으므로 계산의 편의를 위해서 pins의 size는 len(s)+1로 잡은 것이다. 위치의 계산은 % 연산으로 사용하여 26개의 circle을 돌게 한다고 생각하면 된다.  'a' 로터의 간격(gap) 을 구하면 된다.  O(N)
```python
# Runtime 60 ms Beats 58.18% /  Memory 41.24 MB Beats 86.06%

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pins = [0] * (len(s) + 1)
        sl = list(s)
        for start,end,dir in shifts:
            if dir == 1:  # forward : +1
                pins[start] += 1
                pins[end+1] -= 1
            else: # backward : -1
                pins[start] -= 1
                pins[end+1] += 1
        # print('pins',pins)
        shift = 0
        size = ord('z') - ord('a') + 1  # 26
        for i in range(len(s)):
            if pins[i] != 0:
                shift += pins[i]
            curPos = ord(sl[i]) - ord('a')
            gap = (curPos + shift) % size
            # print('i',i,'shift',shift,'sl[i]',sl[i],'curPos',curPos,'gap',gap,size)
            sl[i] = chr(ord('a')+gap)
        return ''.join(sl)
```

