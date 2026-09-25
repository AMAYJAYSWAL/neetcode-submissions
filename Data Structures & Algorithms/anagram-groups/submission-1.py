class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}  # Create an empty dictionary

        for s in strs:
            a = sorted(s)  # Sort letters of current word
            # Example: "eat" -> ['a', 'e', 't']

            sortedS = ''.join(a)  # Join sorted letters back into a string
            # ['a', 'e', 't'] -> "aet"

            if sortedS not in res:  # If this sorted word is not already a key
                res[sortedS] = []   # Create an empty list for this group

            res[sortedS].append(s)  # Add original word to its group

        return list(res.values())   # Return all the grouped lists