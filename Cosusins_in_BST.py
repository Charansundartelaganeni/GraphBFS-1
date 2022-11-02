#Time_Complexity: O(n)
#Space_Complexity: O(n)

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque() #Initialize q using deque
        q.append(root)  #Append the root into q
        
        
        while q:    #Continue till the q is empty
            size = len(q)  
            level = set()   #Initialize level as a set
            for _ in range(size):   #Continue till the size
                node = q.popleft()  
                level.add(node.val) #Add the node.val in level which acts as the visited set to avoid duplicates
                #If there is left and right children and left value is equal to x and right value equal to y or left value equal to y and right value equal to x
                if (node.left and node.right) and ((node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x)):   
                    return False    #It means they are in the same level and have same parent return False
                
                if node.left:   #If there is left child
                    q.append(node.left) #Append it to the q

                if node.right:  #If there is right child
                    q.append(node.right)    #Append it to the q
                    
            if x in level and y in level:   #If x in level and y in level 
                return True #It means they are in the same level and have different parents return True
            
        return False    #Return False