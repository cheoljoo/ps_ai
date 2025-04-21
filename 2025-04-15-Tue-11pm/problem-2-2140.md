# problem : 2140. Solving Questions With Brainpower
- https://leetcode.com/problems/solving-questions-with-brainpower

- You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

- The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

- For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
  - If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
  - If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.
 

- Example 1:

- Input: questions = [[3,2],[4,3],[4,4],[2,5]]
- Output: 5
- Explanation: The maximum points can be earned by solving questions 0 and 3.
  - Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
  - Unable to solve questions 1 and 2
  - Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.

- Example 2:

- Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
- Output: 7
- Explanation: The maximum points can be earned by solving questions 1 and 4.
  - Skip question 0
  - Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
  - Unable to solve questions 2 and 3
  - Solve question 4: Earn 5 points
Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.
 

- Constraints:

  - 1 <= questions.length <= 10^5
  - questions[i].length == 2
  - 1 <= pointsi, brainpoweri <= 10^5

# answer

## al
- m[i] : i번째 문제에서 시작 했을 경우 최대 점수를 저장한다.
- 문제의 개수 n 개일 때 m[n - 1] 은 마지막 문제를 풀었을 때 획득할 수 있는 점수이다.(questions[n - 1][0])
- 마지막 문제를 풀었을 때 획득할 수 있는 최고 점수가 고정되어 있으므로, 이를 기반으로 역순으로 확인하면서 풀이한다.
- 문제를 대할 때 푸는 경우(solv), 풀지 않는 경우(skip)를 구분하여 계산한다.
- 문제를 푸는 경우 최대 점수는 그 문제의 점수(questions[i][0]) + 다음으로 풀 수 있는 문제부터 시작했을 경우의 최대 점수 m[i + questions[i][1] + 1]
- 문제를 풀지 않는 경우 최대 점수는 다음 문제의 최대 점수 m[i + 1]
- i번째 문제에서 시작했을 때 최대 점수(m[i]) 는 i 번째 문제를 푸는 경우와 풀지 않는 경우 중 큰 값을 저장한다.
- 0번째 문제에서 시작하는 경우의 최대 점수 (m[0])가 정답이 된다.
```python
# Runtime 67 ms Beats 79.52% / Memory 60.84MB Beats 62.77%

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        m = [0] * n
        m[n - 1] = questions[n - 1][0]

        for i in range(n - 2, -1, -1):
            solv = questions[i][0]
            next_question = i + questions[i][1] + 1
            if next_question < n:
                solv += m[next_question]
            skip = m[i + 1]
            m[i] = max(solv, skip)

        return m[0]
```


## peter
- 
```python
```


## charles
```python
```
