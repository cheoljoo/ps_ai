# problem : 684. Redundant Connection
- https://leetcode.com/problems/redundant-connection/description/?envType=daily-question&envId=2025-01-29

```txt
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.



Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]


Constraints:
- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= ai < bi <= edges.length
- ai != bi
- There are no repeated edges.
- The given graph is connected.

```

# answer

## al
- union find 알고리즘 사용
- 연결된 노드는 동일한 그룹
- 동일한 그룹간에 연결이 추가될 경우 cycles 을 만든다. 

- ref : https://gmlwjd9405.github.io/2018/08/31/algorithm-union-find.html

- union find (Runtime 3 ms Beats 54.07% / Memory 18.24 MB Beats 54.19%)
```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(p, x):
            if p[x] == x:
                return x
            p[x] = find(p, p[x])
            return p[x]
        def union(p, x, y):
            px = find(p, x)
            py = find(p,y)
            p[py] = px

        parent = [ i for i in range(len(edges) + 1) ]

        for edge in edges:
            x = edge[0]
            y = edge[1]

            if find(parent, x) == find(parent, y):
                break

            union(parent, x, y)

        return edge
```


## peter
- 
```python
```


## charles
- This is similar to grouping problem / find loop.
- 기본 아이디어는 remove하여 cycle이 안 생기게 한다는 것은 , 하나씩 추가해서 cycle이 생길때의 edge를 찾으라는 것과 같은 것으로 ,
- 각 edge를 추가할때마다 loop가 있는지 판별하는게 첫번째 방법이고,
- loop를 찾을때 , parent값을 찾아가게 하면 root parent가 나오게 될 것이며 , edge의 양 노드의 root parent가 같으면 삼각형 모양을 이루게 되어 loop를 나타내게 되어 loop를 찾았다고 할수 있다.
- helpful information : https://github.com/cheoljoo/problemSolving/blob/master/leetcode/README.md#218-grouping--find--union

- recursive method (Runtime 15 ms Beats 10.08% / Memory 18.34 MB Beats 36.87%)
```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.graph = {}   # { node : set()}
        for edge in edges:
            a , b = edge
            if self. find(a,b):
                return edge
            if a not in self.graph:
                self.graph[a] = set()
            self.graph[a].add(b)
            if b not in self.graph:
                self.graph[b] = set()
            self.graph[b].add(a)
        return []
    def find(self,start,target):
        if start not in self.graph:
            return False
        if target not in self.graph:
            return False

        visited = {start}
        if self.go(visited,start,target):
            return True
        visited = {target}
        if self.go(visited,target,start):
            return True
        return False
    def go(self,visited,node,target):
        # print('go',node,target,visited,self.graph)
        for n in self.graph[node]:
            # print(n,target)
            if n == target:
                return True
            if n not in visited:
                visited.add(n)
                if self.go(visited,n,target):
                    return True
        return False
```

- queue (loop) (Runtime 15 ms Beats 10.08% / Memory 18.46 MB Beats 20.15%)
```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.graph = {}   # { node : set()}
        for edge in edges:
            a , b = edge
            if self. find(a,b):
                return edge
            if a not in self.graph:
                self.graph[a] = set()
            self.graph[a].add(b)
            if b not in self.graph:
                self.graph[b] = set()
            self.graph[b].add(a)
        return []
    def find(self,start,target):
        if start not in self.graph:
            return False
        if target not in self.graph:
            return False

        if self.go(start,target):
            return True
        if self.go(target,start):
            return True
        return False
    def go(self,node,target):
        visited = {node}
        q = [node]
        while q:
            # print('q',q,target,visited,self.graph)
            node = q.pop()
            if node == target:
                return True
            for n in self.graph[node]:
                if n == target:
                    return True
                if n not in visited:
                    visited.add(n)
                    q.append(n)
        return False
```

- grouping / union method (Runtime 3 ms Beats 54.19% / Memory 18.28 MB Beats 53.58%)
```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # https://github.com/cheoljoo/problemSolving/blob/master/leetcode/README.md#218-grouping--find--union
        N = 0
        for a,b in edges:
            N = max(N,a)
            N = max(N,b)
        # print(N)
        p = list(range(N+1))  # parent
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                p[py] = px
                return False
            else:
                return True

        for a,b in edges:
            if union(a,b):
                return [a,b]
        return []
```

