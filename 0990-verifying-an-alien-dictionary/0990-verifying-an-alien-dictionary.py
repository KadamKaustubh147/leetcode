class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = defaultdict(int)

        for i,c in enumerate(order):
            mp[c] = i
        
        

        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            for j in range(len(w1)):

                # prefix violation app and apple
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if mp[w1[j]] > mp[w2[j]]:
                        return False
                    # else will break to return True
                    break
                    
        
        return True

