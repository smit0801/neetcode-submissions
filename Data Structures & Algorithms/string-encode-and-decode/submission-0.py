class Solution:

    def encode(self, strs: List[str]) -> str:
        res1=''
        for s in strs:
            res1 += str(len(s)) + '#' + s
        return res1
    def decode(self, s: str) -> List[str]:
        res2=[]
        i=0
        while i< len(s):
            j=i
            while s[j] != "#":
                j += 1
            length= int(s[i:j])
            res2.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res2





