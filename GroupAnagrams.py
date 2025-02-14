class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            # print(sortedS)
            res[sortedS].append(s)
            # print(res[sorted])
        return list(res.values())
            

        # LOGIC 

        # we made a dictonary and stored all the sorted items as index 
        # eg "act"
        # now "act" is already sorted and next time when cat comes it gets sorted
        # sort of 'cat' is act which is index 
        # at index 'act' -> 'cat' is stored 
        # the res is made a  dict with list values as elements 
        # default dict is used to make this list 
        # at the end we return all the values 
        