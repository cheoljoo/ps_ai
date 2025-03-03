
# 퓨처 셀프 책 소개 부탁드립니다.

# problem : 1415. The k-th Lexicographical String of All Happy Strings of Length n
- https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/?envType=daily-question&envId=2025-02-19

```txt
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
- s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
- For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

 

Example 1:
Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

Example 2:
Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.

Example 3:
Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
 

Constraints:
1 <= n <= 10
1 <= k <= 100

```

# answer

## al
- happy string 의 첫번째 문자로 올 수 있는 문자는 'a', 'b', 'c' 3개, 그 이후 문자는 바로 앞자리에서 사용되지 않은 문자 2개.
- 길이가 n인 happy string 의 최대 개수는 3 * 2 ** (n - 1)개 이다.
- 첫번째 문자는 3진수, 그 이후 문자는 2진수 표현으로 볼 수 있다.
- 앞에서 결정된 문자에 따라 바로 뒷 문자의 표현이 제한된다. (char 딕셔너리 이용)
- 인덱스로 접근하기 위해서 k - 1 을 사용했다.
- 다음은 k 를 2진수와 3진수 혼합 표현으로 변경하는 과정이다.
- n - 1 번 2로 나눈 나머지들을 각각 스택(remain)에 저장 후, 3으로 나눈 나머지 값으로 첫번째 문자를 결정한다.
- 이전 문자(res[-1]) 를 key 로 char 딕셔너리에 접근하면 현재 사용할 수 있는 문자 2개의 배열에 접근할 수 있다.
- remain 스택의 값을 pop 하면서 문자를 결정한다.
```python
# Runtime 0ms Beats 100% / Memory 17.85 MB Beats 64.20% / Time approximately 1h
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_str_cnt = 3 * 2 ** (n - 1)
        if happy_str_cnt < k:
            return ""

        res = []
        remain = []
        char = { "a" : ["b", "c"], "b" : ["a", "c"], "c" : ["a", "b"] }
        base = ["a", "b", "c"]

        tmp = k - 1
        for _ in range(n - 1):
            remain.append(tmp % 2)
            tmp = tmp // 2

        tmp = tmp % 3
        res.append(base[tmp])

        for _ in range(n - 1):
            res.append(char[res[-1]][remain.pop()])

        return ''.join(res)
```


## peter
- 
```python
```


## charles
- BFS로 찾아가면서 n level에서의 k 번째 값을 찾으면 된다.
- Runtime 27 ms Beats 45.67% / Memory 18.08 MB Beats 34.67% / Time 33 min
```python
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # totalCountWithN = 3 * (2 ** (n-1))
        self.k = k
        self.n = n
        self.ans = ""
        ans = ""
        # 3**10이 될수 있지만, recursive로 해도 100까지만 call을 하면 되므로 상관없다.
        # 또 다른 방법은 각 level에서의 k 번째를 찾아야 하므로 
        # 각 level마다로 가는 BFS를 찾는 것도 방법이다.
        if k > 3 * (2**(n-1)):
            return ""
        q = ['a','b','c']
        nq = []
        while q:
            # print(q)
            for newString in q:
                # print('new',newString)
                if n == len(newString):
                    k -= 1
                    if k == 0:
                        return newString
                for ch in ['a','b','c']:
                    if newString[-1] != ch:
                        nq.append( newString + ch )
            q = nq
            nq = []
            if n > 10:
                return ""
        return ""
```
