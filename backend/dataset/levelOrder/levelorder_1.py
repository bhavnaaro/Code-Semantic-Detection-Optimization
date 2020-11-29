from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        sol = []
        def _solve(node, depth=0):
            if node:
                if depth >= len(sol):
                    sol.append([])
                _solve(node.left, depth+1)
                sol[depth].append(node.val)
                _solve(node.right, depth+1)
        _solve(root)
        return sol
