#TC: O(n)
#SC: O(n)

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        m = len(wordList[0])
        #remove duplicates
        wordList = set(wordList)
        
        #add the begin word in the wordlist set to create graph
        wordList.add(beginWord)
        
        #create adjacency matrix
        matrix = collections.defaultdict(list)
        for word in wordList:
            for i in range(m):
                s = word[:i] + '_' + word[i+1:]
                matrix[s].append(word)
        print(matrix)
            
        # do bfs to find the minimum distance between the begin word to end word in the graph
        queue = [beginWord] #queue will have the beginword
        mark = set()
        mark.add(beginWord) #mark will be the hashset and add the beginword to hashset as well
        dist = 0
        while queue: #traverse until there are elements in queue
            size = len(queue)
            dist += 1 #always increase the distance by 1
            next_queue = [] 
            for _ in range(size):
                word = queue.pop(0) #current word is the first element in queue
                for i in range(m):
                    s = word[:i] + '_' + word[i+1:] #fina all the varieties of string using a special character in the middle
                    for next_word in matrix[s]: #traverse through the graph 
                        if next_word not in mark:
                            if next_word == endWord: #when current word that is not in visited set and equals endword, then it can be connected and the distance will be increased by 1
                                return dist + 1
                            mark.add(next_word) #now add the next word to mark and append it to queue
                            queue.append(next_word)
            #queue = next_queue
            
        return 0