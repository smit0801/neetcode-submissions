class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        digChar= {"2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"}
        def bT(i,curS):
            if len(curS)== len(digits):
                res.append(curS)
                return
            for c in digChar[digits[i]]:
                bT(i+1,curS+c)
        if digits:
            bT(0,"")
        return res