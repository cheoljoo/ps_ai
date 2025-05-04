# problem : 1976. Number of Ways to Arrive at Destination
- https://leetcode.com/problems/number-of-ways-to-arrive-at-destination

- You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

- You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

- Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

- Example 1:
    - ![](https://assets.leetcode.com/uploads/2025/02/14/1976_corrected.png)
    - Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    - Output: 4
    - Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
    - The four ways to get there in 7 minutes are:
        - 0 ➝ 6
        - 0 ➝ 4 ➝ 6
        - 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
        - 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

- Example 2:
    - Input: n = 2, roads = [[1,0,10]]
    - Output: 1
    - Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.
 
- Constraints:
    - 1 <= n <= 200
    - n - 1 <= roads.length <= n * (n - 1) / 2
    - roads[i].length == 3
    - 0 <= ui, vi <= n - 1
    - 1 <= timei <= 109
    - ui != vi
    - There is at most one road connecting any two intersections.
    - You can reach any intersection from any other intersection.

# answer

## al
- graph 의 index는 출발지점, 값은 dict(key는 도착 지점, value는 걸리는 시간)
- 가장 짧은 시간이 걸리는 경로의 개수를 찾는 문제로 모든 경로를 찾아야 할 것 같아 bfs(우선 순위 적용), dfs 로 시도했으나 둘 다 시간 초과 발생
```python
# Runtime 12 ms Beats 92.77% / Memory 24.21MB Beats 95.86%
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        ways  = [ {} for _ in range(n) ]
        graph = [ {} for _ in range(n) ]
        min_time = [float('inf')] * n
        min_time[0] = 0

        for u, v, t in roads:
            graph[u][v] = t
            graph[v][u] = t

        hq = [(0, 0)] # (time, node)
        while hq:
            time, node = heapq.heappop(hq)
            if min_time[node] < time:
                continue

            for next_node, t in graph[node].items():
                nt = time + t
                if min_time[next_node] <= nt:
                    continue

                min_time[next_node] = nt
                heapq.heappush(hq, (nt, next_node))

        def countWays(node, time):
            nonlocal ways
            if node == 0 and time == 0:
                return 1
            cnt = 0
            for prev_node, t in graph[node].items():
                pt = time - t
                if pt < min_time[prev_node]:
                    continue
                if pt in ways[prev_node]:
                    cnt += ways[prev_node][pt]
                else:
                    ret = countWays(prev_node, pt)
                    ways[prev_node][pt] = ret
                    cnt += ret

            return cnt

        return countWays(n - 1, min_time[n - 1]) % (10 ** 9 + 7)

# Time Limit Exceeded 17/56 testcases passed
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        min_time = 10 ** 9 * 200 * 199 / 2 + 1
        cnt = 0
        graph = [ {} for _ in range(n) ]

        for u, v, t in roads:
            graph[u][v] = t
            graph[v][u] = t

        def dfs(node, time, passed):
            nonlocal min_time
            nonlocal cnt

            if node == n - 1:
                if min_time > time:
                    min_time = time
                    cnt = 1
                elif min_time == time:
                    cnt += 1
                return

            for v, t in graph[node].items():
                if v in passed:
                    continue
                if time + t > min_time:
                    continue
                dfs(v, time + t, passed + [v])

        dfs(0, 0, [0])
        return cnt % (10 ** 9 + 7)

# Time Limit Exceeded 15/56 testcase passed
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [ {} for _ in range(n) ]
        for u, v, t in roads:
            graph[u][v] = t
            graph[v][u] = t

        # print(graph)
        q = [(0, 0, [0])] # (time, node, passed)
        min_time = 10 ** 9 * 200 * 199 / 2 + 1
        cnt = 0

        while q:
            time, node, passed = heapq.heappop(q)
            # print(f'node = {node}, time = {time}, passed = {passed}')
            if node == n - 1:
                if min_time > time:
                    min_time = time
                    cnt = 1
                elif min_time == time:
                    cnt += 1
                continue

            if time > min_time:
                continue

            for v, t in graph[node].items():
                if v in passed:
                    continue
                heapq.heappush(q, (time + t, v, passed + [v]))
            # print(f'q = {q}')

        return cnt
```


## peter
- 
```python
```


## charles
```python
# Solution URL : https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/solutions/6568355/dp-dijkstra-python-c-java-js-c-go-rust-kotlin/
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
            
        dist = [float('inf')] * n
        ways = [0] * n
        
        dist[0] = 0
        ways[0] = 1
        
        pq = [(0, 0)]
        
        MOD = 10**9 + 7
        
        # Dijkstra's algorithm
        while pq:
            d, node = heapq.heappop(pq)
            
            if d > dist[node]:
                continue
                
            for neighbor, time in graph[node]:
                if dist[node] + time < dist[neighbor]:
                    dist[neighbor] = dist[node] + time
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq, (dist[neighbor], neighbor))
                elif dist[node] + time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
        
        return ways[n-1]
```
