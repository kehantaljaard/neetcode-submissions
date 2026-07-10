class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key not in maps:
                maps[key] = []
            maps[key].append(s)
        return list(maps.values())