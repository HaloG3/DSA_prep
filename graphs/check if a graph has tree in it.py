'''
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false

Does the given undirected graph form a valid tree?

👉 A graph is a tree if it satisfies two conditions:

Connected → All nodes must be reachable from any starting node.

Acyclic → No cycle should exist.

So, for n nodes and edges, a valid tree must have:

Exactly n-1 edges (since a tree with n nodes always has n-1 edges).

No cycle.

So the given solution uses Union-Find (Disjoint Set Union) to check both conditions:

No cycles.

Single connected component.

Fully connected.

Step by Step for Example 1:

Initially: p = [0,1,2,3,4]

Edge (0,1): union → [1,1,2,3,4] , n=4

Edge (0,2): union → [2,1,2,3,4] , n=3

Edge (0,3): union → [3,1,2,3,4] , n=2

Edge (1,4): union → [3,4,2,3,4] , n=1

✅ n==1, so it’s a valid tree.

'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(x):
            if p[x] != x:      # Path compression
                p[x] = find(p[x])
            return p[x]

        p = list(range(n))     # Initially each node is its own parent

        for a, b in edges:
            if find(a) == find(b):   # If they have the same root → cycle
                return False
            p[find(a)] = find(b)     # Union step
            n -= 1                   # Reduce number of connected components

        return n == 1   # Valid tree if only ONE connected component remains


'''
🔹 Why DFS can also solve this

Union-Find is efficient, but DFS can also be used:

Build adjacency list.

Run DFS from node 0:

After DFS finishes, check if all nodes were visited.

If yes → connected.

If not → disconnected → not a tree.
If you encounter a visited node that is not your parent → cycle.

After DFS, check if all nodes are visited (ensures connectedness).
'''
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree must have exactly n-1 edges
        if len(edges) != n - 1:
            return False
        
        # Build adjacency list
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False  # cycle detected
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:  # ignore the edge back to parent
                    continue
                if not dfs(nei, node):
                    return False
            return True

        # Start DFS from node 0
        if not dfs(0, -1):
            return False
        
        # Check if all nodes are visited (connectedness)
        return len(visited) == n
