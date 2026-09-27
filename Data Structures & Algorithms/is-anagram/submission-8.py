class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        S={}
        T={}
        for c in s:
            S[c]= 1 +  S.get(c,0)
        for c in t:
            T[c]= 1 +  T.get(c,0)
        return S == T