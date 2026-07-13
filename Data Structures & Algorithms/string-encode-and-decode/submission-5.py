class Solution:

    def encode(self, strs: List[str]) -> str:
        out = []
        for i in strs:
            out.append(f"{len(i)}#{i}")
        ret = "".join(out)
        return ret
        
    def decode(self, s: str) -> List[str]:
        out = []
        current = ""
        l = len(s)
        n = 0
        read = False
        done = False
        i = 0
        while(i < l):
            c = s[i]
            if not read:
                if c!='#':
                    n = 10*n + int(c)
                else: read = True 
            else:
                current += c
                n-=1
                if n==0: 
                    read = False
                    out.append(current)
                    current = "" 
            i+=1
        if not out:
            out = [""]
        return out