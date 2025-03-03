# problem : 2370. Longest Ideal Subsequence
- https://leetcode.com/problems/longest-ideal-subsequence/description

```txt
You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

 t is a subsequence of the string s.
 The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.

Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.
 

Example 1:

Input: s = "acfgbd", k = 2
Output: 4
Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.

Example 2:

Input: s = "abcd", k = 3
Output: 4
Explanation: The longest ideal string is "abcd". The length of this string is 4, so 4 is returned.
 

Constraints:

1 <= s.length <= 10^5
0 <= k <= 25
s consists of lowercase English letters.
```

# answer

## al
- 문자열 s 의 각 문자를 숫자로 변경하여 s_num 배열을 만들었다. ( a = 0 ... z = 25 )
- max_num 은 0(a) ~ 25(z) 인덱스에 각 문자에서 이상적인 문자열의 최대 길이를 저장했다.
- s_num 의 배열을 반복하면서 현재 문자 c 에서 인접할 수 있는 범위(max_num[max(0, c - k) : min(c + k + 1, 26)]) 내의 최대 값에 현재 문자를 포함(+1) 하여 현재 문자의 최대 길이로 저장 한다.
- max_num 에서 최대값을 리턴 했다.

```python
# Runtime 343ms Beats 93.68% / Memory 19.38 MB Beats 23.16% / Time approximately 2h
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        s_num = [ ord(c) - ord('a') for c in s ]
        max_num = [0] * 26
        # print(s_num)

        for c in s_num:
            max_num[c] = max(max_num[max(0, c - k) : min(c + k + 1, 26)]) + 1
            # print(c, max_num)

        return max(max_num)
```


## peter
- 
```python
```


## charles
- Runtime 3975 ms Beats 12.62% / Memory 21.45 MB Beats 21.72%
- ```python
  class Solution:
      def longestIdealString(self, s: str, k: int) -> int:
          # N**2 으로 풀면 timeout 일 것이다.
          # N으로 풀어야하는데 , windows는 중간에 빠질수 있어 고려가 안되고,
          # 방법 2 : 각 문자가 몇개씩인지를 보고 , windows를 k size로 a ~  z까지 옮기면서 그 합이 제일 큰 것을 답으로 하면 될 듯 하다.  (이건 말이 안되는구나. 연속된 두 수 간의 diff 임)
          # 방법 3 : 끝나는 alphabet을 기준으로 string을 저장한다. 끝나는 알파벳으로 끝나는 현재까지 가장 긴 string이 되는 것이다. 다음 새로운 글자가 올때 차이가 밖이라면 해당 문자의 가장 긴 것과 비교해서 삽입 , 차이 안에 들어올때는 기존 것은 놔두고 , 새로 추가되는 문제의 가장 긴 것보다 긴 것인지 check해서 삽입
          stringWithLastChar = [''] * 26
          stringWithLastChar[ord(s[0])-ord('a')] = s[0]
          for ch in s[1:]:
              longLengthStr = stringWithLastChar[ord(ch)-ord('a')]
              for index in range(26): # stringWithLastChar
                  longStr = stringWithLastChar[index]
                  if len(longStr) == 0:
                      if len(stringWithLastChar[ord(ch)-ord('a')]) == 0:
                          # stringWithLastChar[ord(ch)-ord('a')] = ch
                          if len(longLengthStr) == 0:
                              longLengthStr = ch
                  else:
                      diff = abs(ord(ch) - ord(longStr[-1]))
                      if diff <= k:
                          if len(longLengthStr) < len(longStr)+1:
                              longLengthStr = longStr + ch
              stringWithLastChar[ord(ch)-ord('a')] = longLengthStr
              # print(ch,stringWithLastChar)
          
          mx = 0
          for s in stringWithLastChar:
              mx = max(len(s),mx)
          return mx
  ```
