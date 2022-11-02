#TC: O(n) 
#SC: O(n) 

class Solution:     
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        gh = defaultdict(list) #create a graph
        self.treetograph(root, None, gh)
       
        # create a visited node list
        visited = {} 
        ans = [] 
       
        # Assign visited as False
        for i in gh:
            visited[i] = False
        # Mark the target node as visited
        visited[target.val] = True
        
        self.dfs(gh, target.val, visited, k, ans) #do the DFS
        return ans 


        # Performing a DFS traversal
    def dfs(self, gh, t, visited, k, ans):

        if k == 0: #if k is 0, then that's at the perfect distance, append it to the answer
            ans.append(t)  
            return
        
        for i in gh[t]: #traverse through the list in graph value with key 't'
            if not visited[i]: 
                visited[i] = True
                self.dfs(gh, i, visited, k-1, ans) 
                visited[i] = False 


    def treetograph(self, root, parent, gh):
        if root:
            # Add the parent node to child node's list
            if parent:
                gh[root.val].append(parent.val) #append the parent if there's one

            if root.left:
                gh[root.val].append(root.left.val) #append the left value

            if root.right:
                gh[root.val].append(root.right.val) #append the right value

            self.treetograph(root.left, root, gh) #do the same dfs again to traverse left side
            self.treetograph(root.right, root, gh) #do the same dfs again to traverse left side