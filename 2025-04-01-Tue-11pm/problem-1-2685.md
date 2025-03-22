# problem : 2685. Count the Number of Complete Components
- https://leetcode.com/problems/count-the-number-of-complete-components/description/?envType=daily-question&envId=2025-03-22

- You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.
- Return the number of complete connected components of the graph.
- A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.
- A connected component is said to be complete if there exists an edge between every pair of its vertices.

- Example 1:
    - ![](https://assets.leetcode.com/uploads/2023/04/11/screenshot-from-2023-04-11-23-31-23.png)
    - Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
    - Output: 3
    - Explanation: From the picture above, one can see that all of the components of this graph are complete.

- Example 2:
    - ![](https://assets.leetcode.com/uploads/2023/04/11/screenshot-from-2023-04-11-23-32-00.png)
    - Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
    - Output: 1
    - Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.    

- Constraints:
    - 1 <= n <= 50
    - 0 <= edges.length <= n * (n - 1) / 2
    - edges[i].length == 2
    - 0 <= ai, bi <= n - 1
    - ai != bi
    - There are no repeated edges.


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
- Runtime 215 ms Beats 5.36% / Memory 18.52 MB Beats 16.83%
- apply group/loop concept -> complelte means all vertics are connected. -> so vertices count is n*(n-1) // 2
```python
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def findParent(node):
            if node == parent[node]:
                return node
            else:
                return findParent(parent[node])
        parent = [ i for i in range(n) ]
        for edge in edges:
            a , b = edge
            aRoot = findParent(a)
            bRoot = findParent(b)
            if aRoot != bRoot:
                parent[aRoot] = bRoot
        # print(parent)
        root = [ 0 ] * n
        rootNodeCount = {}
        edgeCount = {}
        for i in range(n):
            rootA = findParent(i)
            root[i] = rootA
            if rootA not in rootNodeCount:
                rootNodeCount[rootA] = 0
            rootNodeCount[rootA] += 1
            if rootA not in edgeCount:
                edgeCount[rootA] = 0
        # print(root)
        # print(rootNodeCount)
        for a,b in edges:
            edgeCount[findParent(a)] += 1
        # print(edgeCount)
        ans = 0
        for root , nodeCount in rootNodeCount.items():
            if edgeCount[root] == nodeCount * (nodeCount -1) // 2:
                ans += 1
        return ans
```
