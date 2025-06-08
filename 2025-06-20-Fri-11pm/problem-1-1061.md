# problem : 1061. Lexicographically Smallest Equivalent String
- https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/?envType=daily-question&envId=2025-06-05

```txt
You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.

Example 1:

Input: s1 = "parker", s2 = "morris", baseStr = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
The characters in each group are equivalent and sorted in lexicographical order.
So the answer is "makkek".

Example 2:

Input: s1 = "hello", s2 = "world", baseStr = "hold"
Output: "hdld"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".

Example 3:

Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
Output: "aauaaaaada"
Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".


Constraints:

1 <= s1.length, s2.length, baseStr <= 1000
s1.length == s2.length
s1, s2, and baseStr consist of lowercase English letters.
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
- Runtime 3ms Beats 92.21% / Memory 17.86MB Beats 64.77%
```python
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        alphabetDict = {}
        minMatched = [ chr(c) for c in range(ord('a'),ord('z')+1)]
        for c in range(ord('a'),ord('z')+1):
            alphabetDict[chr(c)] = set([chr(c)])
        for i in range(len(s1)):
            a = s1[i]
            b = s2[i]
            aIndex = ord(a)-ord('a')
            bIndex = ord(b)-ord('a')
            aMinMatched = minMatched[aIndex]
            bMinMatched = minMatched[bIndex]
            # print(a,b,aIndex,bIndex,'minMatched',aMinMatched,bMinMatched)
            if aMinMatched == bMinMatched:
                continue
            elif aMinMatched > bMinMatched:
                minIndex = ord(aMinMatched)-ord('a')
                minMatched[minIndex] = bMinMatched  # a 자리에 b를 넣는다. 이후 alphabetDict에도 a 자리 안에 있는 것들을 모두 가서 b로 바꿔준다. 그리고, a는 set() 으로 바꾼다(clear). 
                for ac in alphabetDict[aMinMatched]:
                    alphabetDict[bMinMatched].add(ac)
                    minMatched[ord(ac)-ord('a')] = bMinMatched
                alphabetDict[aMinMatched] = set()
            else:
                minIndex = ord(bMinMatched)-ord('a')
                minMatched[minIndex] = aMinMatched  # a 자리에 b를 넣는다. 이후 alphabetDict에도 b 자리 안에 있는 것들을 모두 가서 a로 바꿔준다. 그리고, b는 set() 으로 바꾼다(clear). 
                for ac in alphabetDict[bMinMatched]:
                    alphabetDict[aMinMatched].add(ac)
                    minMatched[ord(ac)-ord('a')] = aMinMatched
                alphabetDict[bMinMatched] = set()
            # self.printA(a,b,alphabetDict,minMatched)
        ans = ''
        for bc in baseStr:
            ans += minMatched[ord(bc) - ord('a')]
        return ans
    def printA(self,a,b,alphabetDict,minMatched):
        pp = {}
        for c in alphabetDict:
            if len(alphabetDict[c]) != 1:
                pp[c] = alphabetDict[c]
        print(a,b,pp,minMatched)
```
