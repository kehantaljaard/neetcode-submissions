class Solution:

    def encode(self, strs: List[str]) -> str:
        out = []
        for i in strs:
            out.append(f"{len(i)}{i}")
        ret = "".join(out)
        
    def decode(self, s: str) -> List[str]:
        out = []
        current = ""
        n = None
        for c in s:
            if n is None:
                n = int(c)
            if n==0: 
                n = int(c)
                out.append(current)
                current=""
            if n!=0: 
                current+= c
                n-=1