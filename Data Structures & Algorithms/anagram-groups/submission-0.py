class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aMap = {}

        for word in strs:
            key = "".join(sorted(word))
            if key in aMap:
                aMap[key].append(word)
            else:
                aMap[key] = [word]
        
        return list(aMap.values())
            
            # diff = target - n
            # if diff in prevMap:
            #     return [prevMap[diff], i]
            # prevMap[n] = i        
        